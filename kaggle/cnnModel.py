from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, Dropout

img_rows, img_cols = 28, 28
num_classes = 10

batch_size = 16

fashion_model = Sequential()
fashion_model.add(Conv2D(16, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(img_rows, img_cols, 1)))
fashion_model.add(Conv2D(16, (3, 3), activation='relu'))
fashion_model.add(Flatten())
fashion_model.add(Dense(128, activation='relu'))
fashion_model.add(Dense(num_classes, activation='softmax'))

fashion_model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer='adam',
              metrics=['accuracy'])

fashion_model.fit(x, y,
          batch_size=batch_size,
          epochs=3,
          validation_split = 0.2)