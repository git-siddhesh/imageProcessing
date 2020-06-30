# take image of github opeencv link from tony   
# motion detector
import cv2
cap=cv2.VideoCapture(0)
# frame
take1=cap.read()[1]
take2=cap.read()[1]
take3=cap.read()[1]
# to avoid change in color 
'''
gray1=cv2.cvtColor(take1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(take2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(take3,cv2.COLOR_BGR2GRAY)
#print(cv2.subtract(gray1,gray2))
# now creating image difference
'''
'''def img_diff(x,y,z):
    d1=cv2.subtract(x,y)
    d2=cv2.subtract(y,z)
'''
def img_diff(x,y,z):
    d1=cv2.absdiff(x,y)
    d2=cv2.absdiff(y,z)
    finalimg=cv2.bitwise_and(d1,d2)
    return finalimg

while cap.isOpened():
    status,frame=cap.read()
    motionimg=img_diff(gray1,gray2,gray3)
    # REPLACING IMAGE FRAME
    gray1=gray2
    gray2=gray3
    gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    
    cv2.imshow('live',gray3)    
    cv2.imshow('motion',motionimg)
    if cv2.waitKey(10) & 0xff == ord('\r'):break
cv2.destroyAllWindows()
cap.release()