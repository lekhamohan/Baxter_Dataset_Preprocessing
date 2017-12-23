import glob
import os
import matplotlib.pyplot as plt 
from PIL import Image
import time
import h5py
import cv2
import numpy as np

from IPython import embed 
from collections import Counter
from random import shuffle
from numpy import loadtxt


list_of_files = os.listdir(os.getcwd())

file_list = ['/home/dhiraj/7355Sep28']

img_files = []
label_files = []
joint_files = []
hdf5_path = '/home/dhiraj/Desktop/rgb.hdf5'
#label_list = [1,2,7,8,9,14,21]		#Sampled labels
label_list = [2,3,4,5,6,7,8,9,13,14,17,20,21]
JOINT_LIN_SPACE = 500


def DumpHDF5(zipped_files):
	#hdf5_file.create_dataset("train_img",)

	I,L,J = zip(*zipped_files) 

	train_img_shape = (len(glob.glob(I[0])),224,224,3)
	train_joint_shape = (len(J),500,17)		

	#Dumping into hdf5 file
	hdf5_file = h5py.File(hdf5_path, mode = 'w')
	hdf5_file.create_dataset("train_img",train_img_shape, np.int8)
	hdf5_file.create_dataset("train_labels",(len(L),), np.int8)
	hdf5_file.create_dataset("train_joints",train_joint_shape, np.float64)
        hdf5_file.create_dataset("file_names",(len(L),),dtype = "S10")
	#Dump Labels
	train_labels = []
        train_names = []

	for files in list(L):
		print files
		with open(files, 'r') as f:
            	            train_labels.append(int(f.readline()))
                            train_names.append(files)       

	hdf5_file["train_labels"][...] = train_labels
	hdf5_file["file_names"][...] = train_names

	print "Done with labels"

        #Dump Images
        print "GOING TO DUMP IMAGES"
        for i in range(len(I)):
		img = glob.glob(I[i])
		img.sort()
                for j in range(len(img)):
		  img_j = cv2.imread(img[j])
		  img_j = img_j[250:474, 200:424]
                  img_j = cv2.resize(img_j,(224,224))
		  cv2.imshow("cropped",img_j)
		  cv2.waitKey(20)
		  hdf5_file["train_img"][j, ...] = img_j
                embed() 
        print "Done with Images"

	#Dump Joints
        for j in range(2): #len(J)):
		angleVector = np.array([], dtype=np.float64).reshape(0,17)
		print "\n"
		print "****************************************************************"
		print "Check output for j = ", j
		print J[j]
		joint_ang_files = glob.glob(J[j])
		joint_ang_files.sort()
		numFiles = len(joint_ang_files)
		jointArr = np.asarray(np.linspace(0, numFiles-1, 500)).astype(int)
                #embed()
               
		for num in range(len(jointArr)):

			joint_vec = loadtxt(joint_ang_files[jointArr[num]], comments="#",                                                       delimiter=",", unpack= False)
			
			angleVector = np.vstack([angleVector, joint_vec])
                
                hdf5_file["train_joints"][j, ...] = angleVector
        print "Done with Joints"

	hdf5_file.close()
	print "closed HDF5"


#Check if Retrieved label is in current list
def CheckLabel(full_label_path):
	with open(full_label_path) as f:
		print "Text file read"
		#embed()
        	label_num = np.genfromtxt(full_label_path,dtype='int64') 
		if label_num in label_list:
			return True
		else:
			return False                             


#Counts label and frequency
for files in file_list:
        if not (files.startswith('HD') or files.startswith('RD') or files.startswith('hd')):   
		full_label_path = files+"/label.txt"      
		full_img_path = files+"/HD "+os.path.basename(files)+"/kinect_rgb/*.png"             
		full_joint_path = files+ "/RD "+os.path.basename(files)+"/joint_angles/*.txt"

		if os.path.exists(full_label_path):
			check_label = CheckLabel(full_label_path)
			if (check_label):
				img_files.append(full_img_path)
				label_files.append(full_label_path)
				joint_files.append(full_joint_path)

#Shuffle data
zipped_files = zip(img_files , label_files, joint_files)						
shuffle(zipped_files)
DumpHDF5(zipped_files)

embed()
