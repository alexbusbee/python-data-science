from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

# [height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male']

clf1 = tree.DecisionTreeClassifier()
clf2 = GaussianNB()
clf3 = QuadraticDiscriminantAnalysis()

clf1 = clf1.fit(X, Y)
clf2 = clf2.fit(X, Y)
clf3 = clf3.fit(X, Y)

x_test = [[198,92,48],[184,84,44],[183,83,44],[166,47,36],[170,60,38],[172,64,39],[182,80,42],[180,80,43]]
y_test = ['male','male','male','female','female','female','male','male']

prediction1 = clf1.predict(x_test)
prediction2 = clf2.predict(x_test)
prediction3 = clf3.predict(x_test)

accuracy1 = accuracy_score(y_test, prediction1)
accuracy2 = accuracy_score(y_test, prediction2)
accuracy3 = accuracy_score(y_test, prediction3)

results = {'DecisionTreeClassifier': accuracy1, 'GaussianNB': accuracy2, 'QuadraticDiscriminantAnalysis': accuracy3}

maximum = max(results, key=results.get)
print('The winner is', maximum, 'with an accuracy score of', results[maximum])