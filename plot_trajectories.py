import os
import glob
import shutil
import numpy as np
import matplotlib.pyplot as plt

from natsort import natsorted,ns
from IPython import embed
from shutil import copyfile

#--------------------COPY FILES INTO A NEW SUBSET. ONLY KINECT RGB O HD RD AND JOINTS - 60 FILES
dest_path = '/home/dhiraj/Desktop/Sub_DataSet/'
label_dirs = []
for subdir, dirs, files in os.walk(dest_path): 
    for dir_name in dirs:   
        full_file_path = dest_path+dir_name+'/label.txt'
        if os.path.exists(full_file_path): 
            with open(full_file_path) as f:
                num = int(f.read())
                if num == 14:
                   label_dirs.append(full_file_path)

print "Label_dirs"
embed()


def ProcessFiles(files):
    files = [f.strip() for f in files]
    files.pop(0)
    del files[3:]
    files = map(float, files)  # str ->float
    return files

def Plot(a,name):
    fig, ax = plt.subplots(nrows=2, ncols=2)
    plt.subplot(2,2,1)
    plt.title(name) 
#    a_min = np.min(a, axis=tuple(range(a.ndim-1)), keepdims=1)
#    a_max = np.max(a, axis=tuple(range(a.ndim-1)), keepdims=1)
#    # Normalize with those min, max values leveraging broadcasting
#    a = (a - a_min)/ (a_max - a_min)
    plt.plot(np.arange(61),a[:,0],'r')
    axes = plt.gca()
    axes.set_ylim([-1,1])
    axes.set_xlim([0,61])
    plt.ylabel("x")
    plt.subplot(2,2,2)
    plt.plot(np.arange(61),a[:,1],'b')
    axes = plt.gca()
    axes.set_ylim([-1,1])
    axes.set_xlim([0,61])
    plt.ylabel("y")
    plt.subplot(2,2,3)
    plt.plot(np.arange(61),a[:,2],'g')
    plt.ylabel("z")
    axes = plt.gca()
    axes.set_ylim([-1,1])
    axes.set_xlim([0,61])
    return plt

sub_dirs = label_dirs[0:5]

for d in sub_dirs:
     dirs = os.path.dirname(d)
     files_left = glob.glob(dirs+"/RD "+os.path.basename(dirs)+"/fk/left/*.txt")  
     files_left = natsorted(files_left, key=lambda y: y.lower())
     files_right = glob.glob(dirs+"/RD "+os.path.basename(dirs)+"/fk/right/*.txt")
     files_right = natsorted(files_right, key=lambda y: y.lower())
     pose_left = []
     pose_right = []

     for i in range(len(files_left)):
         with open(files_left[i]) as left:
            pose_left.append(np.asarray(ProcessFiles(left)))
         with open(files_right[i]) as right:
             pose_right.append(np.asarray(ProcessFiles(right)))
             
     left_array = np.asarray(pose_left)
     plt_left = Plot(left_array,"left_arm") 
     right_array = np.asarray(pose_right)
     plt_right = Plot(right_array,"right_arm")



