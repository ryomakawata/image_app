import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.python.keras.utils import np_utils
from tensorflow.python.keras.applications import VGG16

#パラメータの初期化
classes = ["lion","tiger"]
num_classes = len(classes)
image_size = 224

#データの読み込み
x_train,x_test,y_train,y_test = np.load("./imagefiles_224.npy",allow_pickle=True)
y_train = np_utils.to_categorical(y_train,num_classes)
y_test = np_utils.to_categorical(y_test,num_classes)
x_train = x_train.astype("float") / 255.0
x_test = x_test.astype("float") / 255.0

#モデルの定義
model = VGG16(weights='imagenet', include_top=False,input_shape=(image_size,image_size,3))
#print('Model_loaded')
#model.summary()

top_model = Sequential()
top_model.add(Flatten(input_shape=model.output_shape[1:]))
top_model.add(Dense(256, activation='relu'))
top_model.add(Dropout(0.5))
top_model.add(Dense(num_classes, activation='softmax'))

model = Model(inputs=model.input,outputs=top_model(model.output))

for layers in model.layers [:15]:
    layers.trainable = False

opt = Adam(lr=0.0001)

#opt = SGD(lr=0.01, momentum=0.0, nesterov=False)
model.compile(loss='categorical_crossentropy',optimize=opt,metrics=['accuracy'])

model.fit(x_train,y_train,batch_size=32,epochs=18)

score = model.evaluate(x_test,y_test,batch_size=32)

model.save("./vgg16_transfer.h5")