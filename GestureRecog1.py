import cv2
import numpy as np 
'''Convex hull : using this function we can find the outermost pixel of boundary and connect them '''

cap = cv2.VideoCapture(0)
'''plugin = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("NewVideo.avi",plugin,24,(640,480))
while cap.isOpened():
    status,frame = cap.read()
    cv2.imshow("frame",frame)
    output.write(frame)
    if cv2.waitKey(10) & 0xff == ord('\r') : break
'''
status,frame = cap.read()
grayimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image",grayimg)

ret,the = cv2.threshold(grayimg, 70,255, cv2.THRESH_BINARY)
cv2.imshow("Threshold",the)

con,_ = cv2.findContours(the.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = [cv2.convexHull(c) for c in con]

final = cv2.drawContours(grayimg, hull, -1, (255,0,0))
cv2.imshow("hull",final)

cv2.waitKey(0)

