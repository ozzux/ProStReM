import tensorflow as tf
import pickle


while True:
    from processing import x_train, x_test, y_train, y_test
    print(x_train[0])
    model = tf.keras.Sequential()

    model.add(tf.keras.layers.InputLayer((23000,)))
    model.add(tf.keras.layers.Activation(tf.nn.relu))
    model.add(tf.keras.layers.Dense(500, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(500, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(500, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(500, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(500, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(500, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(500, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(1, activation=tf.nn.sigmoid))

    model.compile(optimizer="adam", loss=tf.losses.binary_crossentropy, metrics=["accuracy"])
    model.fit(x_train, y_train, epochs=10)
    val_loss, val_acc = model.evaluate(x_test,y_test)
    print(val_acc)
    if val_acc >= 0.8:
        break

print(val_acc)

pickle_out = open("model.pickle", "wb")
pickle.dump(model, pickle_out)
pickle_out.close()