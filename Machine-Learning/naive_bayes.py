
### sklearn.naive_bayes.GaussianNB

# official examples

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

