# import numpy as np
# import cv2 as cv
#
# def nothing(x):
#     print(x)
#
# # Create a black image, a window
# img = np.zeros((300,512,3), np.uint8)
# cv.namedWindow('image')
#
# cv.createTrackbar('B', 'image', 0, 255, nothing)
# cv.createTrackbar('G', 'image', 0, 255, nothing)
# cv.createTrackbar('R', 'image', 0, 255, nothing)
#
# switch = '0 : OFF\n 1 : ON'
# cv.createTrackbar(switch, 'image', 0, 1, nothing)
#
# while(1):
#     cv.imshow('image',img)
#     k = cv.waitKey(1) & 0xFF
#     if k == 27:
#         break
#
#     h = cv.getTrackbarPos('B', 'image')
#     s = cv.getTrackbarPos('G', 'image')
#     v = cv.getTrackbarPos('R', 'image')
#     switchs = cv.getTrackbarPos(switch, 'image')
#
#     if switchs == 0:
#        img[:] = 0
#     else:
#        img[:] = [h, s, v]
#
#
# cv.destroyAllWindows()

'''
trackbar for video.
source:http://allinonecode.pythonanywhere.com/Trac/
https://www.youtube.com/watch?v=WUFJu-rJNdQ
'''

import cv2
import numpy as np

#create a window
cv2.namedWindow('Track')
cv2.resizeWindow('Track', 700, 512)

#trackbar
def track(x):
    pass

cv2.createTrackbar('hue min', 'Track', 87, 179, track)
cv2.createTrackbar('hue max', 'Track', 103, 179, track)
cv2.createTrackbar('sat min', 'Track', 103, 255, track)
cv2.createTrackbar('sat max', 'Track', 244, 255, track)
cv2.createTrackbar('val min', 'Track', 63, 255, track)
cv2.createTrackbar('val max', 'Track', 213, 255, track)


while True:
    h_min = cv2.getTrackbarPos('hue min', 'Track')
    h_max = cv2.getTrackbarPos('hue max', 'Track')
    s_min = cv2.getTrackbarPos('sat min', 'Track')
    s_max = cv2.getTrackbarPos('sat max', 'Track')
    val_max = cv2.getTrackbarPos('val max', 'Track')
    val_min = cv2.getTrackbarPos('val min', 'Track')
    print(f'HUE MIN : {h_min} HUE MAX : {h_max} SAT MIN : {s_min} SAT MAX : {s_max} VAL MIN : {val_min} VAL MAX : {val_max}')
    if cv2.waitKey(1) &0xFF == ord('q'):
        break