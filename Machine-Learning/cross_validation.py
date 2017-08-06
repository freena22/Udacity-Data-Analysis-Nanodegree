### Cross-validation

# offical exampple

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
features = iris.data
labels = iris.target

print(features.shape) # -> (150,4)
print(labels.shape) # -> (150,)


from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
    features, labels, test_size=0.4, random_state=0)

print(features_train.shape, labels_train.shape) # -> (90, 4)(90,)
print(features_test.shape, labels_test.shape) # -> (60, 4)(60,)

clf = svm.SVC(kernel='linear', C=1).fit(features_train,labels_train)
print(clf.score(features_test, labels_test)) # 0.967
print(clf.score(features_train, labels_train)) # 0.989

# GridSearchCV: systematically working through multiple combinations of parameter tunes
# cross-validating as it goes to determine which tune gives the best performance
from sklearn import svm, grid_search, datasets
iris = datasets.load_iris()
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svr = svm.SVC()
clf = grid_search.GridSearchCV(svr, parameters)
clf.fit(iris.data, iris.target)
print(clf.best_params_)
# -> {'C': 1, 'kernel': linear}


"""
    code for the validation mini-project.

"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)
from sklearn import tree
from sklearn.metrics import accuracy_score

#### first POI Identifier (overfit) -- unvalidated, use all the data to train
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
pred = clf.predict(features)
acc = accuracy_score(pred, labels)
print(acc)
# -> 0.989

#### deploying a training/testing regime
from sklearn import cross_validation
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
    features, labels, test_size=0.3, random_state=42)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(pred, labels_test)
print(acc)
# -> 0.724


