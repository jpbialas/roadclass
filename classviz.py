#!/usr/bin/python

import decoder
from sklearn import datasets
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
import simplekml
kml=simplekml.Kml()
dataset=[]
validation=[]
target=[]
vtarget=[]
resultant=[]

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
expected= target
predicted= model.predict(dataset)
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted)) 

file=open("validation.csv", "r")
lines=file.readlines();
file.close()
for line in lines:
        ents=line.split(",")
	dist=decoder.distance_on_unit_sphere(float(ents[6]),float(ents[7]),float(ents[8]),float(ents[9]))
	curviness=dist*6378100/float(ents[11])
        categ=model.predict([[curviness,float(ents[3]),float(ents[5]),float(ents[10]),float(ents[11])]])
	segmentname=ents[2].decode('utf-8')
        seg=kml.newdocument(name=segmentname)
	
        resultant=decoder.decode_line(ents[21].rstrip())
        lin=seg.newlinestring(coords=resultant)
	print float(categ[0])
	if float(categ[0])==1:
		print "one"
		lin.style.linestyle.color= 'ff0000ff' 
	if float(categ[0])==2:
                print "two"
                lin.style.linestyle.color= 'ff008000'
	if float(categ[0])==3:
                print "three"
                lin.style.linestyle.color= 'ffff0000'

	
	lin.style.linestyle.width=10
	kml.save("segments.kml")

