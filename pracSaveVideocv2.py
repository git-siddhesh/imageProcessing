import numpy as np
import cv2

'''cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()'''

# to play any saved video
cap= cv2.VideoCapture('test.avi')
while(cap.isOpened()):
    status,frame=cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.flip(gray,0)
    cv2.imshow('frame',gray)
    if cv2.waitKey(20) & 0xff == ord('\r'):break
cap.release
cv2.destroyAllWindows()
`   