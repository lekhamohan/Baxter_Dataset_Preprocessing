import re
import os
import glob
import shutil

from IPython import embed

# return PathNames
def pathNames():
	basePath = '/home/dhiraj/'
	allFiles = os.listdir(basePath)
	fileNames = glob.glob(basePath+"HD*") 
	
	print "check PATHNAMEs"
	#embed()

	return basePath, allFiles, fileNames


def main():
	basePath, allFiles, fileNames = pathNames()
	#embed()
	for name in fileNames:  
		# Extracts HD directory name
		baseFileName = os.path.basename(basePath + name)
		# Extracts demo trajectory number
		regex = re.compile(r'\d+')  
		numList = regex.findall(baseFileName)

		print "RD files CHECK"
		#embed()

		if len(numList) == 2:  #Check for broken Files
			fileRD =  "RD "+baseFileName.split()[1]	

			#print "CHECK 3"
			#embed()

			#Create new demo directory
			if fileRD in allFiles:
				dirName = os.path.dirname(name)+"/"
				dirName = dirName+baseFileName.split()[1]

				#embed()
				if not os.path.exists(dirName):
					os.makedirs(dirName)
					print "Made directory,", dirName
					#Move RD_num and HD_num under directory num    
					shutil.move(name, dirName)
					
					#embed()

					shutil.move(basePath+fileRD, dirName)		
				else:
					print "ALREADY EXISTS OR MADE__________________", dirName			
if __name__ == "__main__":
	main()
