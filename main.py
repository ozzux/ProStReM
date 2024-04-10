import tensorflow as tf
from processing import x_train, x_test, y_train, y_test

model = tf.keras.Sequential()

model.add(tf.keras.layers.InputLayer((23000,)))
model.add(tf.keras.layers.Activation(tf.nn.relu))
model.add(tf.keras.layers.Dense(400, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(400, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(1, activation=tf.nn.sigmoid))

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(x_train, y_train, epochs=5)

val_loss, val_acc = model.evaluate(x_test,y_test)


print(val_acc)