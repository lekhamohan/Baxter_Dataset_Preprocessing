import os
import glob
import ast

from IPython import embed

#path = '/mnt/seagate/dataset/RD 152Apr22/'
path = os.getcwd()+'/'

print "inside the file"

for subdir, dirs, files in os.walk(path):

    #embed()		
    for dir_name in dirs:
       #print "for dir_name",dir_name    
       #print path
     
       if not (dir_name.startswith('HD') or dir_name.startswith('RD') or dir_name.startswith('hd')):
      
	     joint_files_path = path+dir_name+'/RD '+ dir_name+'/baxter_right_joints'
	   

	     if os.path.exists(joint_files_path):
		print "--------------------------------------------"
		print "checking for directory", dir_name
		files = glob.glob(joint_files_path+'/*.txt')
		directory = path+dir_name+ '/RD '+ dir_name+ '/joint_angles/'

		if not os.path.exists(directory):
		    os.makedirs(directory)
		    print "made joint_angle folder for", dir_name

		    #embed()
		    for name in files:
		      with open(name) as f:
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
			 #from IPython import embed; embed()
print "FINISHED"
