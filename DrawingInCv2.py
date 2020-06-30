import cv2
import numpy as np 
# creating an empty black screen
img=np.zeros((512,512,3))
cv2.ellipse(img,(255,233),(200,33),0,0,360,100,2)
cv2.imshow('myimg',img)
cv2.waitKey(0)

# creating a white screen image
imgwhite=np.ones((512,512,3))*255
cv2.imshow('myimg2',imgwhite)
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.release()