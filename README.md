A collection of files for RoadClass.
James Bialas
SU5050, 12/8/2014

RoadClass downloads road segments from Strava, and given training samples, classifies road segments based on any number of critera.

README- This file.

decoder.py- A collection of functions found on the internet for decoding google polylines and measuring distance on a sphere between two points.`

classviz.py- Based on a trainiung sample, will classify another set of data and visualize both training sample and classified data in Google Earth.

displaysegs.py- Displays unclassified segments obtained from Strava in Google Earth.

dt.py- Trains a decision tree classifier with a training sample, classifies a validation sample and prints some results.

featurizer.py- Develop some new features from segments and distill raw data down into what we feed the classifier.

slider.py- Pulls in data from Strava. Given a bounding box and a grid size, will side across bounding box at increment intervals, then shrink the gride size by the increment and repeat. 


