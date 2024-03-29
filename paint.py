import cv2
import numpy as np
framewidth=1040
frameheight=440
cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,150)

with open('values.txt') as f:
    values = f.read().splitlines()
values = [int(i) for i in values]

color_array = [[133, 255, 158],
               [166, 244, 220],
               [175, 144, 169],
               [160, 92, 123],
               [148, 70, 84]]

counter = 0

colors=[values]
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
            cv2.drawContours(imgResult,cn,-1,(255,255,255),3)
            peri=cv2.arcLength(cn,True)
            approx=cv2.approxPolyDP(cn,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
    return x+w/2,y

def Draw(pts,cval,color):
    for pt in pts:
        cv2.circle(imgResult, (int(pt[0]), int(pt[1])), 8, color, cv2.FILLED)

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
        Draw(myPoints,co,color_array[ counter % len(color_array) ])
    cv2.imshow("r",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('s') or cv2.waitKey(1) & 0xFF == ord('S'):
        break
    elif cv2.waitKey(1) == ord('c') or cv2.waitKey(1) == ord('C'):
        myPoints = []
    elif cv2.waitKey(1) == ord('q') or cv2.waitKey(1) == ord('Q'):
        counter += 1
