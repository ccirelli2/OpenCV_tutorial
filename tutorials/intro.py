'''
Tutorial:   https://www.tutorialspoint.com/opencv/opencv_overview.htm
'''

# MODULES --------------------------------------------------------------
import cv2 
import numpy as np
from matplotlib import pyplot as plt


# How to read and write an image -------------------------------------- 
'''
functions   = cv2.imread(), cv2.imshow(), cv2.imwrite()
flags       = 1:    load color image
              0:    load image in grayscale
             -1:    load image as such including alpha channel'''

img_punisher = cv2.imread('punisher.jpg', 0)
#print('Shape of punisher image = {}'.format(img_punisher.shape))


# Print Image to a window----------------------------------------------
'''cv2.imshow():    first argument is the name of the window
                    the second is the image object that you created from imread()
'''
def show_image(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    return None

# Write Image --------------------------------------------------------
'''
cv2.imwrite('file_name', img2save)
img2save:   will save the image in png format
'''

def save_image(filename, image):
    cv2.imwrite(filename, image)
    print('image successfully saved')
    return None


# Display Image using Matplotlib --------------------------------------

def display_img_plt(filename):
    img = cv2.imread(filename, 0)
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([]) # hide tick values on x and y axis
    plt.show()


# Capture & Read Video from Camera ------------------------------------
'''
methodology:    To capture a video you need to create a VideoCapture object. 
                The arguments can be either the device index (?) or the name
                of a video file. 
Device Index:   Indicate which device to use (I guess 0 = the internal camera)
'''

def capture_image():
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Operations on the frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything is done release the capture
    cap.release()
    cv2.destroyAllWindows()


# Saving a Video ------ -------------------------------------------------
'''
methodology:    Create a VideoWriter object. 

'''


def saving_a_video():
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # File name, fourcc code, number of frames per second, and frame size
    out = cv2.VideoWriter('test_output_vid.avi', fourcc, 20.0, (640, 480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame, 1)

            # Write the flipped frame
            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    # Return None
    return None















