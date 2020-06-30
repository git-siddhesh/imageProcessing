import cv2
import numpy as np
img  = cv2.imread('dog.jpg')
#b=img.copy()
h,w,_ = img.shape
for i in range(h):
    for j in range(w):
        Blue_,Green_,Red_ = img[i][j]
        I = ((0.3 * 𝑅𝑒𝑑_) + (0.59 * 𝐺𝑟𝑒𝑒𝑛_) + (0.11 * 𝐵𝑙𝑢𝑒_))
        img[i][j] = I
cv2.imshow('aa',img)
cv2.waitKey(0)
cv2.destroyAllWindows()