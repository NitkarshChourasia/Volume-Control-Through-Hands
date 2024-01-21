# Hand Gesture Volume Control with Python and OpenCV 🤚🎚

Control your computer's volume with a wave of your hand! This Python script utilizes the OpenCV library to detect hand landmarks and adjust the system volume using the PyAutoGUI library.

## Requirements
- Python 3.x
- OpenCV (`pip install opencv-python`)
- Mediapipe (`pip install mediapipe`)
- PyAutoGUI (`pip install pyautogui`)

## How it Works
1. Captures video from your webcam.
2. Detects hand landmarks using the Mediapipe library.
3. Tracks the movement of the forefinger and thumb.
4. Calculates the distance between them to determine the hand gesture.
5. Adjusts system volume using PyAutoGUI based on the hand gesture.

## Setup
1. Install the required libraries: `pip install opencv-python mediapipe pyautogui`
2. Run the script: `python hand_volume_control.py`
3. Use your forefinger and thumb gestures to control the volume.

## Controls
- Pinch: Decrease volume
- Spread: Increase volume
- Press `ESC` to exit the application.

Feel free to customize the script according to your preferences! Happy coding! 🚀

**Note:** Ensure your system supports volume control via keyboard shortcuts for the script to work effectively.

---

*Disclaimer: This project is for educational purposes and may require adjustments based on your system's configuration.*