import cv2
import time
import os
DEST_DIR = "D:\Smart parking\Data\CTIC_2023_v2"
T_SAMP = 30*60#30MIN
capture  = cv2.VideoCapture("rtsp://admin:Hik12345@192.168.0.100/video")
time_last = time.time()
first = True
i=0
while True:
    ret, frame_org = capture.read()
    frame = cv2.resize(frame_org, (1280, 720))
    time_now = time.time()
    cv2.imshow("image", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if(first or time_now-time_last>=T_SAMP):
        time_name = f"{time.asctime()}.png".replace(":", "-")
        # time_name = f"{i}.png"
        # i+=1
        file_path = os.path.join(DEST_DIR, time_name)
        cv2.imwrite(file_path, frame)
        print(f"{file_path} written")
        time_last = time_now
        first = False
    
capture.release()
cv2.destroyAllWindows()