# DOCUMENTATION --------------------------------------------------------
''' Desc:       Tutorial for affine transformations of imgs using warpAffine
    Tutorial:   https://circuitdigest.com/tutorial/image-manipulation-in-python-opencv-part1
    Math:       https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/
                warp_affine/warp_affine.html


    Rotation:   Rotating an image about a point or the point in the center of the 
                image.  T =     |Cos -Sin|  where theta (not shown) is the angle
                                |Sin  Cos|  of rotation, measured in anti-clockwise dir. 
'''


# IMPORT LIBRARIES -----------------------------------------------------
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


# DEFINE DIRECTORIES --------------------------------------------------
dir_imgs    = r'/home/ccirelli2/Desktop/data/opencv_imgs'

# IMPORT DATA ---------------------------------------------------------
img1    = dir_imgs + '/' + 'punisher.jpg'
img2    = dir_imgs + '/' + 'car1.jpg'

# FUNCTONS ------------------------------------------------------------

def translate_img(img):
    # Read Image
    img_read    = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    # Get Height and Width (note, need to read in as b&w or shape is diff)
    height, width   = img_read.shape
    # Calculate Quarter height and width    
    qu_height, qu_width = height/4, width/4 
    # Define the Transformation Matrix
    ''' Remember from Linear Algebra, this is a 2x3 or 2x2 matrix used to 
        transform "T" the x/y coordinates of the images
        T = 1 0 T(x)
            0 1 T(y)
    '''
    T   = np.float32([[1,0, qu_width], [0, 1, qu_height]])

    # Use the warpAffine function to apply the transformation (image, T, (cols, rows))
    img_translate = cv2.warpAffine(img_read, T, (width, height))
    
    # Show Original Image
    cv2.imshow('Original', img_read)
    cv2.waitKey(0)

    # Show Translated Image
    cv2.imshow('Translated', img_translate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # return transformed image
    return img_translate



def rotate_img(img):
    # Read Image
    img_read    = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    # Get Height and Width (note, need to read in as b&w or shape is diff)
    height, width   = img_read.shape
    # Divide height and width by 2 to get the center point of the image
    'cv2.getRotationMatrix2D(rotation_center_x, rotation_center_y, angle of  rotation, scale)'
    rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 15, 1)
    # Apply warpAffine to rotate
    rotated_img     = cv2.warpAffine(img_read, rotation_matrix, (width, height))

    # Show original image
    cv2.imshow('Original', img_read)
    cv2.waitKey(0)
     
    # Show Rotated Image
    cv2.imshow('Rotated', rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Return rotated image
    return 

rotate_img(img2)









