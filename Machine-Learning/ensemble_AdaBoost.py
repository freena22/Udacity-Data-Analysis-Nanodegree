
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
from sklearn.ensemble import AdaBoostClassifier

iris = load_iris()
clf = AdaBoostClassifier(n_estimators=100)
scores = cross_val_score(clf, iris.data, iris.target)
print(scores.mean())
# -> 0.96


## mini-project from course
from class_vis import prettyPicture
features_train, labels_train, features_test, labels_test = makeTerrainData()

clf = AdaBoostClassifier(n_estimators=100)
scores = cross_val_score(clf, features_train, labels_train)
print(scores.mean())
# -> 0.9427