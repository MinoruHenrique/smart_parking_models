import tensorflow as tf
import os
import numpy as np
import time
from matplotlib import pyplot as plt
import cv2
from utils import load_spaces, crop_from_space

spaces = load_spaces(r"C:\Users\Usuario\Documents\proyectos\smart_parking\carnet\new_spaces.txt")
model = tf.keras.models.load_model(r'C:\Users\Usuario\Documents\proyectos\smart_parking\carnet\model\Carnet_transfer.h5')

DATA_DIR = "D:\Smart parking\Data\CTIC_2023"

images = os.listdir(DATA_DIR)
time_measurements = [[1],[2],[3],[4],[5],[6],[7]]

for image in images:
    img = cv2.imread(os.path.join(DATA_DIR, image))
    img = cv2.resize(img, (1280, 720), fx = 0, fy = 0,
                         interpolation = cv2.INTER_CUBIC)
    for cant_spaces in range(1,8):
        start = time.time()
        cropped_imgs = []
        for space in spaces[:cant_spaces]:
            cropped_img = crop_from_space(img, space)
            cropped_img = cv2.resize(cropped_img, (32,54))/255
            space = np.array(space).reshape(-1,1,2)
            cropped_imgs.append(cropped_img)
        cropped_imgs = np.array(cropped_imgs)
        predicts = model.predict(cropped_imgs, batch_size=cant_spaces)
        end = time.time()
        elapsed = end-start
        time_measurements[cant_spaces-1].append(elapsed)
time_measurements = np.array(time_measurements)
        
# print(time_measurements)
x = [1,2,3,4,5,6,7]
y = []
for times in time_measurements:
    mean = np.mean(times[1:])
    y.append(mean)
print(x)
print(y)
plt.figure()
plt.bar(x,y)
plt.xlabel("Cantidad de parkings")
plt.ylabel("Tiempo elapsed (s)")
plt.show()