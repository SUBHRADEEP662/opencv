import cv2 as cv

img = cv.imread('img1.jpg')

cv.imshow('Original', img)

# Averaging
average = cv.blur(img, (7, 7))
cv.imshow('Blur', average)

# Gaussian blur

gaussian = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian blur', gaussian)

# Median blur

median = cv.medianBlur(img, 3)
cv.imshow('Median blur', median)

# Bilateral

bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral blur', bilateral)

cv.waitKey(0)
cv.destroyAllWindows()
