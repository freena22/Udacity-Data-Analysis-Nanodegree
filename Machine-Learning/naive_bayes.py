
### sklearn.naive_bayes.GaussianNB

# official example

import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
print(clf.predict([[-0.8, -1]])) # -> [1]
print(clf.predict([1, 2])) # -> [2]



from sklearn.metrics import accuracy_score
x = [1, 1, 1, 4, 3, 5]
y = [1, 1, 1, 2, 2, 2]
print(accuracy_score(x,y))
# -> 0.5


""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
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



from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
clf = GaussianNB()
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
print(pred) #-> [001]
print(accuracy_score(pred,labels_test))
# -> 0.973265


