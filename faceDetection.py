import cv2

casclf=cv2.CascadeClassifier('harcascade.xml')
cap=cv2.VideoCapture(0)
while cap.isOpened():
    status,frame=cap.read()
    # now we can apply classifier to live frame
    face=casclf.detectMultiScale(frame,1.13,5)  # classifier tuning parameter
    #print(face)      # [[x,y,height,width]]
    for x,y,h,w in face:
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),4)
        facedata=frame[x:x+h,y:y+w]
        #cv2.imshow('face',facedata)
    cv2.imshow('face',frame)
    if cv2.waitKey(10) & 0xff == ord('\r'):break
cv.destroyAllWindows()
cap.release()



# for more accuracy use LBPH algo 

# in deep learning     dlib library is used 
#        dlib use much cpu and gpu  9
#     face-recognisation 

# we can also use API 
#   world most power full API KAIROS

# YOU ONLY LOOK ONCE technique



# another one is AMAZON REKOGNITION 