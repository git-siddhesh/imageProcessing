# EVENT in cv2 

import cv2
import numpy as np 

# mousecall back function

def Draw_cicle(event,x,y,flags,param):
    if event == (cv2.EVENT_MOUSEMOVE and cv2.EVENT_FLAG_CTRLKEY):
        cv2.circle(img,(x,y),10,(250,0,0),-1)

# create a black image (window)
# and bind the function with it

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',Draw_cicle)

while 1: 
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

cv2.createTrackbar(tb,window)

