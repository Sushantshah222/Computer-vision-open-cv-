import numpy as np
import cv2


image = cv2.imread("/home/sushant/Desktop/sample img/number plate/blue_car.jpg")
image = cv2.resize(image,(800,800))


hsvFrame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

red_lower = np.array([0, 128, 169], np.uint8)
red_upper = np.array([10, 255, 217], np.uint8)


red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
kernal = np.ones((5, 5), "uint8")
red_mask = cv2.dilate(red_mask, kernal)
res_red = cv2.bitwise_and(image, image, mask=red_mask)

contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if area > 3000:
        x, y, w, h = cv2.boundingRect(contour)
        imageFrame = cv2.rectangle(image, (x-10, y-10),(x + w+10, y + h+10),(0, 255, 0), 2)
        cv2.putText(imageFrame, "Number Plate", (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0,255))
        new_img = image[y:y + h, x:x + w]
cv2.imshow("Cars", image)
cv2.imshow("Number Plate", new_img)
cv2.waitKey(0)
cv2.destroyWindow()





