import cv2 as cv

#img = cv.imread('img1.jpg')
#cv.imshow('Nature', img)
#cv.waitKey(0)


capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('video1', frame)
    
    if cv.waitKey(20) & 0xFF==ord('q'):
        break
capture.release()
cv.destroyAllWindows()
