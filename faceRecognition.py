# project prac session 1 

import cv2
#creatin a cascade classifier obj
face_cascade = cv2.CascadeClassifier("faceimg.png")
# Reading the image 
img= cv2.imread('faceimg.png')
#Converting this image to GrayScale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Search the coordinate of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05,minNeighbors=5)
print(type(faces),faces)

for x,y,w,h in faces:
    img = cv2.reactangle(img, (x,y), (x+w,y+h), (0,255,0),3)

cv2.imshow("window",img)
cv2.waitKey(0)
