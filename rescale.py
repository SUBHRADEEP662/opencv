import cv2 

def rescale(frame, scale = 1):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    
    dimension = (width, height)
    return cv2.resize(frame, dimension)
    

capture = cv2.VideoCapture('video1.mp4')

while True:
    isTrue, frame = capture.read()
    
    #cv2.imshow('Original', frame)
        
    
    i = 0.5
    while(i<=2.00):
        cv2.imshow('Resized'+str(i), rescale(frame, scale=i))
        i = i + 0.05
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()



