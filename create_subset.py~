import os
import glob
import shutil
import numpy as np

from natsort import natsorted,ns
from IPython import embed
from shutil import copyfile
#--------------------COPY FILES INTO A NEW SUBSET. ONLY KINECT RGB O HD RD AND JOINTS - 60 FILES

#dest_path = '/home/dhiraj/Desktop/Sub_DataSet'
dest_path = '/mnt/backUp/DataSubset'        #To be copied here
empty_files = []

def DeleteFiles(path,ext):
    files = glob.glob(dest_path+"/"+path)
    new_files = natsorted(files, key=lambda y: y.lower())
    numFiles = len(new_files)
    print "LENGTH--->", numFiles
    if numFiles == 0:
        empty_files.append(path) 
        print "EMPTY FILES"
        empty_files
        return  
    index = np.asarray(np.linspace(0, numFiles, 62)).astype(int)

    print " FOr PAth", path
    count = 0
    flag =0 
    retain_list = []
    for i in index :
        if count == 61:
            break 
        curr_file = new_files[i] 
        new_name = dest_path+"/"+os.path.dirname(path)+"/"+str(count)+ext
 
        if os.path.exists(new_name):
            flag = 1
            break
            return
        
        copyfile(curr_file,new_name)
        count = count+1
    print "Not returning"
    if flag == 0:
        for files in new_files:
            print "deleting", files
            os.remove(files)
         
def RemoveFiles(dest_path):
    os.chdir(dest_path)
    num = 1
    for subdir,dirs,files in os.walk(dest_path):
        for dir_name in dirs:
          if os.path.exists(dir_name+"/HD "+dir_name+"/kinect_rgb"): 
            #embed()  
            #Delete Depth images, Sk_left_depth, Sk_right_depth, baxeter_right joints
            hd_images = dir_name+"/HD "+dir_name+"/kinect_rgb/*.png"
            rd_images = dir_name+"/RD "+dir_name+"/kinect_rgb/*.png"
            joints = dir_name+"/RD "+dir_name+"/baxter_right_joints/*.txt"
            
            DeleteFiles(hd_images,".png")
            DeleteFiles(rd_images,".png")
            print "-------------------------------->",num
            num = num+1 
            DeleteFiles(joints,".txt")

            shutil.rmtree(dir_name+"/HD "+dir_name+"/kinect_depth",ignore_errors=True)    
            print "REMOVED ", dir_name,"KINECT DEPTH"
            shutil.rmtree(dir_name+"/RD "+dir_name+"/kinect_depth",ignore_errors=True)
            shutil.rmtree(dir_name+"/RD "+dir_name+"/baxter_left_gripper",ignore_errors=True)
            shutil.rmtree(dir_name+"/RD "+dir_name+"/baxter_right_gripper",ignore_errors=True)
            print "REMOVED",dir_name,"grippers"
       
            shutil.rmtree(dir_name+"/RD "+dir_name+"/joint_angles",ignore_errors=True)
            shutil.rmtree(dir_name+"/RD "+dir_name+"/sk_left_depth",ignore_errors=True)
            print "REMOVED", dir_name,"JOINT ANGLES AND SK _LEFT DEPTH"
          
            shutil.rmtree(dir_name+"/RD "+dir_name+"/sk_left_rgb",ignore_errors=True)
            shutil.rmtree(dir_name+"/RD "+dir_name+"/sk_right_depth",ignore_errors=True)
            shutil.rmtree(dir_name+"/RD "+dir_name+"/sk_right_rgb",ignore_errors=True)

    print "END OF LOOP"
    embed()

#-------------------------------------------IMPORTANT: UNCOMMENT LINE 87-99 AND COMMENT LINE 100, TO INITATE COPYING----------------------------------------
#-------------------------------------------AFTER COPYING, COMMENT LINE 87-99 AND UNCOMMENT LINE 100 TO DELETE UNNECESAARY FILES----------------------------
#-----------------------------------------------------OR BETTER!!!!! PLEASE REWRITE THIS CODE!!!!!!!!!!-----------------------------------------------------
   
#lists = ['Sep','Oct']   #Copies only data collected during these months
#for subdir, dirs, files in os.walk('/run/user/1001/gvfs/smb-share:server=192.168.2.6,share=lekha/'):
#   #for subdir, dirs, files in os.walk('/home/dhiraj/Desktop/Sub_DataSet/'):
#   for dir_name in dirs:   
#        for word in lists:
#            if word in dir_name:
#                if not (dir_name.startswith('HD') or dir_name.startswith('RD') or dir_name.startswith('hd')): #to avoid copying noise files
#                    if not os.path.isdir(dest_path+"/"+dir_name):
#                        print dest_path+"/"+dir_name, " being copied to"
#                        shutil.copytree('/run/user/1001/gvfs/smb-share:server=192.168.2.6,share=lekha/'+dir_name,dest_path+"/"+dir_name,True) 
#                        #shutil.copytree('/home/dhiraj/Desktop/Sub_DataSet/'+dir_name,dest_path+"/"+dir_name,True) 
#                    else:
#                        print dest_path+"/"+dir_name, "already found"
RemoveFiles(dest_path)
