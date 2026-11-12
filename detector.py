import cv2
import dlib
from imutils import face_utils


detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor(
    "shape_predictor_68_face_landmarks.dat"
)


cap = cv2.VideoCapture(0)


while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    for face in faces:

        landmarks = predictor(gray, face)

        landmarks = face_utils.shape_to_np(landmarks)

        for (x, y) in landmarks:
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)


    cv2.imshow("68 Face Landmark Detection", frame)


    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()