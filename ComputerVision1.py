import numpy as np 
import cv2
from pynput import mouse
i=0
def on_click(x,y,button,pressed):
    if pressed==True :
        
        
    if not pressed:
        return False
img = cv2.imread("imgs.jpeg")
img2 = cv2.imread("img2.png")
blank=np.zeros((512,512))
#cv2.namedWindow("Instruction",cv2.WINDOW_NORMAL)
#cv2.resizeWindow("window1",400,300)
cv2.putText(blank,"Select and drag for filp the part",(10,50),cv2.FONT_HERSHEY_SIMPLEX,4,(255,0,0),2)
cv2.imshow('instruction',blank)
cv2.waitKey(100)
cv2.destroyWindow('instruction')
cv2.imshow("image",img)
with mouse.Listener(on_click=on_click) as l:
    l.join()

mouse.Listener.CLICK_BUTTONS
img3 = cv2.flip(img[150:450,650:1000],1)
img[150:450,650:1000]=img3
cv2.imshow("window1",img)
cv2.waitKey(0)
#cropimg1 = img[]



