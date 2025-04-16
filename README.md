# 🎮 Tekken Gesture Control (Punch + Movement via Webcam)

Control your Tekken fighter using real-time upper body gestures captured through your webcam!  
This project detects punches and body tilts using pose estimation powered by **YOLOv8 Pose**, triggering keypresses to control the game.

## 📦 Features

- 🥊 **Punch Detection**: Left and right punches using elbow-wrist-shoulder angles.
- ↔️ **Tilt Detection**: Move left or right based on upper body tilt.
- 🔁 **Real-time Detection** using `YOLOv8` and `OpenCV`.
- ⌨️ **Virtual Keypresses** sent using the `keyboard` module.


## 📽️ Demo

> Coming soon!  
> A short clip will be added here showing punches and movements mapped to keyboard keys.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/tekken-gesture-control.git
cd tekken-gesture-control
```
### 2. Install Dependencies

```bash
pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu118
```
> ⚠️ For GPU support, make sure PyTorch is installed with CUDA.

### 3. Download the YOLOv8 Pose Model
```bash
mkdir models
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n-pose.pt -P models/
```
Or place `yolov8n-pose.pt` manually inside the `models/` directory.

## 🛠 Usage
Run the program in **debug setup mode** first to visualize detection:
```bash
python main.py
```
-   Press `q` to exit setup mode.
-   To disable debug overlay and begin controlling with gestures, set `setup=False` in `main.py` or modify the logic accordingly.

## ⚙️ Customization
You can tweak the following settings in `config.py`:
-   `KEY_MAP`: Modify movement and attack keys
-   Angle thresholds for punch detection
-   Device preference (CPU/GPU)

## 🙌 Acknowledgements
-   [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
-   [OpenCV](https://opencv.org/)
-   [PyTorch](https://pytorch.org/)
-   You — for trying this out!
