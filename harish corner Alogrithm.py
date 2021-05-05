import cv2
import numpy as np
from matplotlib import pyplot as plt



cv2.destroyAllWindows()

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    gray_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    gray_image = np.float32(gray_image)

    corners = cv2.cornerHarris(gray_image,2,3,0.04)

    img2 = frame
    corners2 = cv2.dilate(corners, None, iterations=3)
    img2[corners2 > 0.01 * corners2.max()] = [255, 0, 0]

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
