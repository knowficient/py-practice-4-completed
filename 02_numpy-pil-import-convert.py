# convert colour image into grayscale using manual numpy matrix conversion
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#dummy = np.zeros((10, 10))

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

# convert array into uint8 instead of float
imgy = Image.fromarray(grayfloat.astype(np.uint8))
imgy.save('car-gray-blur.png')

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
plt.title('Gray', fontsize=10)
#replace the correct variable dummy for your plot
plt.imshow(imgy, cmap = plt.get_cmap(name = 'gray'), vmin=0, vmax=255)
# Show the plot
plt.show()
