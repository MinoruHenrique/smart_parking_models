import cv2

capture  = cv2.VideoCapture("rtsp://admin:Hik12345@192.168.0.102/video")
i=0
while True:
    ret, frame_org = capture.read()
    frame = cv2.resize(frame_org, (1280, 720))
    
    cv2.imshow("image", frame)
    if i == 0:
        cv2.imwrite("ctic.png",frame)
        i+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()