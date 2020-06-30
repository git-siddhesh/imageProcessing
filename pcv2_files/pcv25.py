import os
import numpy as np
import cv2
images_folder_path = os.path.abspath(os.path.join('..', 'Images'))
for image_name in os.listdir(images_folder_path):
    b= np.ones((800,800),np.uint8)*255
    print(image_name)
    img = cv2.imread(images_folder_path+"/"+image_name) 
    new1 = cv2.resize(img, (800,800))
    img2 = cv2.cvtColor(new1,cv2.COLOR_BGR2GRAY)
    ret , thresh2 = cv2.threshold(img2, 180, 255, cv2.THRESH_BINARY)
    con,hier = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#select the desire contour no
    for i in range(4):
        if (len(con[i])>150 and len(con[i])<450):
            k = i
    #cv2.drawContours(new1,con, k, (255,0,0), 3)
# Copy the section to the white 'b' image
    cv2.fillPoly(b, pts =[con[k]], color=(0,0,0))
    
    cv2.imshow("white",b)
    b1 = np.fft.fftshift(img, axes=None)
    cv2.imshow("b1",b1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


''' for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            dist = cv2.pointPolygonTest(con[k],(j,i),True)
            if dist>=0:
                b[i,j] = 0
'''
