# Import Modules
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

# Documentation
'''
Tutorial:       https://circuitdigest.com/tutorial/getting-started-with-opencv-image-processing

'''

# Load Images 
os.chdir('/home/ccirelli2/Desktop/repositories/OpenCV_tutorial/data')
img_cyber = cv2.imread('cyber_image.jpg')



# Grey Scaling Image ------------------------------------------------------
def show_img(img):
    cv2.imshow('Cyber Image', img)
    cv2.waitKey()


def image_grey(img):
    "You also add 0 to imread('name', 0)"
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow(image_gray)

def get_shape(img):
    print('Image shape = {}'.format(img.shape))


def get_color(img):
    'cv2 stores colors in BGR, not RBG'
    print(img[100,100]) # should return three colors for this pixel


def split_color_img(img):
    'split image into three planes of each color'
    B, G, R = cv2.split(img)
    print('Red', R)
    print('Green' , G)


def histogram_rep_of_img(img):
    '''Create a histogram representation of image, freq of intensity'''
    B, G, R = cv2.split(img)
    plt.hist(list(B))
    plt.show()

histogram_rep_of_img(img_cyber)


