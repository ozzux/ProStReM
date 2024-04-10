import os
import random
import numpy as np
import sklearn
import sklearn.model_selection
import sklearn.preprocessing
import sklearn.utils

def datafy():
    def extract(struc):
        # Exctracting Proteins as Strings
        grp = open(os.path.join("prot_txt",struc+".txt")).read()
        grp = grp.split(">")
        for prot in range(len(grp)):
            grp[prot] = grp[prot].replace("\n","")
            for ltr in range(len(grp[prot])):
                if grp[prot][ltr] == "S":
                    if grp[prot][ltr+1] == "V":
                        if grp[prot][ltr+2] == "=":
                            grp[prot] = grp[prot].replace(grp[prot][0:ltr+4], "")
                            break

        # Turning Strings into Lists
        for prot in range(len(grp)):
            grp[prot] = list(grp[prot])

        # Randomising Order
        random.shuffle(grp)

        # Shortening List
        grp = grp[0:5000]

        # Letters to Nums
        tcde = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

        for prot in range(len(grp)):
            for ltr in range(len(grp[prot])):
                grp[prot][ltr] = tcde[grp[prot][ltr]]

        # Convert to arrays
        for prot in range(len(grp)):
            grp[prot] = np.array(grp[prot])

        return grp

    fibrous = extract("fibrous")
    globular = extract("globular")

    training_data = []

    for prot in fibrous:
        training_data.append([prot, 0])

    for prot in globular:
        training_data.append([prot, 1])

    random.shuffle(training_data)

    x = []
    y = []

    for feat,lab in training_data:
        x.append(feat)
        y.append(lab)

    # Padding X
    for prot in range(len(x)):
        temp = np.zeros((23000,),dtype="int32")
        shape = x[prot].shape
        temp[:shape[0],] = x[prot]
        x[prot] = temp


    # Splitting Test Data
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.1)

    x_train = np.array(x_train)
    x_test = np.array(x_test)
    y_train = np.array(y_train)
    y_test = np.array(y_test)

    return x_train, x_test, y_train, y_test