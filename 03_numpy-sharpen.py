# sharpen image using numpy convolution
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image



# convolution 2D function
def convolution2d(image, kernel, bias):
    m, n = kernel.shape
    if (m == n):
        y, x = image.shape
        y = y - m + 1
        x = x - m + 1
        new = np.zeros((y,x))
        for i in range(y):
            for j in range(x):
                new[i,j] = np.sum(image[i:i+m, j:j+m]*kernel) + bias
    return new

# GrayScale Method 1: Function RGB to Gray Level
# luminance (E'y) in Rec.ITU-R BT.601-7l
# Gray = 0.299*r + 0.587*g + 0.114*b
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
# Open the input image as numpy array
# configure data tpe as uint8, as default uint32
img = np.array(Image.open("car-blur.png"), dtype = np.uint8)
# Convert RGB to Grayscale
grayfloat = rgb2gray(img)
#Create the kernel 3x3 matrix
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
# apply convolution
imgc = convolution2d(grayfloat, kernel, 0)

# Set plot size in inch
plt.figure(figsize=(10, 5), dpi=140)
# Plot colour image image
plt.subplot(121)
plt.axis('on')
plt.title('Original', fontsize=10)
#replace the correct variable dummy for your plot
plt.imshow(img)
# Plot gray image
plt.subplot(122)
plt.axis('on')
plt.title('Convolve', fontsize=10)
#replace the correct variable dummy for your plot
plt.imshow(imgc, cmap = plt.get_cmap(name = 'gray'), vmin=0, vmax=255)
# Show the plot
plt.show()

