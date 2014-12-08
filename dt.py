#!/usr/bin/python

from sklearn import datasets
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import StringIO
from sklearn import tree
import pydot
dataset=[]
validation=[]
target=[]
vtarget=[]

file=open("training.csv", "r")
lines=file.readlines();
file.close()
for line in lines:
	ents=line.split(",")
	dataset.append([float(ents[1]),float(ents[2]),float(ents[3]),float(ents[4]),float(ents[5])])
	target.append(ents[0])
	
#dataset=datasets.load_iris()

print dataset
print target
model=DecisionTreeClassifier()
model.fit(dataset,target)
print(model)
dot_data=StringIO()
tree.export_graphviz(model, out_file=dot_data)
graph=pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("dt.pdf")
expected= target
predicted= model.predict(dataset)
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted)) 

file=open("validation.csv", "r")
lines=file.readlines();
file.close()
for line in lines:
        ents=line.split(",")
        validation.append([float(ents[1]),float(ents[2]),float(ents[3]),float(ents[4]),float(ents[5])])
	vtarget.append(ents[0])


expected=vtarget
predicted=model.predict(validation)
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))


