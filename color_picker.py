import cv2
import numpy as np
framewidth=640
frameheight=240
cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,150)

def emp(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("h min","HSV",0,255,emp)
cv2.createTrackbar("h max","HSV",0,255,emp)
cv2.createTrackbar("s min","HSV",0,255,emp)
cv2.createTrackbar("s max","HSV",0,255,emp)
cv2.createTrackbar("v min","HSV",0,255,emp)
cv2.createTrackbar("v max","HSV",0,255,emp)
cap=cv2.VideoCapture(0)

while True:
    _, img=cap.read()
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("h min", "HSV")
    h_max = cv2.getTrackbarPos("h max", "HSV")
    s_min = cv2.getTrackbarPos("s min", "HSV")
    s_max = cv2.getTrackbarPos("s max", "HSV")
    v_min = cv2.getTrackbarPos("v min", "HSV")
    v_max = cv2.getTrackbarPos("v max", "HSV")
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    result=cv2.bitwise_and(img,img,mask=mask)

    mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    hstack=np.hstack([img,mask,result])
    cv2.imshow("1",hstack)

    if cv2.waitKey(1) & 0xFF ==ord('s'):
        break
cap.release()
cv2.destroyAllWindows()




