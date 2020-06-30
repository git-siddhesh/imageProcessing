import cv2
import numpy as np
img = cv2.imread("lena.jpg")
'''r,c,ch = img.shape
img[120:125,350:355] = [255,0,0]
img[120:125,990:995] = [255,0,0]
img[620:625,120:125] = [255,0,0]
img[620:625,1150:1155] = [255,0,0]

pts1 = np.float32([[120,350],[620,120],[120,890],[620,1150]])
pts2 = np.float32([[0,0],[500,0],[0,100
0],[500,1000]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(1000,1000))'''

gamma = 0.8
res2 = cv2.convertScaleAbs(img,2.5,1.5)
loookuptable = np.empty((1,256),np.uint8)
for i in range(256):
    loookuptable[0,i] = np.clip(pow(i/255.0,gamma)*255.0,0,255)
res = cv2.LUT(res2,loookuptable)

cv2.imshow("alphabeta",res2)
cv2.imshow("original",img)
cv2.imshow("gamma correction",res)
cv2.waitKey(0)
cv2.destroyAllWindows()