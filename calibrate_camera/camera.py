import cv2
import os
capturadora = cv2.VideoCapture("rtsp:admin:Hik12345@192.168.0.100/video")

while True:
    ret, frame_org = capturadora.read()
    frame = cv2.resize(frame_org, (1280, 720))
    cv2.imshow('captura', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
            i = len(os.listdir("./captures"))
            cv2.imwrite(f"./captures/{i}.jpg", frame_org)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capturadora.release()
cv2.destroyAllWindows()