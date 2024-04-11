import tensorflow as tf
import processing
import numpy as np

model = tf.keras.models.load_model("model.keras")

# x_train, x_test, y_train, y_test = processing.datafy()

# val_loss, val_acc = model.evaluate(x_test,y_test)

# print(val_acc)

def ProStReM(protein, model):
    # Converting Protein String to Array
    protein = list(protein)

    tcde = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

    try:
        for ltr in range(len(protein)):
            protein[ltr] = tcde[protein[ltr]]
    except:
        return "invalid input"
    
    protein = np.array(protein)

    # Padding
    shape = protein.shape
    temp = np.zeros((23000,), dtype="int32")
    temp[:shape[0],] = protein
    protein = temp

    # Predict
    prediction = model.predict(np.array([protein]))

    return prediction

prot = input("Paste the protein sequence: ")

result = ProStReM(prot,model)
print(result)
if result[0][0] >= 0.5:
    result = "Globular"
else:
    result = "Fibrous"

print(result)