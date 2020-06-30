import cv2
cap=cv2.VideoCapture(0)
n=0
print(cap.isOpened)
while cap.isOpened():
    status,frame=cap.read()
    # converting image into gre scale
    print(status)
    grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    matplt=cv2.cvtColor(frame,cv2.COLOR_)
    # NOw we will print pattern 
    #line
    cv2.line(frame,(0,0),(200+n,300+n),(0,255,0),3)
    # rectangel
    cv2.rectangle(frame,(0,0),(200+n,300+n),(255,0,0),3)
    # circle
    cv2.circle(frame,(200+n,300+n),100,(255,0,0),3)
    #text
    font=cv2.FONT_HERSHEY_SIMPLEX # this font type
    cv2.putText(frame,'Siddhesh',(10,50),font,2,(0,0,255),2,cv2.LINE_AA)     #HELLO or curvyhello
    cv2.namedWindow('live',cv2.WINDOW_NORMAL)
    cv2.imshow('live',frame)
    #cv2.imshow('livegray',grayimg)
    n=n+2
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
