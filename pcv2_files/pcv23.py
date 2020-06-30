import cv2
import numpy as np
img  = cv2.imread('dog.jpg')
'''print(img.shape)
a=[1,2]
ar = np.asarray(a)
print(type(img[0][0]))

for i in range(223):
    for j in range(226):
       a[i][j]=img[i][j]
np.append(ar,3+)
print(ar)
#img_height, img_width = 300, 300
#n_channels = 4
#transparent_img = np.zeros((img_height, img_width, n_channels), dtype=np.uint8)

# Save the image for visualization

#cv2.imshow("fdfdf",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.imwrite("./transparent_img.png", transparent_img)

image = cv2.imread('dog.jpg')
overlay = image.copy()
x, y, w, h = 10, 10, 100, 100  # Rectangle parameters
#cv2.rectangle(overlay, (x, y), (x+w, y+h), (0, 200, 0), -1)  # A filled rectangle
alpha = 0.5 # Transparency factor.
# Following line overlays transparent rectangle over the image
image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
cv2.imshow("sf",image_new)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

b = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
print(b[0][0][3])
for i in range(b.shape[0]):
    for j in range(b.shape[1]):
       bl,g,r,a=b[i][j]
       a = int(255/2)
       b[i,j]=bl,g,r,a
cv2.imwrite('dog.png',b)
img1  = cv2.imread('dog.png')
cv2.imshow('transp 0.5',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()