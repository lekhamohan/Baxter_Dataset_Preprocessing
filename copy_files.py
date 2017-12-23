import shutil
from shutil import copyfile
import glob
import os
from IPython import embed
import subprocess

path = os.getcwd()
#pathHD = glob.glob(path+"/HD*")
pathHD = glob.glob(path+"/RD*")

destPath = "/mnt/backUp6/Dataset/"
 
fileNum  = 0
exists = 0
for name in pathHD:
	#cmd = ['cp -r' ,name, destPath]
	baseName =os.path.basename(name) 
	#Checking if direcotry exists in dest path
        if not (os.path.exists( os.path.join(destPath,baseName))):
		#embed()
		print "Moving ",name,"--->",destPath
		print fileNum
		#subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr = subprocess.PIPE)

		shutil.copytree(name,destPath+baseName) #recursive copying to destination dir
                fileNum = fileNum + 1

		
  	else:
		print name,"  exists----->", exists
		exists = exists+1

        if fileNum == 11:
        	break




