import os
import glob
import ast
import shutil

from IPython import embed

#This script removes unwanted files which started getting stored from Baxter after Baxter's software update. 
path = os.getcwd()+'/'
toBeRemoved = ' ' 
for subdir, dirs, files in os.walk(path):
    for dir_name in dirs:
       if not (dir_name.startswith('HD') or dir_name.startswith('RD') or dir_name.startswith('hd')):   
	     joint_files_path = path+dir_name+'/RD '+ dir_name+'/baxter_right_joints'
	     if os.path.exists(joint_files_path):
		print "--------------------------------------------"
		print "checking for directory", dir_name
		files = glob.glob(joint_files_path+'/*.txt')
	        for name in files:
		      with open(name) as f:
			 if not toBeRemoved == ' ':
				print "Going to delete", toBeRemoved
				os.remove(toBeRemoved)
				toBeRemoved = ' '	
			 content = f.read()
			 # Str ---> Dict
			 dictAngles = ast.literal_eval(content)
			 if len(dictAngles) != 17: #This Check catches the unwanted data, stores them temporarily and deletes them
				toBeRemoved = name	

