
from cv2 import cv2


img = cv2.imread('img1.jpg')

# Converting to grayscale image

# gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# cv2.imshow('Gray', gray)
# cv2.waitKey(0)

#Blur

# blur = cv2.GaussianBlur(img, (7, 7), cv2.BORDER_DEFAULT)
# cv2.imshow('Blured', blur) 

# Edge Cascade

# canny = cv2.Canny(img, 125, 175)
# cv2.imshow('Canny', canny)

#Dialating images

# dilated = cv2.dilate(canny, (5, 5), iterations=1)
# cv2.imshow('Dilated', dilated)

#Eroding

# eroded = cv2.erode(dilated, (3, 3), iterations=1)

# cv2.imshow('Eroded', eroded)


#Resizing

# resized = cv2.resize(img, (5000, 5000), interpolation=cv2.INTER_CUBIC)

# resized1 = cv2.resize(img, (5000, 5000))
# cv2.imshow('Resized with Inter_cubic', resized)
# cv2.imshow('Resized without Inter_cubic', resized1)

#Cropping

cropped =  img[100:300, 200:400]
cv2.imshow('Cropped', cropped)

cv2.imshow('Original', img)
cv2.waitKey(0)

