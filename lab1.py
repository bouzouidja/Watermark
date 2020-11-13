
"""
from skimage.io import imread,imsave,imshow
#from matplotlib import pyplot as plt

from skimage.io import imread,imsave,imshow
%matplotlib inline



#############Image informations ###########
image = imread("camera.jpg")
plt.figure()
imshow(image)
plt.show()
"""

from skimage.io import imread,imsave,imshow
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import cm
#%matplotlib inline




####################################
##########READ & SAVE IMAGE#########
####################################
im = imread('camera.jpg')
#plt.figure()
#imshow(im)
imsave('camera-(copy).jpg', im)


print("this is the binary representation of the image" , im)
print("This is the len of image >>>> means height (hauteur)  :" ,len(im) )
print("this is the len of one element in the list of list or array of array of fixed size  for image >>>>> means the width (Largeur) :" , len(im[-1]) )
"""
maxx = 0
for  i in im:
	if max(i) > maxx :
		maxx= max(i)
print("the max value in the image >>>> the max value in the list of list : " , maxx) 

minn= 0
for  j in im:
	if min(j) < minn :
		minn= min(j)
print("the min value in the image >>>> the min value in the list of list : " , minn)
print("the type of pixel in the image is  : " , type(minn))
"""
np.ndarray(shape=(100,100))
print("shape with np :",np.shape(im)) # we don't have the third dimension, that means we have one channel >>> so we have a greyscale image !

print("Min/Max:", np.min(im), np.max(im)) #we could also use: im.min(), im.max()
print("Type: ", im.dtype)

## show the center of the image

print("point in the sky with coordinate y = 100 and x = 10" , im[100 ,10])

#print("this is  the center of the image ",imshow(im[100:250,100:250]))



####################################
##########IMAGE HISTOGRAM###########
####################################

### Plot a graph that show the average of each pixel (how many grey is it or how many white is it)

#plt.figure()
#plt.imshow(im, cmap=plt.cm.gray, vmin=0, vmax=255)
#plt.axis('off')
#plt.title("Cameraman")
#plt.show()

#create a list of tuple that contain key, value, the key can be from 0 to 255 and the value is the count of pixel that take this key
hist = np.zeros((256,))
for item in range(0,256) : 
	hist[item] = (im==item).sum()
#print("HISTOGRAM" , hist)
#plt.figure(figsize=(15,5))
plt.plot(hist)
plt.xlabel('Gray level')
plt.ylabel('Number of pixels')
#plt.show()
#print("histogram with  occurence" ,hist)




###################################HISTOGRAM ############
"""
normalized Histogram is an array like the occurence array but he gives the probability of distribution of values pixel (0>>255)
#So if we sum all values of this normalized array we should have sum equal to 1


norm_hist = hist/hist.sum()
#print("the sum of histogram" , norm_hist.sum())
plt.figure(figsize=(15,5))
plt.plot(norm_hist)
plt.xlabel('Gray level')
plt.ylabel('% of pixels')
plt.show()
"""
"""
dark_image = (im<=20)*(im>=10)
light_image = (im<=185)*(im>=150)
#print("dark_image histo" ,len(dark_image) )
#print(" light_image histo" , light_image)

plt.figure()
plt.subplot(1,2,1) # Subplots can show multiple images on the same figure.
plt.imshow(dark_image, cmap=plt.cm.gray)
plt.title('Cameraman?')
plt.subplot(1,2,2)
plt.imshow(light_image, cmap=plt.cm.gray)
plt.title('Sky?')
plt.show()
#print("histogram with  percentage" ,norm_hist)
#plt.show()
"""
pixels_in_cameraman = hist[10:20].sum()
pixels_in_sky = hist[150:185].sum()

print("There are around %d pixels in the cameraman and around %d pixels in the sky"%(pixels_in_cameraman, pixels_in_sky))




###########################ENTROPY #################


def norm_hist(im):
    # Compute normalized histogram
    h = np.zeros((256,))
    for v in range(0,256):
        h[v] = (im==v).sum()
    h /= h.sum()
    return h

def entropy(h):    
    # Compute entropy
    return -(h[h>0]*np.log2(h[h>0])).sum()

"""
""" 
#The entropy is a measure of amount of information in the image.
#The entropy will be higher when you have an even distribution of grayscale vale, and lower if the image is more homogeneous.
#The entropy give us information if the image is encoded uniformely (bits for nothing or some bits is not used!!! >>>>perte >>>> microprosessor SIMD computation) 
"""


A = (np.random.random((100,100))*255).astype('uint8')
B = np.zeros((100,100))
plt.figure()
plt.imshow(B,cmap = plt.cm.gray)
plt.title("random Image")
plt.show()

print("Entropy of a random image :", entropy(norm_hist(A)))
print("Entropy of a uniform image :", entropy(norm_hist(im)))

"""







############### IMAGE COMPRESSION ##############


"""
You need to do slicing in the array, and you  should know the tools hstack and vstack 
"""


"""
### TOOLS 
I = np.arange(16).reshape((4,4))
print(I)
print(I[0:-1,0:-1]) # From 0 to -1 (1 before the end) on each dimension
print(I[0:-1:3,0:-1:3]) # From 0 to -1 (1 before the end) on each dimension, with a stride of 2



a = im[0:-1:20,0:-1:20]

plt.figure()
plt.imshow(a,cmap = plt.cm.gray)
plt.title("Sliced Image")
plt.show()

b = I[1::2,0::2]
print("a:")
print(a)
print("b:")
print(b)
print("hstack:")
print(np.hstack((a,b)))
print("vstack:")
print(np.vstack((a,b)))
#####

"""


##### THIS IS THE PYRAMID COMPRESSING#########
# Modify this method:
def split(im ,level):
	
    # splitting####
    if( level <= 0 ): return im # end recursion
    
    a = im[0:-1:2,0:-1:2]
    b = im[0:-1:2,1::2]-a
    c = im[1::2,0:-1:2]-a
    d = im[1::2,1::2]-a
    ### compressing vertically each subimage splited
    R = np.vstack((np.hstack((split(a,level-1),b)),np.hstack((c,d)))) # recursion call going down one level
    return R



"""
# We have to convert to 'int' because the original type is 'unsigned int' and we will need negative values...
im = imread('camera.jpg').astype(np.int)
plt.figure(figsize=[4,4])
plt.imshow(split(im,1),interpolation='nearest',cmap=plt.cm.gray,vmin=-255, vmax=255)
plt.title("Split 1 time")
plt.axis('off')
plt.figure(figsize=[4,4])
plt.imshow(split(im,8),interpolation='nearest',cmap=plt.cm.gray,vmin=-255, vmax=255)
plt.title("Split 8 times")
plt.axis('off')
plt.show()


"""

# RECONSTRUCTION OF COMPRESSED IMAGE#####

def reconstruct(s, level):

    if level==0: return s
    
    # We first need to go "deep" into the top-left half
    m = s.shape[0]//2
    n = s.shape[1]//2
    a = reconstruct(s[0:m,0:n],level-1)

    # Once we have reconstructed the top left half, we can use the remainders to reconstruct the original.
    b = s[0:m,n:]
    c = s[m:,0:n]
    d = s[m:,n:]

    r = np.zeros(s.shape)
    r[0:-1:2,0:-1:2]=a
    r[0:-1:2,1::2]=b+a
    r[1::2,0:-1:2]=c+a
    r[1::2,1::2]=d+a
    
    return r



"""
# Testing:
im = imread('camera.jpg').astype(np.int)
compressed = split(im,8)
rec = reconstruct(compressed,8)

plt.figure(figsize=(15,8))
plt.subplot(1,3,1)
plt.imshow(im,interpolation='nearest',cmap=plt.cm.gray,vmin=0, vmax=255)
plt.subplot(1,3,2)
plt.imshow(compressed,interpolation='nearest',cmap=plt.cm.gray,vmin=-255, vmax=255)
plt.subplot(1,3,3)
plt.imshow(rec,interpolation='nearest',cmap=plt.cm.gray,vmin=0, vmax=255)
plt.show()
"""


####### CO Occurence MATRIX #####

####the co-occurrence matrix gives us information about the spatial distribution of pixel.

from skimage.feature import greycomatrix



im = imread('camera.jpg')

distances = [5,50] # Distances in pixels that we want to check
angles = [0, np.pi/2] # Angles in radians that we want to check

co_matrices = greycomatrix(im, distances, angles)
#print("this is the co max", co_matrices)

def norm_gcmat(gcmat):
    return gcmat/gcmat.sum()


plt.figure(figsize=(8,8))

i = 1
for idd,d in enumerate(distances):
    for ida,a in enumerate(angles):
        plt.subplot(2,2,i)
        plt.imshow(co_matrices[:,:,idd,ida], vmin=co_matrices.min(), vmax=co_matrices.max()) # Give the same scale to all images!
        plt.title('d = %d, a = %.2f, entropy=%.2f'%(d,a,entropy(norm_gcmat(co_matrices[:,:,idd,ida]))))
        i += 1
plt.show()






###########COLOR EPRESENTATION ###################"




from skimage.data import immunohistochemistry

im = immunohistochemistry() # scikit-image method to load the example image
print(im.shape,im.dtype)
r = im[:,:,0]
g = im[:,:,1]
b = im[:,:,2]

plt.gray() # Use grayscale by default on 1-channel images, so you don't have to add cmap=plt.cm.gray everytime

plt.figure(figsize=(12,12))
plt.subplot(2,2,1)
plt.imshow(im)
plt.title('RGB')
plt.subplot(2,2,2)
plt.imshow(r)
plt.title('Red')
plt.subplot(2,2,3)
plt.imshow(g)
plt.title('Green')
plt.subplot(2,2,4)
plt.imshow(b)
plt.title('Blue')
plt.show()