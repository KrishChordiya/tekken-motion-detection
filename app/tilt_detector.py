from config import TILT_LEFT_THRESHOLD, TILT_RIGHT_THRESHOLD

def detect_body_tilt(results, frame_width, model_names):
    for box in results.boxes:
        cls_id = int(box.cls[0])
        label = model_names[cls_id]
        if label == "person":
            x1, _, x2, _ = map(int, box.xyxy[0])
            center_x = (x1 + x2) // 2
            norm_cx = center_x / frame_width
            if norm_cx < TILT_RIGHT_THRESHOLD:
                return "right"
            elif norm_cx > TILT_LEFT_THRESHOLD:
                return "left"
            else:
                return "center"
    return "center"
