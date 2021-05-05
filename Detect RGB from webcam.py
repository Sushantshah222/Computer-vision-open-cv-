'''
Detect the RGB color from a webcam
source: https://www.geeksforgeeks.org/detect-the-rgb-color-from-a-webcam-using-python-opencv/?ref=rp
'''
import cv2
import numpy as np

vid = cv2.VideoCapture(1)


while True:

    # capturing the current frame
    _, frame = vid.read()

    # displaying the current frame
    cv2.imshow("frame", frame)

    # setting values for base colors
    b = frame[:, :, :1]
    g = frame[:, :, 1:2]
    r = frame[:, :, 2:]

    # computing the mean
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)

    # displaying the most prominent color
    if (b_mean > g_mean and b_mean > r_mean):
        print("Blue")
    if (g_mean > r_mean and g_mean > b_mean):
        print("Green")
    else:
        print("Red")

