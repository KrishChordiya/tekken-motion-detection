import torch
import keyboard
from ultralytics import YOLO
from punch_detector import PunchDetector
from tilt_detector import detect_body_tilt
from config import MODEL_PATH, KEY_MAP, USE_CUDA_IF_AVAILABLE

class GestureControl:
    def __init__(self, setup=False):
        self.setup = setup
        self.device = "cuda" if USE_CUDA_IF_AVAILABLE and torch.cuda.is_available() else "cpu"
        self.model = YOLO(MODEL_PATH).to(self.device)
        self.state = "center"
        self.holding = False
        self.key_map = KEY_MAP
        self.punch_detector = PunchDetector()

    def detect_tilt(self, results, frame_width):
        return detect_body_tilt(results, frame_width, self.model.names)

    def detect_punches(self, results):
        return self.punch_detector.detect(results.keypoints)

    def handle_movement(self, new_state):
        if new_state == self.state:
            return

        if new_state in ["left", "right"]:
            if not self.holding:
                keyboard.press(self.key_map[new_state])
                self.holding = True
                print(f"Holding {self.key_map[new_state].upper()}")
        elif new_state == "center" and self.state in ["left", "right"]:
            key = self.key_map[self.state]
            keyboard.release(key)
            keyboard.press_and_release(key)
            self.holding = False
            print(f"Released {key.upper()}, tapped once")

        self.state = new_state