from skimage.io import imread,imsave,imshow
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import cm
import cv2
import add_logo as add




print(" \n \n\t \t \tWelcome to watermark tools.\n In this program you can preserve your images with adding your watermark.\n" )
print("First you need to enter the name of your image and your logo. The images and this program should be in the same repository.\n")


while True :
    try :
        image = input("Enter your image name here, like YourImage.jpg \n")
        img = imread(image)
        print("Image : " , img)
        my_logo = input("Enter your logo name here, like MyLogo.jpg \n")
        lg = imread(my_logo)
        print("logo : " , lg)
    except :
            print("Could not read" ,image,"Or could not read" ,my_logo)
    else : 
        break
print(" \n \n\t \t \tWatermark position \n")
while True:    
    y,x,z =np.shape(img)
    lg_y , lg_x,lg_z = np.shape(lg)
    pos  = input("Enter 'C' for center...\nEnter 'TL' for top left watermark... \n Enter 'TR' for top right watermark...\n Enter 'BL' for bottom left watermark...\n Enter 'BR' for bottom right watermark...\n If you want to specify a desire position for Y and X enter 'O' for other... \n" )
    if pos == "O":
        pos_y  = input("Enter your Y position...")
        pos_x = input("Enter your X position..." )
        if int(pos_y) > int(y) or int(pos_x) > int(x):
            print ("\n \nERROR:Assure that the value Y between 1 and " , int(y),"\n and X between 1 and ", int(x))
        elif int(pos_y) + int(lg_y) > int(y) or   int(pos_x) + int(lg_x) > int(x):
            print(" \n \nAccording to those positions, the watermark will be out of your image try another positions") 
        else : 
            print("All values is checked")
            break    
    if pos != "TL" and pos != "TR" and pos != "BL" and pos != "BR" and pos != "C" : 
        print ("Your input is not the correct value:")
    else :
        print("Your input is right" , pos)
        break    


# map the inputs to the function blocks
options = {"TL" : add.tl_watermark ,
           "TR" : add.tr_watermark,
           "BL" : add.bl_watermark,
           "BR" : add.br_watermark,
           "C"  : add.c_watermark,
           "O"  : add.o_watermark,
}

if pos == "O" :
    result = options["O"](img , lg , int(pos_y) , int(pos_x))
    imsave('etretat_watermark.jpg', result)
else :
    result = options[pos](img , lg)
    imsave('etretat_watermark.jpg', result)
plt.figure()
plt.imshow(img)
plt.title("Image with Watermark!")
plt.show()

print("END....")