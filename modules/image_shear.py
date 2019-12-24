# DOCUMENTATION -----------------------------------------------------------
'''
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


# Define Zero Value MxN Matrix
row =   5
col =   5
m = np.zeros((row,col))

# Create a Line in the Middle of the Image
m[:,2] = 255 


# Define Matrix for Affine Transformation

T   = np.array([1,3], [0,1])





def get_list_loc_n_pixel_val(np_matrix):
    ''' Desc:   This function is used to transform a numpy array of image pixel 
                values into a structure that captures both the location (x,y) 
                coordinate and value of the pixel. The purpose is so that we can 
                apply an affine transformation to the location of the pixels and 
                return the new location of the pixel values to the user. 
    
        Funct:  This function takes a list of arrays of integers; 
                ex: [[0,0], [0,0]] and return a list of lists
                in the form [((row_index, col_index), pixel_val)]
    '''
    # List of lists
    row_lists   = []
    # Row Count
    row_count   = -1

    # Iterate Each Row of Matrix
    for row in np_matrix:
        # Increase Row Count
        row_count += 1

        # Define list for col values
        col_vals    = []
        # Column Count
        col_count   = -1

        # For Value in Row
        for val in row:
            # Increase Col Count
            col_count +=1

            # Define Position & Pixel Values
            pos_value   = row_count, col_count
            pixel_value = np_matrix[row_count, col_count]
            
            # Append Position & Pixel Values to Col Val List
            col_vals.append((pos_value, pixel_value))

        # Append Column Values List to Row Lists
        row_lists.append(col_vals)

    # Return row_lists
    return row_lists

list_tuples = create_tuple_loc_val(m)




def apply_affine_tranf_2_nparray(list_of_list_of_tuples, matrix_transformer):
    ''' Desc:   Applies a transformation of the form T(u) where T is a matrix
                and u is the location of the pixel in the image. 
                The purpose is to create an affine transformation of an image. 
    '''
    




    pass





def return_typle_loc_val_2_np_matrix(list_tuple_obj):
    ''' Desc:   Convert list of lists of tuple values
                back to original nparray structure. 
        Input:  list of list of tuple values
                ex: [[((0,0), 255.0), ((0,1), 0)...
        Output: nparray w/ n rows of lists w/ values
                equal to pixel intensity. 
    '''
    
    # Get Num Rows Input Object
    row_count   =   0 
    for row in list_tuple_obj:
        row_count +=1
    
    # Get Col Count Input Object
    col_count   = len(list_tuple_obj[0])
   
    # Create Numpy Zero Array of Same Dimensions
    np_zero_array   = np.zeros((row_count, col_count))

    # Assing values of input object to np zero matrix
    row_count   = -1
    
    # Iterate Rows of Input Tuple Object
    for row in list_tuple_obj:
        row_count +=1

        # Iteratate Columns
        for col in row:
            new_row_index   = col[0][0]
            new_col_index   = col[0][1]
            new_pixel_val   = col[1]

            # Assign Values
            np_zero_array[new_row_index, new_col_index] = new_pixel_val 

    # Return np object
    return np_zero_array
    









