import cv2
import dlib
from scipy.spatial import distance
from imutils import face_utils
import pygame


# ----------------------------
# ALARM SETUP
# ----------------------------
pygame.mixer.init()
pygame.mixer.music.load("alarm.mp3")


# ----------------------------
# SETTINGS
# ----------------------------
EAR_THRESHOLD = 0.25
EAR_CONSEC_FRAMES = 20

counter = 0


# ----------------------------
# EAR FUNCTION
# ----------------------------
def eye_aspect_ratio(eye):

    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])

    ear = (A + B) / (2.0 * C)

    return ear


# ----------------------------
# FACE DETECTOR
# ----------------------------
detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor(
    "shape_predictor_68_face_landmarks.dat"
)


# ----------------------------
# EYE LANDMARK INDEXES
# ----------------------------
(leftStart, leftEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rightStart, rightEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]


# ----------------------------
# START CAMERA
# ----------------------------
cap = cv2.VideoCapture(0)


while True:

    ret, frame = cap.read()

    if not ret:
        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)


    # Default status
    status = "STATUS: DRIVER ALERT"


    for face in faces:

        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)


        # Extract eyes
        leftEye = landmarks[leftStart:leftEnd]
        rightEye = landmarks[rightStart:rightEnd]


        # Calculate EAR
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        ear = (leftEAR + rightEAR) / 2.0


        # Display EAR
        cv2.putText(
            frame,
            f"EAR: {ear:.2f}",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )


        # ----------------------------
        # EYES CLOSED
        # ----------------------------
        if ear < EAR_THRESHOLD:

            counter += 1
            status = "STATUS: EYES CLOSED"


            # If eyes remain closed for 20 frames
            if counter >= EAR_CONSEC_FRAMES:

                status = "DROWSINESS DETECTED! WAKE UP!"

                # Play alarm
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play()

        else:

            counter = 0

            # Stop alarm
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()


    # ----------------------------
    # DISPLAY STATUS
    # ----------------------------
    cv2.putText(
        frame,
        status,
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255) if counter >= EAR_CONSEC_FRAMES else (0, 255, 0),
        2
    )


    # Camera window
    cv2.imshow(
        "Driver Drowsiness Detection System",
        frame
    )


    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break


# ----------------------------
# CLOSE PROGRAM
# ----------------------------
cap.release()
cv2.destroyAllWindows()
pygame.mixer.music.stop()
pygame.quit()