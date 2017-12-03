# Machine_Learning
For Machine Learning starters
# how to implement a decision tree model using python
from sklearn import tree
# Planet or a star
#features are size and light
x=[[200, 1], [100, 0],[120,0],[180,1],[190,1], [90,0]]
y=['Star', 'Planet', 'Planet','Star','Star', 'Planet']
a=tree.DecisionTreeClassifier()
a=a.fit(x,y)
prediction=a.predict([[150,1]])
print (prediction)
