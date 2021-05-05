import cv2
import numpy as np

video = cv2.VideoCapture(1)

def nothing():
    pass

cv2.namedWindow('img')
cv2.createTrackbar('quality','img',1,100,nothing)

while True:
    _,frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    quality = cv2.getTrackbarPos('quality','img')
    quality = quality/1000
    corner = cv2.goodFeaturesToTrack(gray,18,0.5,10)
    if corner is not None:
        corner = np.int0(corner)
        for corners in corner:
            x , y = corners.ravel()
            cv2.circle(frame,(x,y),6,(0,0,255),-1)

    k = cv2.waitKey(1)
    if k == 32:
        break
    cv2.imshow('img',frame)
video.release()
cv2.destroyAllWindows()

