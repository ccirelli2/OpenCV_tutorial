# Import Modules
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

# Documentation
'''
https://circuitdigest.com/tutorial/image-manipulation-in-python-opencv-part2
'''

# Import Image
os.chdir('/home/ccirelli2/Desktop/repositories/OpenCV_tutorial/data')
img_cyber = cv2.imread('cyber_image.jpg')


# Image Transformations - Affine & Non-Affine 
'''
Affine:     three types, scaling, rotating and translating.
            lines are parrallel before and after image transformation. 
Non-Affine: does not preserver parallelism, legth or angel.
            it does however preserve collinearity that two points lie on the same 
            straight line. 
'''

# Image Translations - Moving images up, down, left, right
'''
cv2.warpAffine:     Used to translate images.  Input = 

    * I dont' understand the documentation. 
'''



# Cropping - Cutting an dImage Region

def crop_img(img):
    img_cropped = img[100:200, 100:200]
    cv2.imshow('Cropped Image', img_cropped)
    cv2.waitKey()


# Lightening & Darkening Images
'''
Arithmetic operations in OpenCV basically are adding or subtracting matrixes to the image, adding or subtracting matrixes has effect on increasing or decreasing of brightness.

So to add or subtract matrixes we have to create them and numpy has a function called as np.ones that gives matrixes of 1’s same size as of our image.
'''

def light_dark_img(img):
    # np.ones returns a matrix w/ the same dimensions as our image
    M = np.ones(img.shape, dtype="uint8")
    print('Image shape', img.shape)
    print('np one shape', M.shape)
    
    # Add Matrix to Image (*100 to get a visible affect)
    img_add_m = cv2.add(img, M * 100)
    cv2.imshow('Brightened Image', img_add_m)
    cv2.waitKey()

    # Image Darker
    img_subtract_m = cv2.subtract(img, M * 100)
    cv2.imshow('Darker Image', img_subtract_m)
    cv2.waitKey()


























