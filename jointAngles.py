import os
import glob
import ast

from IPython import embed

#This script reads the stored raw joint_angles from Baxter Dempo and converts it to a human readble dictionary form 
#This script has to be run as soon as we get the data from Baxter, right after sort_me_HD_RD_Demo.py

path = os.getcwd()+'/'  #Change this path with respect to the script's location. By Default, Baxter Data is stored in /home/dhiraj

for subdir, dirs, files in os.walk(path):
    for dir_name in dirs:
       if not (dir_name.startswith('HD') or dir_name.startswith('RD') or dir_name.startswith('hd')): #Check for broken files     
	     joint_files_path = path+dir_name+'/RD '+ dir_name+'/baxter_right_joints'
	     if os.path.exists(joint_files_path): #Checking if joint_angles is already present
                    print "--------------------------------------------"
                    print "checking for directory", dir_name
                    files = glob.glob(joint_files_path+'/*.txt')
                    directory = path+dir_name+ '/RD '+ dir_name+ '/joint_angles/'
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                        print "made joint_angle folder for", dir_name
                        for name in files:
                              with open(name) as f:  #Converting raw joint angles into dictionary format
                                     content = f.read()
                                     # Str ---> Dict
                                     dictAngles = ast.literal_eval(content)
                                     #Extracting FileName 
                                     newFileName = os.path.basename(name)
                                     fileObj = open(directory+newFileName,'w')
                                     for k,v in dictAngles.items():
                                        fileObj.write('%s\n'%v)
                                     fileObj.close() 
                    else:
                        print "joint_angle folder already present - ", directory         
        

