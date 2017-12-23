import cv2

from IPython import embed
import os
import glob

file_list = ['/home/dhiraj/7522Sep28',
#'/home/dhiraj/6921Sep21', 
#'/home/dhiraj/7686Sep29',
#'/home/dhiraj/6866Sep21',
#'/home/dhiraj/7303Sep28',
#'home/dhiraj/7549Sep28',
#'/home/dhiraj/7742Sep29',
#'/home/dhiraj/7830Sep30',
#'/home/dhiraj/7941Sep30',
#'/home/dhiraj/8000Sep30',
#'/home/dhiraj/8118Sep30',
#'/home/dhiraj/9088Oct06',
#
           #'/run/user/1001/gvfs/smb-share:server=192.168.2.6,share=lekha/7300Sep28',
#'/run/user/1001/gvfs/smb-share:server=192.168.2.6,share=lekha/4313Aug02',
#'/run/user/1001/gvfs/smb-share:server=192.168.2.6,share=lekha/4064Jul31',
#'/run/user/1001/gvfs/smb-share:server=192.168.2.6,share=lekha/3936Jul30',
#'/run/user/1001/gvfs/smb-share:server=192.168.2.6,share=lekha/3644Jul25',
#'/run/user/1001/gvfs/smb-share:server=192.168.2.6,share=lekha/1854Jun15',
#'/run/user/1001/gvfs/smb-share:server=192.168.2.6,share=lekha/3992Jul31',
#'/run/user/1001/gvfs/smb-share:server=192.168.2.6,share=lekha/5522Aug18',
#'/run/user/1001/gvfs/smb-share:server=192.168.2.6,share=lekha/5406Aug18',
]

count = 0
for i in file_list:
             file_names = glob.glob(i+"/HD "+os.path.basename(i)+"/kinect_rgb/*")
             file_names.sort()
             print "found"
             for j in file_names:
                img = cv2.imread(j)
                img = img[200:600,100:500]
                cv2.imshow("cropped",img)
#                print os.path.basename(j)
#                if count %3 == 0:
#                    embed()
                cv2.waitKey(50)
                count = count + 1
#             embed()       


