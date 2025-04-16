import cv2
import time
import keyboard
from gesture_controller import GestureControl
from angle_utils import calculate_angle
from config import KEY_MAP, DEBUG_COLOR, DEBUG_FONT, DEBUG_ANGLE_COLOR, LEFT_ARM_COLOR, RIGHT_ARM_COLOR

def draw_debug(frame, results, punches, direction):
    cv2.putText(frame, f'Tilt: {direction}', (20, 30), DEBUG_FONT, 1, DEBUG_COLOR, 2)
    
    for p in punches:
        y = 50 if p == "left" else 70
        cv2.putText(frame, f"{p.capitalize()} Punch", (20, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    for kp in results.keypoints:
        kps = kp.data[0].cpu().numpy()
        joints = {
            "left": (kps[5][:2], kps[7][:2], kps[9][:2]),
            "right": (kps[6][:2], kps[8][:2], kps[10][:2])
        }

        for side, (shoulder, elbow, wrist) in joints.items():
            angle = calculate_angle(shoulder, elbow, wrist)
            wx, wy = int(wrist[0]), int(wrist[1])
            cv2.putText(frame, f"{angle:.1f}°", (wx + 20, wy - 20), DEBUG_FONT, 0.8, DEBUG_ANGLE_COLOR, 2)
            color = (255, 0, 0) if side == "left" else (0, 0, 255)
            cv2.line(frame, tuple(map(int, shoulder)), tuple(map(int, elbow)), LEFT_ARM_COLOR if side == "left" else RIGHT_ARM_COLOR, 2)    


    cv2.imshow('Tekken Gesture Control - Setup', frame)

def main():
    controller = GestureControl(setup=True)
    print(f"Using CUDA: {controller.device == 'cuda'}")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Webcam not found.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        results = controller.model(frame, verbose=False)[0]
        direction = controller.detect_tilt(results, frame.shape[1])
        punches = controller.detect_punches(results)

        if controller.setup:
            draw_debug(frame, results, punches, direction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            controller.handle_movement(direction)
            for p in punches:
                key = KEY_MAP["punch_left"] if p == "left" else KEY_MAP["punch_right"]
                keyboard.press(key)
                time.sleep(0.05)
                keyboard.release(key)
                print(f"{p.capitalize()} punch - {key.upper()}")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
