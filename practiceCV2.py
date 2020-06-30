'''import cv2
cap=cv2.VideoCapture(0)
status,frame=cap.read()
cv2.imshow('image',frame)
k=cv2.waitKey(0) & 0xff
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('messieimg.png',frame)
    cv2.destroyAllWindows()
'''

import numpy as np 
import cv2
cap=cv2.VideoCapture(0)
plugin=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('test.avi',plugin,20.0,(640,480))
while cap.isOpened():
    status,frame = cap.read()
    if status:
        frame=cv2.flip(frame,0)
        out.write(frame)
        cv2.imshow('myframe',frame)
        if cv2.waitKey(10) & 0xff == ord('\r'):
            break
    else :
        print("image can not be captured")
cv2.destroyAllWindows()
cap.release()
out.release()
