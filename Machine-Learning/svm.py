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



""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# cut the data set to 1/100
features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100]
# acc = 0.884527 small data set, less time, less acc


from sklearn.svm import SVC
clf = SVC(kernel='rbf',C=10000.)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
answer = pred[50]
print(answer)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred,labels_test)
print(acc)
# -> no. of Chris training emails: 7936
# -> no. of Sara training emails: 788
# -> 0.98407 

# the SVM is MUCH slower to train and use for predicting.

# Try1: downsize the data set: 0.88 acc but much faster
# Try2: change the kernel from 'linear' to 'rbf' use small data set: 0.62 acc
# Try3: C=10.0 acc=0.62 / C=100.0 acc=0.62 / C=1000.0 acc=0.82 / C=10000.0 acc=0.89
# Try4: kernel='rbf' / C=10000.0 / full data set / acc=0.99

# In 99% acc condition, check the np.100 element in predition: pred[100] = 0 (Sara)
