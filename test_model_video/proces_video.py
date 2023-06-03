import cv2
import numpy as np
import tensorflow as tf
import time
from utils import load_spaces, crop_from_space
VIDEO_PATH = "C:/Users/Usuario/Pictures/video_def.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)
while not cap.isOpened():
    cap = cv2.VideoCapture(VIDEO_PATH)
    cv2.waitKey(1000)
    print("Wait for the header")

width= 960
height= 540
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
writer= cv2.VideoWriter('video_postprocess.avi',fourcc, 30, (width,height))

spaces = load_spaces(r"C:\Users\Usuario\Documents\proyectos\smart_parking\carnet\new_spaces.txt")
model = tf.keras.models.load_model(r'C:\Users\Usuario\Documents\proyectos\smart_parking\carnet\alternative_models\Xception.pt')
print("Init processing")
# used to record the time when we processed last frame
prev_frame_time = 0
  
# used to record the time at which we processed current frame
new_frame_time = 0
i=0
while (cap.isOpened()):
 
    # Capture frame-by-frame
    ret, frame = cap.read()
#  cv2.polylines(image, [refPt], True, (0,0,255), 2)
    # Display the resulting frame
    # cv2.imshow('Frame', frame)
    frame = cv2.resize(frame, (1280, 720), fx = 0, fy = 0,
                         interpolation = cv2.INTER_CUBIC)
    cropped_imgs = []
    for space in spaces:
        cropped_img = crop_from_space(frame, space)
        cropped_img = cv2.resize(cropped_img, (32,54))/255
        space = np.array(space).reshape(-1,1,2)
        cropped_imgs.append(cropped_img)
    cropped_imgs = np.array(cropped_imgs)
    predicts = model.predict(cropped_imgs)
    # print(predicts)
    for space, predict in zip(spaces,predicts):
        predict = predict[0]
        space = np.array(space).reshape(-1,1,2)
        if predict >= 0.5:
            # cv2.imwrite("C:\\Users\\Usuario\\Documents\\proyectos\\smart_parking\\carnet\\Occ\\"+str(i)+".jpg", cropped_img)
            color = (0,0,255)
            # print(f"{i}Occ")
        else:
            # cv2.imwrite("C:\\Users\\Usuario\\Documents\\proyectos\\smart_parking\\carnet\\Empt\\"+str(i)+".jpg", cropped_img)
            color = (0,255,0)
            # print(f"{i}Empt")
        cv2.polylines(frame, [space], True, color, 2)
        # i+=1
        # # print(cropped_img)
        # # print(cropped_img.shape)
        # # print(type(cropped_img))
        # class_predict = model.predict(img_model)[0][0]
        # # 
        # if class_predict >= 0.5:
        #     # cv2.imwrite("C:\\Users\\Usuario\\Documents\\proyectos\\smart_parking\\carnet\\Occ\\"+str(i)+".jpg", cropped_img)
        #     color = (0,0,255)
        #     # print(f"{i}Occ")
        # else:
        #     # cv2.imwrite("C:\\Users\\Usuario\\Documents\\proyectos\\smart_parking\\carnet\\Empt\\"+str(i)+".jpg", cropped_img)
        #     color = (0,255,0)
        #     # print(f"{i}Empt")
        # cv2.polylines(frame, [space], True, color, 2)
        # # i+=1
        
    frame = cv2.resize(frame, (width, height), fx = 0, fy = 0,
                         interpolation = cv2.INTER_CUBIC)
    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    fps = str(int(fps))
    cv2.putText(frame, fps, (7, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)
    writer.write(frame)
    cv2.imshow('Thresh', frame)
    # define q as the exit button
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    if cap.get(1) == cap.get(7):
        # If the number of captured frames is equal to the total number of frames,
        # we stop
        break
    elif(i%500==0):
        print(f"{cap.get(1)} of {cap.get(7)} frames")
    i+=1
 
# release the video capture object
cap.release()
writer.release()
# Closes all the windows currently opened.
cv2.destroyAllWindows()