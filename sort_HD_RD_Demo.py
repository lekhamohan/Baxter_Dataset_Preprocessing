import re
import os
import glob
import shutil
from IPython import embed

#This script sorts the HD folder(HD 12000Jun02)  and its corresponding RD folder(RD 12000Jun02)  into single directory(12000 Jun02); Since Baxter's data by default gets stores in the home direcotry, there are no parameters to pass.

# return PathNames
def pathNames():
	basePath = '/home/dhiraj/'
	allFiles = os.listdir(basePath)
	fileNames = glob.glob(basePath+"HD*") 
	return basePath, allFiles, fileNames

def main():
        #Gets relevant path names and files name to sort
	basePath, allFiles, fileNames = pathNames()
	for name in fileNames:  
		# Extracts HD directory name
		baseFileName = os.path.basename(basePath + name)
		# Extracts demo trajectory number
		regex = re.compile(r'\d+')  
		numList = regex.findall(baseFileName)
		if len(numList) == 2:  #Checks for broken Files
			fileRD =  "RD "+baseFileName.split()[1]	
			#Create new demo directory(12000 Jun02)
			if fileRD in allFiles:
				dirName = os.path.dirname(name)+"/"
				dirName = dirName+baseFileName.split()[1]
				if not os.path.exists(dirName):
					os.makedirs(dirName)
					print "Made directory,", dirName    
					shutil.move(name, dirName)
					shutil.move(basePath+fileRD, dirName)		
				else:
					print "ALREADY EXISTS OR MADE__________________", dirName			
if __name__ == "__main__":
	main()
