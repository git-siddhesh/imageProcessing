import cv2
import numpy as np
import math
list=[]
list1=[]

img = cv2.imread(r'C:\Users\siddhesh\Downloads\task1#sb\Task1.1\Images\image_3.png',0)
#img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#height,width,channel=cimg.shape

circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,20,
                            param1=5,param2=51,minRadius=1,maxRadius=26)
 
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
   
    
#x,y,r=print(circles)
list.append(circles)
print(list)
for i in range(0,2):
    for j in range(0,3):
        list1.append(list[0][0][i][j])
print(list1)

#slope1=(int(height/2)-list1[1])/(int(width/2)-list1[0])
#slope2=(int(height/2)-list1[4])/(int(width/2)-list1[3])
del list1[2]
del list1[4]
x = [list1[0],list1[2]]
y = [list1[1],list1[3]]


val = (y[0]**2 + x[0]**2 + y[0]**2 + x[0]**2 -(y[1]-y[0])**2 - (x[1]-x[0])**2)/(2*(((y[1]**2+x[1])**2) *(y[0]**2+x[0])**2)**(1/2))

angle=math.degrees(math.acos(val))

'''
#let the center of the image as origin
# cal the new value of point 1 and 2 wrt origin
for i in range(2):
    x[i] = x[i]-int(width/2)
for i in range(2):
    y[i] = int(height/2)-y[i]
list1=[x[0],y[0],x[1],y[1]]
print(list1)
slope1= y[0]/x[0]
slope2= y[1]/x[1]
'''

value=(slope2-slope1)/(1+slope1*slope2)
angle=math.degrees(math.atan(value))
'''if(angle<0):
    angle = 180+angle
print(angle)'''
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
  
