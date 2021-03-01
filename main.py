import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=3)
    cv2.imshow("press q to exit", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break;

video.release()
cv2.destroyAllWindows()



