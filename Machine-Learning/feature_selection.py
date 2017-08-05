### Feature selection

# Balance the bias and variance 

# Lasso regression
import sklearn.leanr_model.Lasso
features, labels = GetMyData()
regression = Lasso()
regression.fit(features, labels)
# predict a label for a new point [2,4]
regression.predict([2,4])
print(regression.coef_)
# -> [0.7, 0.0] means only one feature really maters
# the first feature is 0.7 and second is 0