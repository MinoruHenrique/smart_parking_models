from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import SGD
from keras.regularizers import l2

"""
Carnet model implementation based on paper:
"Generalized Parking Occupancy Analysis Based on Dilated Convolutional Neural Network"
"""

model = Sequential(name="Carnet")
WEIGHT_DECAY = 0.0005
regularizer = l2(WEIGHT_DECAY)

#Conv1
model.add(Conv2D(96, kernel_size=(11, 11), dilation_rate=2, activation='relu',
                 input_shape=(54, 32, 3), padding='same', kernel_regularizer=regularizer))
model.add(MaxPooling2D(pool_size=(2, 2), strides=2))

#Conv2
model.add(Conv2D(192, kernel_size=(5, 5), dilation_rate=2, activation='relu',
                 padding='same', kernel_regularizer=regularizer))
model.add(MaxPooling2D(pool_size=(2, 2)))

#Conv3
model.add(Conv2D(384, kernel_size=(3, 3), dilation_rate=2, activation='relu',
                 padding='same', kernel_regularizer=regularizer))
model.add(MaxPooling2D(pool_size=(2, 2)))

#Flatten
model.add(Flatten())

#FC1
model.add(Dense(4096, activation='relu',
                kernel_regularizer=regularizer))
model.add(Dropout(.2))

#FC2
model.add(Dense(4096, activation='relu',
                kernel_regularizer=regularizer))
model.add(Dropout(.2))

#Output
model.add(Dense(2, activation='sigmoid'))

opt = SGD(learning_rate=0.00001,
          momentum=0.99)
model.compile(optimizer=opt, loss='binary_crossentropy')

print(model.summary())