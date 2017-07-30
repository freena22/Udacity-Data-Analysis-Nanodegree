### Support Vector machine

# Offical Example
import numpy as np
x = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
from sklearn.svm import SVC
clf = SVC()
clf.fit(x, y) 
print(clf.predict([[-0.8, -1]])) #-> [1]

# Class Practice
import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import copy
import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()


from sklearn.svm import SVC
clf = SVC(kernel="linear")
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
def submitAccuracy():
    return acc
# -> 0.92
