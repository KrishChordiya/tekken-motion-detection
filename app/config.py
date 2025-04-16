from cv2 import FONT_HERSHEY_SIMPLEX
# Model
MODEL_PATH = 'models/yolov8n-pose.pt'

# Device
USE_CUDA_IF_AVAILABLE = True

# Key Bindings
KEY_MAP = {
    "left": "a",
    "right": "d",
    "punch_left": "u",
    "punch_right": "i"
}

# Punch Detection
PUNCH_ANGLE_THRESHOLD = 80
RETRACTION_ANGLE_THRESHOLD = 10
PUNCH_COOLDOWN = 0.4  # seconds

# Tilt Detection
TILT_LEFT_THRESHOLD = 0.57
TILT_RIGHT_THRESHOLD = 0.45

# Debug Mode
DEBUG_FONT = FONT_HERSHEY_SIMPLEX
DEBUG_COLOR = (0, 255, 255)
DEBUG_ANGLE_COLOR = (0, 255, 0)
LEFT_ARM_COLOR = (255, 0, 0)
RIGHT_ARM_COLOR = (0, 0, 255)