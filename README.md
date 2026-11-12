# REAL-TIME DRIVER DROWSINESS AND DISTRACTION ALERT SYSTEM

### A Computer Vision-Based Driver Safety Application

A real-time computer vision-based application designed to monitor a driver's alertness using a webcam. The system detects the driver's face and eyes, calculates the Eye Aspect Ratio (EAR), and identifies prolonged eye closure as a possible sign of drowsiness. When drowsiness is detected, the system generates a warning and activates an alarm.

## Features

- Real-time driver monitoring using a webcam
- Face detection using Dlib
- 68 facial landmark detection
- Eye landmark detection
- Eye Aspect Ratio (EAR) calculation
- Consecutive-frame validation for drowsiness detection
- Drowsiness warning
- Audible alarm alert
- Graphical User Interface (GUI)
- Start, Stop and Exit controls

## Technologies Used

- Python
- OpenCV
- Dlib
- NumPy
- SciPy
- Imutils
- Pygame
- Tkinter

## How the System Works

The system follows these steps:

1. The webcam captures the driver's video.
2. The system detects the driver's face.
3. Dlib facial landmarks are used to locate the eyes.
4. The Eye Aspect Ratio (EAR) is calculated from the eye landmarks.
5. The EAR value is continuously monitored.
6. If the EAR remains below the defined threshold for consecutive frames, the system identifies possible drowsiness.
7. A drowsiness warning is displayed.
8. An alarm sound is activated to alert the driver.

## Drowsiness Detection Logic

The system uses the Eye Aspect Ratio (EAR) to estimate whether the driver's eyes are open or closed.

When the EAR value falls below the predefined threshold, the system starts counting consecutive frames. The alert is triggered only when the condition continues for the required number of frames. This helps reduce false alerts caused by normal blinking.

## Project Structure

```text
Driver_Drowsiness_Detection/
│
├── main.py
├── gui.py
├── detector.py
├── eye_detector.py
├── alarm.mp3
├── shape_predictor_68_face_landmarks.dat
├── requirements.txt
├── .gitignore
├── .gitattributes
├── README.md
```

> The `env` folder is used for the local Python virtual environment and is excluded from GitHub using `.gitignore`.

## Requirements

Python 3.10 or a compatible Python version is recommended.

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

## Running the Project

Activate the virtual environment and run the GUI:

```bash
python gui.py
```

The application opens the graphical interface. Start the detection and allow the webcam to monitor the driver's face and eyes.

## Facial Landmark Model

The project uses the Dlib 68-point facial landmark model:

```text
shape_predictor_68_face_landmarks.dat
```

This file is tracked using **Git LFS** because of its large size.

Make sure Git LFS is installed and enabled before cloning or downloading the repository.

## Important Files

| File | Description |
|---|---|
| `main.py` | Main project execution file |
| `gui.py` | Graphical user interface |
| `detector.py` | Face detection and related detection functionality |
| `eye_detector.py` | Eye landmark and eye-related detection functionality |
| `alarm.mp3` | Alarm sound used for drowsiness alert |
| `shape_predictor_68_face_landmarks.dat` | Dlib facial landmark model |
| `requirements.txt` | Required Python libraries |
| `.gitignore` | Files and folders excluded from Git |
| `.gitattributes` | Git LFS configuration |

## Testing

The system was tested for:

- Webcam initialization
- Face detection
- Eye landmark detection
- EAR calculation
- Normal eye-open condition
- Continuous eye-closed condition
- Drowsiness warning
- Alarm activation
- GUI controls

## Project Output

The system provides two main operating conditions:

### Normal Monitoring

The webcam continuously monitors the driver's eyes and displays the current monitoring status and EAR value.

### Drowsiness Detection

When prolonged eye closure is detected, the system displays a drowsiness warning and activates the alarm to alert the driver.

## Future Scope

The system can be further improved by adding:

- Yawning detection
- Head-pose estimation
- Improved low-light detection
- Deep learning-based drowsiness classification
- Mobile application support
- IoT-based vehicle safety integration
- Multi-feature driver state analysis

## Author

**Amit Karnwal**

BCA  
Department of Computer Science & Application  
COER University, Roorkee

## Project Type

BCA Minor Project

**Session:** 2026–2027