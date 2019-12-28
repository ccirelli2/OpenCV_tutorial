# DOCUMENTATION ----------------------------------------
'''
Url:        https://docs.opencv.org/trunk/d9/d61/tutorial_py_morphological_ops.html
Erosion:    Erodes away the boundaries of the foreground object (always try to keep your
            objects in white).  Uses a 2D convolution.  A pixel will only be a one if all the
            pixels under the kernal are a 1.  Otherwise, it will be a 0.  What does 1 mean?
            Kernel: Try different kernel sizes.  It looks liek the larger the kernel the more
                    erosion will take place. 
            Note:   I tried this on an insurance application where the text was black and 
                    background white, and after 10 iterations it looked like the text
                    was blacked out with a marker. 
Dialation   Inverse of erosion.  In the case of the application image with black text and 
            white background, it erodes the black text and dialates the white. 
'''


# IMPORT LIBRARIES -------------------------------------

import cv2
import numpy as np
import matplotlib.pyplot as plt


# DIRECTORIES ------------------------------------------
dir_cv2_data    = r'/home/ccirelli2/Desktop/data/opencv_tutorials'
dir_ins_data    = r'/home/ccirelli2/Desktop/data/insurance_docs/starr_docs/imgs/app1' 

# DATA -------------------------------------------------
car             = 'car1.jpg'
read_car        = cv2.imread(dir_cv2_data + '/' + car, cv2.IMREAD_GRAYSCALE) 

app             = '1'
read_app        = cv2.imread(dir_ins_data + '/' + app, cv2.IMREAD_GRAYSCALE)

# FUNCTIONS ---------------------------------------------


def erode_img(read_img, num_iters):
    'Input: Image that has already been read in as gray scale'
    # Define kernel (uint8: Unsigned integer (0 to 255))
    kernel      = np.ones((7,7), np.uint8)
    # Erosion (img, kernel, number of iterations)
    eroded_img  = cv2.erode(read_img, kernel, iterations = num_iters)
    # Show Original and Eroded Image
    cv2.imshow('Original', read_img)
    cv2.waitKey(0)
    cv2.imshow('Eroded', eroded_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Return Eroded Image
    return eroded_img


def dialate_img(read_img, num_iters):
    'Not going to add the same documentation as above'
    # Define Kernel Size
    kernel  = np.ones((5,5), np.uint8)
    # Dialate Image
    dialted_img = cv2.dilate(read_img, kernel, iterations=num_iters)
    # Show Images
    cv2.imshow('Original', read_img)
    cv2.waitKey(0)
    cv2.imshow('Eroded', dialted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Return Dialted Image
    return dialate_img 

dialate_img(read_app, 1)



















