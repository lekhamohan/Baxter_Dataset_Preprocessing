import glob
import os
import matplotlib.pyplot as plt 
from PIL import Image
import time
from IPython import embed 
import subprocess
from collections import Counter


#COunts total number if labels in the sampled dataset and it's frequency
#args1 --> list_of_files: directory path of demo trajectories

def CountLabel(list_of_files, unique_labels,count):
    '''
    list_of_files: direcotries it is going to check for labels
    unique_labels: dictionary that holds the labels(keys) and it's frequency(values)
    count: num of files; this line ios commentede as of now
    '''
    for files in list_of_files:
        if not (files.startswith('HD') or files.startswith('RD') or files.startswith('hd')):#Check to avoid incomplete or broken files
 		full_path  = "/home/dhiraj/"+files+'/label.txt' 
		if os.path.exists(full_path): 
			count = count+1
			#print "label available for", files,"------>",count
			with open(full_path) as f: # Read label
			     a = int(f.readline()) 
			     if (a == 114): #Check to find labelling errors; weird labels will be shown in the output; 
				print "CHECK POINT"
				embed()
			     else:		
			     	unique_labels.append(a)	
	     
    print "\n{Keys(labels): Values(number of such labels)}", dict(zip(Counter(unique_labels).keys(),Counter(unique_labels).values())), "\n"
    

if __name__ == "__main__":
     list_of_files = os.listdir("/home/dhiraj")  #os.listdir(os.getcwd())
     unique_labels = []
     count  = 0
     CountLabel(list_of_files, unique_labels,count)

