# to store video
import cv2
cap=cv2.VideoCapture(0)   # to open
# To define video type   or adding plugin
plugin=cv2.VideoWriter_fourcc(*'XVID')
# Now saving video 
output=cv2.VideoWriter('class.avi',plugin,20,(640,480))
output2=cv2.VideoWriter('class.avi',plugin,50,(640,480))  # for speeding up the video+
while cap.isOpened():
    status,frame=cap.read()
    cv2.imshow('live',frame)
    output2.write(frame)    #sending data to Videowriter
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
