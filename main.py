import pickle
import tensorflow as tf
import processing

pickle_in = open("model(0.821).pickle","rb")
model = pickle.load(pickle_in)
pickle_in.close()

x_train, x_test, y_train, y_test = processing.datafy()

val_loss, val_acc = model.evaluate(x_test,y_test)

print(val_acc)