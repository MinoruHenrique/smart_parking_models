import cv2
import os
import pickle
import time
def load_pickle_file(file):
    with open(file,'rb') as f:
        unpickled_file = pickle.load(f)
    return unpickled_file

DEST_DIR = "D:\Smart parking\Data\CTIC_2023_v4"
T_SAMP = 15*60#30MIN

capturadora = cv2.VideoCapture("rtsp:admin:Hik12345@192.168.0.100/video")


time_last = time.time()
first = True
i=0
(cameraMatrix, dist) = load_pickle_file(r'C:\Users\Usuario\Documents\proyectos\smart_parking\carnet\capture_data\calibration.pkl')
while True:
    if capturadora.grab():
        ret, frame = capturadora.read()
        if not ret:
            # print("Frame lost")
            continue
        cv2.imshow('org', frame)
        h,w = frame.shape[:2]
        time_now = time.time()
        newCameraMatrix, roi = cv2.getOptimalNewCameraMatrix(cameraMatrix, dist, (w,h), 1, (w,h))
        dst = cv2.undistort(frame, cameraMatrix, dist, None, newCameraMatrix)

        # crop the image
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]
        dst = cv2.resize(dst, (1280,720))
        cv2.imshow('Disorted', dst)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if(first or time_now-time_last>=T_SAMP):
            time_name = f"{time.asctime()}.png".replace(":", "-")
            # time_name = f"{i}.png"
            # i+=1
            file_path = os.path.join(DEST_DIR, time_name)
            cv2.imwrite(file_path, dst)
            print(f"{file_path} written")
            time_last = time_now
            first = False

capturadora.release()
cv2.destroyAllWindows()