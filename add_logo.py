import numpy as np
import cv2





#################################################
############# Watermark function  BLOCK #########
def tl_watermark(image , logo):
    print ("tl_watermark.\n")
    y,x,z = np.shape(image)
    y_logo , x_logo , z_logo = np.shape(logo)
    logo_place = image[ 0 : y_logo  , 0: x_logo]
    result = cv2.addWeighted(logo_place , 1 , logo , 0.8 , 0)
    image[ 0 : y_logo  , 0: x_logo] = result #logo in the bottom right
    return image
def tr_watermark(image , logo):
    print ("tr_watermark\n")
    y,x,z = np.shape(image)
    y_logo , x_logo , z_logo = np.shape(logo)
    logo_place = image[ 0 : y_logo  , x- x_logo : x]
    result = cv2.addWeighted(logo_place , 1 , logo , 0.8 , 0)
    image[ 0 : y_logo  , x- x_logo : x] = result #logo in the bottom right
    return image
    
def bl_watermark(image , logo):
    print ("bl_watermark\n")
    y,x,z = np.shape(image)
    y_logo , x_logo , z_logo = np.shape(logo)
    logo_place = image[ y- y_logo : y  , x- x_logo: x]
    result = cv2.addWeighted(logo_place , 1 , logo , 0.8 , 0)
    image[ y- y_logo : y  , 0: x_logo] = result #logo in the bottom right
    return image
def br_watermark(image , logo):
    print ("br_watermark\n")
    y,x,z = np.shape(image)
    y_logo , x_logo , z_logo = np.shape(logo)
    logo_place = image[ y- y_logo : y  , x- x_logo: x]
    result = cv2.addWeighted(logo_place , 1 , logo , 0.8 , 0)
    image[ y- y_logo : y  , x- x_logo: x] = result #logo in the bottom right
    return image
def c_watermark(image , logo):
    print ("c_watermark\n")
    y,x,z = np.shape(image)
    y_logo , x_logo , z_logo = np.shape(logo)
    logo_place = image[  int(y/2) - int(y_logo/2): int(y/2) - int(y_logo/2) +y_logo , int(x/2)- int(x_logo/2):int(x/2)- int(x_logo/2)+ x_logo]
    result = cv2.addWeighted(logo_place , 1 , logo , 0.8 , 0)
    image[  int(y/2) - int(y_logo/2): int(y/2) - int(y_logo/2) +y_logo    , int(x/2)- int(x_logo/2):int(x/2)- int(x_logo/2)+ x_logo] = result #logo in the bottom right
    return image


def o_watermark(image , logo , y,x):
    print ("o_watermark\n")
    im_y,im_x,im_z = np.shape(image)
    y_logo , x_logo , z_logo = np.shape(logo)
    logo_place = image[  y: y+ y_logo , x: x+ x_logo]
    result = cv2.addWeighted(logo_place , 1 , logo , 0.7 , 0)
    image[  y: y+ y_logo , x: x+ x_logo] = result #logo in the bottom right
    return image    

#############################################################
#############################################################
