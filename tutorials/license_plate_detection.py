# Import Libraries
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
'''
Links:
    Contours        https://circuitdigest.com/tutorial/image-segmentation-using-opencv
    License Plate   https://circuitdigest.com/microcontroller-projects/
                    license-plate-recognition-using-raspberry-pi-and-opencv


Bilateral Filter:   Two gaussian functions, one applied to nearby pixels and a gaussian
                    function of intensity difference make sure only thos epixels with 
                    similar intensity to central pixel is considerred for bluring. 
                    This avoids bluring edges. 

Contours            Contours can be explained simply as a curve joining all the 
                    continuous points (along the boundary), having same color or 
                    intensity. The contours are a useful tool for shape analysis 
                    and object detection and recognition.
'''

# Import Images
os.chdir('/home/ccirelli2/Desktop/repositories/OpenCV_tutorial/data')
img_car = cv2.imread('car1.jpg')
'https://circuitdigest.com/microcontroller-projects/license-plate-recognition-using-raspberry-pi-and-opencv'


img_car_resize = cv2.resize(img_car, (1240,960))
img_car_gray = cv2.cvtColor(img_car_resize, cv2.COLOR_BGR2GRAY)
img_car_blur = cv2.bilateralFilter(img_car_gray, 11, 17, 17)

edged = cv2.Canny(img_car_blur, 20, 200)
nts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#cv2.imshow('Image Edges', edged)
#cv2.waitKey(0)



