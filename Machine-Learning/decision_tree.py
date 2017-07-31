### Decision Tree

# Offical Example - Classfier
from sklearn import tree
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
print(clf.predict([[2., 2.]]))  # -> [1]


# Coding a decision tree quiz
from sklearn import tree
def classify(features_train, labels_train):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features_train, labels_train)
    return clf

# Decision tree accuracy
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()


from sklearn import tree
from sklearn.metrics import accuracy_score
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(pred, labels_test)
    
def submitAccuracies():
  return {"acc":round(acc,3)}
# -> acc:0.908
# result is Ok but can adjust parameters to improve the overfitting

# 1. min_samples_split: default=2
clf1 = tree.DecisionTreeClassifier(min_samples_split=50)
clf1 = clf1.fit(features_train,labels_train)
pred1 = clf1.predict(features_test)
acc_min_samples_split_2 = accuracy_score(pred1, labels_test) # -> 0.912

clf2 = tree.DecisionTreeClassifier(min_samples_split=2)
clf2 = clf2.fit(features_train,labels_train)
pred2 = clf2.predict(features_test)
acc_min_samples_split_50 = accuracy_score(pred2, labels_test) # -> 0.908



""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
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

# get a decision tree up and running as a classifier, setting min_samples_split=40
clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf = clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(pred, labels_test)
print(acc) # -> 0.977

# Another way to control the complexity of an algorithm is via the number of features that you use in training/testing. 
# The more features the algorithm has available, the more potential there is for a complex fit

print(len(features_train[0])) # -> 3785

# change 'email_preprocess.py': 

# selector = SelectPercentile(f_classif, percentile=10) to percentile=1 
# -- only uses 1% of the available features (less complicated structure)


print(len(features_train[0])) # -> 379 / acc=0.967 


