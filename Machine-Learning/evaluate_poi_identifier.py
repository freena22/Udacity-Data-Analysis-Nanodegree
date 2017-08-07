
# Evaluation Metrics

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
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

# Evaluation: precision / recall 
from sklearn.metrics import confusion_matrix
print(confusion_matrix(features_test,pred))
from sklearn.metrics import precision_score
print(precision_score(features_test, pred,average=None)) # -> 0

from sklearn.metrics import recall_score
print(recall_score(features_test, pred, average=None)) # -> 0




