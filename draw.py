
import cv2
import numpy as np

img = cv2.imread('img1.jpg')
#cv2.imshow('Image', img)

blank = np.zeros((500, 500, 3), dtype='uint8')


#print(blank.shape)
#blank[100:400, 100:400] = 0, 255, 255

#cv2.rectangle(blank, (100, 100), (400, 400), (255, 0, 255), thickness = 2)
#cv2.rectangle(blank, (100, 100), (400, 400), (255, 0, 255), thickness = cv2.FILLED)
#cv2.rectangle(blank, (100, 100), (400, 400), (255, 0, 255), thickness = -1)
#cv2.rectangle(blank, (blank.shape[1]//3, blank.shape[0]//2), (300, 400), (0, 255, 255), thickness = 2)
#cv2.circle(blank, (255, 255), 50, (120, 150, 90), thickness = 2)

#cv2.line(blank, (100, 100), (400, 400), (0, 255, 0), thickness = 5)
#cv2.line(blank, (100, 400), (400, 100), (0, 255, 0), thickness = 5)
#cv2.line(blank, (100, 250), (400, 250), (0, 255, 0), thickness = 5)
#cv2.line(blank, (250, 100), (250, 400), (0, 255, 0), thickness = 5)

cv2.putText(blank, 'I am Subhradeep Halder', (100, 200), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 255, 0))

cv2.imshow('Blank', blank)

cv2.waitKey(0)
