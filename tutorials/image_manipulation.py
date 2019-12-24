# DOCUMENTATION -----------------------------------------------------------
'''
https://circuitdigest.com/tutorial/image-manipulation-in-python-opencv-part2


Affine:         three types, scaling, rotating and translating.
                lines are parrallel before and after image transformation. 
Non-Affine:     does not preserver parallelism, legth or angel.
                it does however preserve collinearity that two points lie on the same 
                straight line. 

cv2.warpAffine: Used to translate images.
                URL: https://docs.opencv.org/2.4/modules/imgproc/doc/
                     geometric_transformations.html?highlight=warpaffine                
                Requires a translation matrix where T = 1 0 Tx
                                                        0 1 Ty
                Where in Tx is a shift along the X-axis





Arithmetic operations:
                basically are adding or subtracting matrixes to the image, adding or 
                subtracting matrixes has effect on increasing or decreasing of brightness.
                So to add or subtract matrixes we have to create them and numpy has a 
                function called as np.ones that gives matrixes of 1’s same size as of our image.



'''

# IMPORT LIBRARIES ------------------------------------------------------------
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt


# DEFINE DIRECTORIES ----------------------------------------------------------
dir_data    =     r'/home/ccirelli2/Desktop/data/opencv_proj'

# IMPORT DATA -----------------------------------------------------------------
img1        = 'punisher.jpg'

# LOAD DATA -------------------------------------------------------------------
path2img1   = dir_data + '/' + img1


# FUNCTIONS -------------------------------------------------------------------

def shift_pos_img(path2img):
    # Read Image
    img_read = cv2.imread(path2img, cv2.IMREAD_GRAYSCALE)
    # Get Image Height, Width
    img_shape   = img_read.shape
    height, width = img_shape
    quarter_height, quarter_width = height/4, width/4
    T   = np.float32([[1,0, quarter_width], [0,1, quarter_height]])




shift_pos_img(path2img1)




# Cropping - Cutting an dImage Region

def crop_img(img):
    img_cropped = img[100:200, 100:200]
    cv2.imshow('Cropped Image', img_cropped)
    cv2.waitKey()


# Lightening & Darkening Images

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


























