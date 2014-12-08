#!/usr/bin/python

import decoder
import csv

file=open('classifiedsegs.csv','r')
lines=file.readlines()
file.close()
file=open('finalfeatures.csv', 'ab')
wr=csv.writer(file,dialect='excel')
for line in lines:
	ents=line.split(',')
	dist=decoder.distance_on_unit_sphere(float(ents[6]),float(ents[7]),float(ents[8]),float(ents[9]))
	curviness=dist*6378100/float(ents[11])
	#print curviness
	newline=[ents[0], curviness, ents[3], ents[5], ents[10], ents[11]]
	wr.writerow(newline)
file.close()
