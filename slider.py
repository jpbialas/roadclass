#!/usr/bin/python

from stravalib.client import Client
import json
from stravalib import unithelper
import csv
import logging
import time
import simplekml

client = Client(access_token='insert_client_access_token_here')
#logging.basicConfig()
increment=0.05
latsize=0.2
lonsize=0.2
lat=46.23
lon=-87.49
kml=simplekml.Kml()
count=0

while latsize>0:
	docname="%s"%(latsize)
	print docname
	segs=kml.newdocument(name=docname)
	while lat<=46.44:
		while lon<=-87.18:
 
			bounds=[lat,lon,lat+latsize,lon+lonsize]
			print bounds
			print latsize
			print lonsize
			print count
			polname="%s" % (bounds)
			pol=segs.newpolygon(name=polname, \
			outerboundaryis=[ \
			(lon,lat),(lon,(lat+latsize)),\
			((lon+lonsize), (lat+latsize)), ((lon+lonsize),lat)])
			pol.style.polystyle.color=simplekml.Color.green
			pol.style.polystyle.fill=0
			pol.style.polystyle.outline=1

			explores=client.explore_segments(bounds)
			time.sleep(3)
			count+=1
			if len(explores)==10:
				pol.style.polystyle.color=simplekml.Color.red
	                        pol.style.polystyle.fill=1


			file=open('segments.slider.01.csv', 'ab')
			wr=csv.writer(file,dialect='excel')

			for s in explores:
				segmentname=s.name.encode('utf-8')
				results=[s.id, segmentname, s.climb_category, s.climb_category_desc, s.avg_grade, \
				s.start_latlng.lat, s.start_latlng.lon, s.end_latlng.lat, s.end_latlng.lon, \
				float(unithelper.meters(s.elev_difference)), float(unithelper.meters(s.distance))\
				,s.segment.state,s.segment.city, s.segment.starred, s.segment.created_at, \
				s.segment.updated_at, s.segment.effort_count, s.segment.athlete_count, \
				s.segment.hazardous, s.segment.star_count,\
				s.points]
				wr.writerow(results)

			file.close()
			lon +=increment
		lat+=increment
		lon=-87.49
	lat=46.23
	latsize-=increment
	lonsize-=increment

kml.save("polys.kml")


	
