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