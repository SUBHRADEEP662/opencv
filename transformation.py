from cv2 import cv2
import numpy as np

img = cv2.imread('img1.jpg')

cv2.imshow('Original', img)

#Translation

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimentions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimentions)

#-x ==> left
#+x ==> right
#+y ==> down
#-y ==> up

translated = translate(img, 100, 100)
# cv2.imshow('Translated', translated)


#Rotation 

# def rotate(img, angle, rotPoint=None):
#     (height, width) = img.shape[:2]
#     if rotPoint is None:
#         rotPoint = (width//2, height//2) 

#     rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimentions = (width, height)
#     return cv2.warpAffine(img, rotMat, dimentions)


# rotated = rotate(img, 45)
# cv2.imshow('Rotated', rotated)


#Resizing

# resized = cv2.resize(img, (600, 600), interpolation=cv2.INTER_LINEAR)
# cv2.imshow('Resized', resized)


#Flipping

# flip0 = cv2.flip(img, 0)
# flip1 = cv2.flip(img, 1)
# flip2 = cv2.flip(img, -1)
# cv2.imshow('Flipped0', flip0)
# cv2.imshow('Flipped1', flip1)
# cv2.imshow('Flipped2', flip2)

  
#Cropping

cropped = img[100:200, 100:200]
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)