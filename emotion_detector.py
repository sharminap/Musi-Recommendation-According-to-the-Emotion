import cv2
from fer import FER

def detect_emotion():
    detector = FER(mtcnn=True)
    cam = cv2.VideoCapture(0)
    emotion_detected = "neutral"

    print("Press 'q' to capture emotion")

    while True:
        ret, frame = cam.read()
        if not ret:
            break
        cv2.imshow("Emotion Detection", frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            results = detector.detect_emotions(frame)
            if results:
                emotion_scores = results[0]["emotions"]
                emotion_detected = max(emotion_scores, key=emotion_scores.get)
            break

    cam.release()
    cv2.destroyAllWindows()
    return emotion_detected