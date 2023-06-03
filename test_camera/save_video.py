import cv2

cap= cv2.VideoCapture("rtsp://admin:Hik12345@192.168.0.105/video")

width= 960
height= 540
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
writer= cv2.VideoWriter('video2.avi',fourcc, 10, (width,height))


while True:
    ret,frame= cap.read()
    frame = cv2.resize(frame, (width,height))

    writer.write(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
writer.release()
cv2.destroyAllWindows()