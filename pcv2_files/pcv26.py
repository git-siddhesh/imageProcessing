import cv2
import cv2.aruco as arc
import numpy as np
ardict1 = arc.Dictionary_get(arc.DICT_5X5_50)
img = arc.drawMarker(ardict1,25,400)
b= np.ones((800,800),np.uint8)*255
b[200:600,200:600] = img
# cv2.imshow("aa1",b)
avging = cv2.blur(b,(10,10))
cv2.imshow("original",avging)
kernel = np.array([[1,1,1], [1,7,1], [1,1,1]])
im = cv2.filter2D(avging, -1, kernel) 
cv2.imshow("sadas",im)
'''img1= cv2.imread("test.jpg")
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.imshow('Blurr',img1)
#new = cv2.Laplacian(b, cv2.CV_64F).var()
#b2 = cv2.bilateralFilter(b,9,75,75)
img = cv2.convertScaleAbs(img1,1,2)
cv2.imshow("deblur",img)

#print(new)
'''
'''
_,th3 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
a = cv2.aruco.detectMarkers(th3,ardict1)
p1x = int(a[0][0][0][0][0])
p1y = int(a[0][0][0][0][1])
p2x = int(a[0][0][0][2][0])
p2y = int(a[0][0][0][2][1])
cv2.rectangle(img,(p1x,p1y),(p2x,p2y),(255,0,0),3)
cv2.imshow('Noise Filtered Image', th3)
cv2.imshow("dsgjhf",img)'''
cv2.waitKey(0)
cv2.destroyAllWindows()





'''
import cv2
import numpy as np

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
'''