import glob
import os
import matplotlib.pyplot as plt
from PIL import Image
import time
from IPython import embed 
import subprocess

list_of_files = os.listdir(os.getcwd())
#embed()

label = 18 
start = raw_input("enter start number: ")
end = raw_input("enter stop number: ")
diff = int(end) - int(start)

embed()
print "LABEL is ", label
for i in range(diff+1):
#while(raw_input("LAbel More?") != 'n'):

    file_num = int(start)+i
    #embed()
    files = glob.glob(os.getcwd()+"/"+str(file_num)+"*")
    print "Files name is ",files
    #embed()
    if files and os.path.exists(files[0]+"/HD "+os.path.basename(files[0])):
        print "Exists folder",files
        if os.path.isfile(files[0]+"/label.txt"):
                print "label available for file, ",files
        else:
                print "-----------------------------------------------------------"
                print "Checking the file,  ",files[0]
                with open (files[0]+"/"+"label.txt", "w") as f:
                    f.write(str(label))
                    print "written"
    elif not files:
        print "FILES LIST IS EMPTY - ",file_num
    else:
        print files, "doesn't exists ",i

print "STOPPED LABELLING"            

