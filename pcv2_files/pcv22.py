import cv2
import numpy as np
img  = cv2.imread('dog.jpg')
b=img.copy()
# set blue and green channels to 0
b[:, :, 0] = 0
b[:, :, 1] = 0
cv2.imshow('image',img)
cv2.imshow('image',b)
cv2.imwrite('R-RGB.jpg',b)
cv2.waitKey(0)
cv2.destroyAllWindows()

#image = img.copy()
#cv2.imshow('R-RGB',image[:, :, 2])
#cv2.imwrite('R-RGB.jpg',image[:, :, 2])
#cv2.waitKey(0)
#cv2.destroyAllWindows()


