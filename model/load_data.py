import os
import tensorflow as tf
DATA_DIR = "D:\Smart parking\Data\PKLot\PKLotSegm_joined"
dataset = tf.keras.preprocessing.image_dataset_from_directory(
    DATA_DIR, image_size=(54,32), batch_size=1
)
for data, labels in dataset.take(1):
    print(data.shape)
    print(labels.shape)