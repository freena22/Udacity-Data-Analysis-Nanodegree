### regression

# Official example
from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
#LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
print(reg.coef_)
# -> array([ 0.5,  0.5])

# quiz: age v.s. net_worths
def studentReg(ages_train, net_worths_train):
    ### import the sklearn regression module, create, and train your regression
    ### name your regression reg
    ### your code goes here!
    from sklearn import linear_model
    reg = linear_model.LinearRegression()
    reg.fit(ages_train, net_worths_train)
    return reg


print("Katie's net worth prediction: ", reg.predict([27])) # -> 160.43
print("slope:", reg.coef_) # -> 6.47
print("intercept:", reg.intercept_) # -> -14.35
print("r-squared score:", reg.score(ages_test, net_worths_test))
# -> 0.81
print("r-squared score:", reg.score(ages_train, net_worths_train))
# -> 0.87

# Visualizing the regression
plt.scatter(ages, net_worths)
plt.plot(ages, reg.predict(ages), color="blue", linewidth=3)
plt.xlabel("ages")
plt.ylabel("net worths")
plt.show()