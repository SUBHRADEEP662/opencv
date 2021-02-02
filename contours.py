from cv2 import cv2
import numpy as np


img = cv2.imread('img1.jpg')

# cv2.imshow('Original', img)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# # cv2.imshow('Gray', gray)

canny = cv2.Canny(img, 125, 175)

# cv2.imshow('Canny', canny)

# contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# print(len(contours))

# ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# cv2.imshow('Thresh', thresh)     
# print(ret)

blank = np.zeros(img.shape, dtype='uint8')
# cv2.imshow('Blank', blank)

cv2.drawContours(blank, contours, -1, (0,0,255) ,1)
cv2.imshow("Blank", blank)

cv2.waitKey(0)