import cv2
import PIL
import os
import time

path ="/home/pdc-p180069/StarGAN1/data/celeba/images"
#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(path):
    for file in files:
        #append the file name to the list
        filelist.append(os.path.join(root,file))
count=0
# print all the file names
for name in filelist:
    image = cv2.imread(name)
    count+=1
    # if (image.shape[2]== 1 ):
    #     print(name, " ::  ", count , " : ",type ( image.shape[2]))
    # if image.any() != None:
    #     if(len(image.shape)<2):
    #         print ('grayscale')
    #     elif len(image.shape)==3:
    #         print ('Colored')
    #     else:
    #         print("cannot find image")  
    print(name, " ::  ", count , " : ",image.shape)
print(count)
