import cv2
import dlib
from scipy.spatial import distance
from imutils import face_utils


def eye_aspect_ratio(eye):

    A = distance.euclidean(
        eye[1],
        eye[5]
    )

    B = distance.euclidean(
        eye[2],
        eye[4]
    )

    C = distance.euclidean(
        eye[0],
        eye[3]
    )

    ear = (A + B) / (2.0 * C)

    return ear



detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor(
    "shape_predictor_68_face_landmarks.dat"
)


(leftStart,leftEnd)=face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]

(rightStart,rightEnd)=face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]



cap=cv2.VideoCapture(0)



while True:

    ret,frame=cap.read()

    gray=cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )


    faces=detector(gray)


    for face in faces:

        landmarks=predictor(
            gray,
            face
        )


        landmarks=face_utils.shape_to_np(
            landmarks
        )


        leftEye=landmarks[
            leftStart:leftEnd
        ]

        rightEye=landmarks[
            rightStart:rightEnd
        ]


        leftEAR=eye_aspect_ratio(leftEye)

        rightEAR=eye_aspect_ratio(rightEye)


        ear=(leftEAR+rightEAR)/2


        cv2.putText(
            frame,
            f"EAR: {ear:.2f}",
            (20,30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )


        for point in leftEye:
            cv2.circle(
                frame,
                tuple(point),
                2,
                (0,255,255),
                -1
            )


        for point in rightEye:
            cv2.circle(
                frame,
                tuple(point),
                2,
                (0,255,255),
                -1
            )


    cv2.imshow(
        "EAR Eye Detection",
        frame
    )


    if cv2.waitKey(1)==27:
        break



cap.release()
cv2.destroyAllWindows()