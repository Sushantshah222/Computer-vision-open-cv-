import cv2
import numpy as np


image = cv2.imread("/home/sushant/Desktop/sample img/number plate/blue_car.jpg")
image = cv2.resize(image,(720,360), interpolation=cv2.INTER_AREA)

cv2.namedWindow('Track')
cv2.resizeWindow('Track', 700, 512)


def track(x):
    pass

cv2.createTrackbar('hue min', 'Track', 0, 179, track)
cv2.createTrackbar('hue max', 'Track', 10, 179, track)
cv2.createTrackbar('sat min', 'Track', 128, 255, track)
cv2.createTrackbar('sat max', 'Track', 255, 255, track)
cv2.createTrackbar('val min', 'Track', 169, 255, track)
cv2.createTrackbar('val max', 'Track', 217, 255, track)

while(1):
    h_min = cv2.getTrackbarPos('hue min', 'Track')
    h_max = cv2.getTrackbarPos('hue max', 'Track')
    s_min = cv2.getTrackbarPos('sat min', 'Track')
    s_max = cv2.getTrackbarPos('sat max', 'Track')
    val_max = cv2.getTrackbarPos('val max', 'Track')
    val_min = cv2.getTrackbarPos('val min', 'Track')

    if cv2.waitKey(1) == ord('s'):
        break




    HSV_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    cv2.imshow('img',image)
    cv2.imshow('img_HSV',HSV_image)

    lv=np.array([h_min,s_min,val_min])
    uv=np.array([h_max,s_max,val_max])

    mask_img = cv2.inRange(HSV_image,lv,uv)
    cv2.imshow('IMG_MASK',mask_img)
    kernal = np.ones((5, 5), np.uint8)
    red_mask = cv2.dilate(mask_img, kernal)
    res_red = cv2.bitwise_and(image, image, mask=red_mask)

    contours,heri = cv2.findContours(mask_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic,contour in enumerate(contours):
        area =cv2.contourArea(contour)
        if area> 300:
            x,y,w,h = cv2.boundingRect(contour)
            image_frame = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
            new_img = image[y:y+h,x:x+w]
cv2.imshow("Cars", image)
cv2.imshow("Number Plate", new_img)
cv2.waitKey()
cv2.destroyAllWindows()