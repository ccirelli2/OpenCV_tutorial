# Import Libraries -----------------------------------------------
import cv2
from matplotlib import pyplot as plt
import os
import numpy as np


# Import Data Files ---------------------------------------------
os.chdir('/home/ccirelli2/Desktop/repositories/OpenCV_tutorial/data')


# Features --------------------------------------------------------
'''
Features:       Tutorial uses a building as an example image.  Shows how edges and corners
                are more easily identified versus flat surfaces.  Basically the corners of 
                images provide the best source of information to identify what the image is. 

Feature 
Detection:      Find the regions of the image with maximum variation when moved 
                (by a small amount). 

Feature 
Description:    Matching words to the features detected.

'''

# Harris Corner Detection ----------------------------------------
'''
Functions:      cv2.cornerHarris(), cv2.cornerSubPix()

Corner:         "a point whose local neighborhood stands in two dominant and
                different edge directions, where an edge is a sudden change in 
                image brightness (or I assume intensity)". 
                "points of interest that are invariant to translation, rotation, 
                and illumination (so unique)"
                
Topics 2 Review: 
                Harris Corner Detection
                Taylor Series
                Eigen Values & Vectors

'''


# Harris Corner Detection Code -----------------------------------

# Load Image
img = cv2.imread('license_plate.jpg')
img_lic_plate = cv2.imread('chessboard.jpg')

def harris_corner_detector(img):
    # Convert to Grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dst = cv2.cornerHarris(img_gray, 2, 3, 0.04)      # (img, blocksize, ksize, k)
    dst_dialate = cv2.dilate(dst, None)
    # Threshold for an optimal value, it may vary depending on the image
    img[dst_dialate > 0.01 * dst_dialate.max()] = [0,0,255]
    cv2.imshow('New Image', img)

    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
    return None


# Shi-Tomasi Corner Detector ------------------------------------------
'''


'''
def shi_tomasi_corner_detector(img):
    # Convert to Grey
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find Corners
    ''' 25  =   num of corners to find, 
        0.01 =  is the quality lvl or min threshold of lamda lamda values
        10  =   min euclidean distance between corners detected.  The algorithm
                searches for the best corner within a region and throws out the rest. 
    '''
    corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10) 
    corners = np.int0(corners)

    for i in corners:
        'ravel() is a numpy operation that returns a flattened 1-D array'
        x,y = i.ravel()
        cv2.circle(img, (x,y), 2, 255, -1)

    plt.imshow(img), plt.show()

shi_tomasi_corner_detector(img_lic_plate)











