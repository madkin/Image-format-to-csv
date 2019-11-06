# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 21:45:58 2019

@author: MAdkin
"""

#load necessary libraries

import numpy as np #for computing

from PIL import Image #for Dealiong with images
import os # for working with operating sysytem
import sys # system specific parameters
import csv # dealding with csv file 


# Default format can be changed as needed jpg png
def createFileList(myDir, format='.png'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList

# load the original image in to the list
# Here "./Au/"  is the folder name which contains the images        
myFileList = createFileList('./Au/')

for file in myFileList:
    print(file)
    img_file = Image.open(file)

    # get original image parameters...
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

    # Convert image Greyscale and save as a CSV file
    img_grey = img_file.convert('L')
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
    value = value.flatten()
    print(value)
    with open("Normal_images.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(value)
        
# the number of imabges should be limited as it may result in a largerfile
#  that the system may not be able tpo open less than 32000 rows and 16000 column     
        