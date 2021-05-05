'''using.html
source :https://art-of-electronics.blogspot.com/2019/11/object-detection-and-tracking-using.html
'''


import cv2
import numpy as np


cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX                ##Font style for writing text on video frame
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)        ##Set camera resolution
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
Kernal = np.ones((3, 3), np.uint8)
#create a window
cv2.namedWindow('Track')
cv2.resizeWindow('Track', 700, 512)

#trackbar
def track(x):
    pass

cv2.createTrackbar('hue min', 'Track', 3, 179, track)
cv2.createTrackbar('hue max', 'Track', 80, 179, track)
cv2.createTrackbar('sat min', 'Track', 118, 255, track)
cv2.createTrackbar('sat max', 'Track', 255, 255, track)
cv2.createTrackbar('val min', 'Track', 144, 255, track)
cv2.createTrackbar('val max', 'Track', 255, 255, track)


while(1):
    ret, frame = cap.read()         ##Read image frame
    frame = cv2.flip(frame, +1)     ##Mirror image frame
    if not ret:                     ##If frame is not read then exit
        break
    h_min = cv2.getTrackbarPos('hue min', 'Track')
    h_max = cv2.getTrackbarPos('hue max', 'Track')
    s_min = cv2.getTrackbarPos('sat min', 'Track')
    s_max = cv2.getTrackbarPos('sat max', 'Track')
    val_max = cv2.getTrackbarPos('val max', 'Track')
    val_min = cv2.getTrackbarPos('val min', 'Track')

    if cv2.waitKey(1) == ord('s'):  ##While loop exit condition
        break

    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)         ##BGR to HSV
    lb = np.array([h_min, s_min, val_min])
    ub = np.array([h_max, h_max, val_max])

    mask = cv2.inRange(frame2, lb, ub)                      ##Create Mask
    cv2.imshow('Masked Image', mask)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, Kernal)        ##Morphology
    cv2.imshow('Opening', opening)

    res = cv2.bitwise_and(frame, frame, mask= opening)             ##Apply mask on original image
    cv2.imshow('Resuting Image', res)

    contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE,      ##Find contours
                                           cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0:
        cnt = contours[0]
        M = cv2.moments(cnt)
        Cx = int(M['m10']/M['m00'])
        Cy = int(M['m01'] / M['m00'])
        S = 'Location of object:' + '(' + str(Cx) + ',' + str(Cy) + ')'
        cv2.putText(frame, S, (5, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.drawContours(frame, cnt, -1, (0, 255, 0), 3)
    ##Lets Detect a red ball
    cv2.imshow('Original Image', frame)

cap.release()                   ##Release memory
cv2.destroyAllWindows()         ##Close all the windows
