# IMPORT MODULES ------------------------------------------------
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

# Import Image -------------------------------------------------
os.chdir('/home/ccirelli2/Desktop/repositories/OpenCV_tutorial/data')
img_punisher    = cv2.imread('punisher.jpg')
img_cyber_gray  = cv2.imread('cyber_image.jpg') 
img_cyber_color = cv2.imread('cyber_image.jpg', 1)

# Access Pixels ----------------------------------------------
'Indexing:  You just call the i and j coordinates'
def access_pixels(img, x, y):
    px_100 = img[x,y]
    'Pixel Value:   simply print the object.  For color it will return 3 values'
    print('Pixel values = {}'.format(px_100))

# Access Pixel of Color Image --------------------------------
'''0 = Blue, 1 = Green, 2 = Red'''
def access_pixel_color(img, x, y, color):
    print(img.item(x, y, color))

    

# Modify Pixel Values-----------------------------------------
def modify_pixels(img, x, y):
    '''Simply reassign the pixel a new value
    img = image, x = x cordinate, y = y coordinate
    255 = pure white'''
    img[0:x,0:y] = [255,255,255]
    cv2.imshow('test', img)
    cv2.waitKey(0)
    # Return None
    return none


# Accessing Image shape ---------------------------------------
def get_img_shape(img):
    print('Shape = {}'.format(img.shape))
    print('Size  = {}'.format(img.size))
    print('D-type= {}'.format(img.dtype))



# Image ROI --------------------------------------------------
''' ROI = Region of Interest
    The book says that you first find the face and then the 
    features like eyes, nose, etc.'''


# Splitting & Merging Image Channels ------------------------
'''
Splitting:  BGR channels of an image can be split into their individual 
            planes when needed
'''
def split_img_channels(img):
    b, g, r = cv2.split(img)
    cv2.imshow('blue', b)
    cv2.imshow('green', g)
    cv2.imshow('red', r)
    cv2.waitKey(0)
    return None


# Making Borders for Images (Padding) -------------------------------

def create_img_border(img):
    RED     = [255, 0, 0]
    GREEN   = [0, 255, 0]
    BLUE    = [0, 0, 255] 

    constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)
    plt.subplot(231) ,plt.imshow(constant, 'Blues_r'), plt.title('CONSTANT BORDER COLOR')
    plt.show()
    cv2.waitKey(0)















