import glob
import os
import matplotlib.pyplot as plt 
from PIL import Image
import time
from IPython import embed 
import subprocess
from collections import Counter

list_of_files = os.listdir(os.getcwd())
#embed()
unique_labels = []
count  = 0 

#COunts total number if labels in the sampled dataset and it's frequency

for files in list_of_files:
        if not (files.startswith('HD') or files.startswith('RD') or files.startswith('hd')):
	  if os.path.exists(files+"/HD "+files+"/kinect_rgb"):
                embed()
 		full_path  = files+'/label.txt' 
		if os.path.exists(full_path):
			count = count+1
			print "label available for", files,"------>",count
			with open(full_path) as f:

			     print full_path #,",",a, type(a)
			     a = int(f.readline())
   			     #print full_path,",",a, type(a)
			     if (a == 114 or a == 220 or a == 99):
				print "CHECK POINT"
				embed()
			     else:		
			     	unique_labels.append(a)	
	     
Counter(unique_labels).keys()
Counter(unique_labels).values()
embed()	
