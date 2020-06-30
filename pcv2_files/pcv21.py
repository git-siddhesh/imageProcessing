'''import cv2
import csv
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('..\HandGesture\dog.jpg')
cv2.imshow('image',img)
dim = img.shape
color = img[int(dim[1]/2),int(dim[0]/2)]
print("color",color)
#print("blue ",b," Green ",g," Red ",r)
#img2= img
#img2[int(dim[1]/2),int(dim[0]/2)] = (0,0,255)
#cv2.imshow('image',img2)
import numpy
a =[['csv',str(dim[0]),str(dim[1]),str(dim[2]),str(color[0]),str(color[1]),str(color[2])]]
with open("output.csv", "w") as f:
    for row in a:
        f.write("%s\n" % ','.join(str(col) for col in row))
#numpy.savetxt("foo.csv", a, delimiter=",")
#print("name, height, width, xyz, Blue, Green, Red\n")
#print("dog",dim[0],dim[1],dim[2],color[0],color[1],color[2])
print(a)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
import cv2
import numpy as np
img = cv2.imread('..\HandGesture\dog.jpg')
dim = img.shape
color = img[int(dim[1]/2),int(dim[0]/2)]
a =[['bird.jpg',str(dim[0]),str(dim[1]),str(dim[2]),str(color[0]),str(color[1]),str(color[2])]]
with open("output.csv", "w") as f:
    for row in a:
        f.write("%s\n" % ','.join(str(col) for col in row))
