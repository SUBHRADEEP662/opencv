from cv2 import cv2 
import numpy as np

img = cv2.imread('img1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

for idx, i in np.ndenumerate(gray):
    if(i>=200):
        cv2.circle(gray, idx, 20, (255, 255, 255), 10)
        print(type(idx))
        print('White found')
        break 

cv2.imshow('White', gray)
cv2.waitKey(0)