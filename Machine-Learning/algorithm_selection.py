

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]

#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()

################################################################################

### Decision tree 
from sklearn import tree
from sklearn.metrics import accuracy_score
clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf = clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(pred, labels_test)
print(acc)
# -> 0.912

# SVM
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
clf = SVC(kernel='rbf',C=10000.)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(pred,labels_test)
print(acc)
# -> 0.932

# AdaBoost Classifier 
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier(n_estimators=100)
scores = cross_val_score(clf, features_train, labels_train)
print(scores.mean())
# -> 0.9427

from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(max_depth=None, min_samples_split=2,random_state=0)
scores = cross_val_score(clf, features_train, labels_train)
print("DecisionTreeClassifier: ")
print(scores.mean())
# -> DecisionTreeClassifier: 0.945370133922

clf = RandomForestClassifier(n_estimators=10, max_depth=None,min_samples_split=2, random_state=0)
scores = cross_val_score(clf, features_train, labels_train)
print('RandomForestClassifier: ')
print(scores.mean())
# -> RandomForestClassifier: 0.952031488504

clf = ExtraTreesClassifier(n_estimators=10, max_depth=None,min_samples_split=2, random_state=0)
scores = cross_val_score(clf, features_train, labels_train)
print('ExtraTreesClassifier: ')
print(scores.mean())
# -> ExtraTreesClassifier: 0.94136477917

try:
	prettyPicture(clf, features_test, labels_test)
except NameError:
	pass
