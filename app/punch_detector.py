import time
from angle_utils import calculate_angle
from config import PUNCH_ANGLE_THRESHOLD, RETRACTION_ANGLE_THRESHOLD, PUNCH_COOLDOWN
from angle_utils import calculate_angle

class PunchDetector:
    def __init__(self, cooldown=0.4):
        self.last_punch_time = {"left": 0, "right": 0}
        self.punch_cooldown = cooldown
        self.arm_retracted = {"left": True, "right": True}

    def detect(self, keypoints):
        now = time.time()
        punches = []

        for kp in keypoints:
            kps = kp.data[0].cpu().numpy()
            left_angle = calculate_angle(kps[5], kps[7], kps[9])
            right_angle = calculate_angle(kps[6], kps[8], kps[10])

            # Left
            if left_angle > PUNCH_ANGLE_THRESHOLD and self.arm_retracted["left"]:
                if (now - self.last_punch_time["left"]) > self.punch_cooldown:
                    punches.append("left")
                    self.last_punch_time["left"] = now
                    self.arm_retracted["left"] = False
            elif left_angle < RETRACTION_ANGLE_THRESHOLD:
                self.arm_retracted["left"] = True

            # Right
            if right_angle > PUNCH_ANGLE_THRESHOLD and self.arm_retracted["right"]:
                if (now - self.last_punch_time["right"]) > self.punch_cooldown:
                    punches.append("right")
                    self.last_punch_time["right"] = now
                    self.arm_retracted["right"] = False
            elif right_angle < RETRACTION_ANGLE_THRESHOLD:
                self.arm_retracted["right"] = True

        return punches