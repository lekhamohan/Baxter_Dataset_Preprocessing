import natsort
import os
import glob
import cv2
import shutil
from IPython import embed

#This Script copies files from one destination to another, compressing all the images into video.avi. 
# args1 -->src_path: Original file location path
#args2 --> dest_path: Final copy destination path


def VideoConverter(src_path, dest_path):
    ''' 
    This function converts all the images to a .avi video at 10fps
    src_path: path of image directory
    dest_path: path to store the converted video
    '''
    img_list = glob.glob(src_path+"/*.png")
    img_list = natsort.natsorted(img_list)
    h,w,l = cv2.imread(img_list[0]).shape
    video = cv2.VideoWriter(dest_path+"video.avi",cv2.cv.CV_FOURCC(*'XVID'),10,(w,h))
    for i in range(len(img_list)):
       video.write(cv2.imread(img_list[i])) 
    video.release()



def create_subset(src_path, dest_path):
    '''
    This function copies the data from one location to another. 
    Whenever it encounters an image filder, it converts it into a video 
    src_path: directory path to be copied
    dest_path: Copied files are stored here
    '''    
    dirs =  os.listdir(src_path)
    for dir_name in dirs:
        for subdir,dirs,files in os.walk(src_path+"/"+dir_name):
            if os.path.basename(subdir).startswith('HD') or os.path.basename(subdir).startswith('RD'):
             subs = os.listdir(subdir)
             for s in subs:
                for sub,d,f in os.walk(subdir+"/"+s):
                    if sub.endswith('depth') or sub.endswith('rgb'):
                        print "Doing ", sub
                        video_path = dest_path+"/"+dir_name+"/"+os.path.basename(subdir)+"/"+os.path.basename(sub)+"/"
                        if not os.path.exists(video_path):
                            os.makedirs(video_path)
                        VideoConverter(sub,video_path)
                    elif sub.endswith('s') or sub.endswith('r'):
                        shutil.copytree(sub, dest_path+"/"+dir_name+"/"+os.path.basename(subdir)+"/"+os.path.basename(sub),True)


if __name__ == "__main__":
    src_path ="/home/dhiraj/Desktop/TEST" 
    dest_path = "/home/dhiraj/Desktop/Sample"
    create_subset(src_path, dest_path)

