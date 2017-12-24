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

#This script dumps the Baxter Demo's images, it's corresponding labels and joints angles into a HDF5 file
#args1: src_path --> Data folder from which you want to read images, labels and angles
#args 2: hdf5_path -->  destination for the .hdf5 file
#args3: label_list --> which lables(1-21) would you like to dump into HDF5

def DumpHDF5(zipped_files):
        '''Start dumping corresopnding files into .hdf5'''
	I,L,J = zip(*zipped_files) 
	train_img_shape = (len(glob.glob(I[0])),224,224,3)
	train_joint_shape = (len(J),JOINT_LIN_SPACE,17) # 17 is total no. of joint angles in Baxter		

	#Creating HDF5 file structure
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
        print "Done with Images"

	#Dump Joints as 500*17 matrix; 500 is the no. of joint_angles data sampled and 17 is the total no.of joint positions present in Baxter
        for j in range(2): #len(J)):
		angleVector = np.array([], dtype=np.float64).reshape(0,17)
		print J[j]
		joint_ang_files = glob.glob(J[j])
		joint_ang_files.sort()
		numFiles = len(joint_ang_files)
		jointArr = np.asarray(np.linspace(0, numFiles-1, 500)).astype(int)
 		for num in range(len(jointArr)):
			joint_vec = loadtxt(joint_ang_files[jointArr[num]], comments="#",                                                       delimiter=",", unpack= False)
			
			angleVector = np.vstack([angleVector, joint_vec])
                
                hdf5_file["train_joints"][j, ...] = angleVector
        print "Done with Joints"
	hdf5_file.close()
	print "closed HDF5"


#Check if Retrieved label is in current list
def CheckLabel(full_label_path,label_list):
        '''
        This function checks if whether the current data(trajectory) belongs to required label_list
        args full_label_path: contains the label of the data folder that is being read
        label_list: containts the list of required labels
        '''
	with open(full_label_path) as f:
        	label_num = np.genfromtxt(full_label_path,dtype='int64') 
		if label_num in label_list:
			return True
		else:
			return False                             


def ProcessHDF5(src_path,list_of_files,label_list):
    '''
    This function checks for the data files belonging to labels mentioned in label_list,                                  extract images and joint angles of those labels and dumps them into HDF5 files
    The arguments here carry the same meaning as mentioned in the top of this script
    '''
    img_files = []
    label_files = []
    joint_files = []
    for files in list_of_files: #Look into specified data folder
        if not (files.startswith('HD') or files.startswith('RD') or files.startswith('hd')):#Avoid broken files   
                full_label_path = src_path+files+"/label.txt"      
		full_img_path = src_path+files+"/HD "+os.path.basename(files)+"/kinect_rgb/*.png"             
		full_joint_path = src_path+files+ "/RD "+os.path.basename(files)+"/joint_angles/*.txt"

		if os.path.exists(full_label_path): #Check for labels provided in the label_list
			check_label = CheckLabel(full_label_path,label_list)
			if (check_label): #if label is found, add the path of image and joint angles
				img_files.append(full_img_path)
				label_files.append(full_label_path)
				joint_files.append(full_joint_path)
    #Shuffle data
    zipped_files = zip(img_files , label_files, joint_files) # zip these files						
    shuffle(zipped_files)
    DumpHDF5(zipped_files) #Dump into .hdf5 files



if __name__ == "__main__":
     
    src_path = '/home/dhiraj/test/'
    list_of_files = os.listdir(src_path) 
    hdf5_path = '/home/dhiraj/processed_data.hdf5'
    label_list = [2,3,4,15,6,7,8,9,13,14,18,20,21]
    JOINT_LIN_SPACE = 500 #No. of samples from joint_angles folder
    ProcessHDF5(src_path,list_of_files,label_list)


