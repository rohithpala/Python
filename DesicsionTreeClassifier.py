import sklearn
from sklearn import tree
features = [[2,100],[6,25],[1,300],[1,1000],[4,100],[10,100]]
label = [1,2,1,1,2,2]
clf = tree.DecisionTreeClassifier()
clf.fit(features, label)
print(clf.predict([[2,120]]))
