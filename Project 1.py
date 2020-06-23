import cv2
import numpy as np
framewidth=1040
frameheight=440
cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,150)

colors=[[31,86,136,255,255,255],
        [0,130,233,255,255,255],
        [29,59,117,255,255,212]]
co=[[0,255,0],
    [0,255,0],
    [0,255,0]]
myPoints=[]
def findC(img,colors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count=0
    newPt=[]
    for col in colors:
        lower = np.array(col[0:3])
        upper = np.array(col[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y=getC(mask)
        cv2.circle(imgResult,(int(x),int(y)),10,co[count],cv2.FILLED)
        cv2.imshow(str(col[0]),mask)
        if x!=0 and y!=0:
            newPt.append([x,y,count])
        count+=1
    return newPt
def getC(img):
    cunt,heri=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cn in cunt:
        area=cv2.contourArea(cn)
        if area>500:
            cv2.drawContours(imgResult,cn,-1,(255,0,0),3)
            peri=cv2.arcLength(cn,True)
            approx=cv2.approxPolyDP(cn,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
    return x+w/2,y

def Draw(pts,cval):
    for pt in pts:
        cv2.circle(imgResult, (int(pt[0]), int(pt[1])), 10, co[pt[2]], cv2.FILLED)

while True:

    success, img = cap.read()
    if img is None:
        break
    imgResult=img.copy()
    newPt=findC(img, colors)
    if len(newPt)!=0:
        for newp in newPt:
            myPoints.append(newp)
    if len(myPoints)!=0:
        Draw(myPoints,co)
    cv2.imshow("r",imgResult)
    if cv2.waitKey(1) & 0xFF ==ord('s'):
        break