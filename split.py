import cv2 as cv

img = cv.imread('img1.jpg')

cv.imshow('Original', img)

r, g, b = cv.split(img)

cv.imshow('RED', b)

cv.waitKey(0)

cv.destroyAllWindows()