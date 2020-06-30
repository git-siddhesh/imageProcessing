import cv2
cap=cv2.VideoCapture(0)

take1=cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2GRAY)
take2=cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2GRAY)
take3=cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2GRAY)

def imgdiff(x,y,z):
    d1=cv2.subtract(x,y)
    d2=cv2.subtract(y,z)
    return(cv2.bitwise_and(d1,d2))

while cap.isOpened():
    cv2.imshow('motion',imgdiff(take1,take2,take3))
    take1=take2
    take2=take3
    take3=cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2GRAY)
    if cv2.waitKey(10) & 0xff == ord('\r'):break

cap.release()
cv2.destroyAllWindows()