import cv2
import numpy as np
img= np.zeros((1024,1024),np.uint8)
cv2.imshow('image',img)

img1=255-img
cv2.imshow('White',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()