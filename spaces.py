# Conversion of color spaces to different color spaces, like: RGB -> BGR, BR -> GrayScale, etc

from cv2 import cv2

import matplotlib.pyplot as plt

img = cv2.imread('img1.jpg')

plt.imshow(img)

plt.show()