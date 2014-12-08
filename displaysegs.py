#!/usr/bin/python

import decoder
import simplekml
kml=simplekml.Kml()
resultant=[]

file=open('usegs.csv','r')
lines=file.readlines()
for line in lines:
	ents=line.split(',')
	segmentname=ents[1].decode('utf-8')
	seg=kml.newdocument(name=segmentname)
	resultant=decoder.decode_line(ents[20])
	lin=seg.newlinestring(coords=resultant)
	print "seg is:"
	print ents[1]
	print resultant
	kml.save("segments.kml")
