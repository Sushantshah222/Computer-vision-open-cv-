import cv2
import numpy as np
#
# cap= cv2.VideoCapture(1);
# print(cap.isOpened())
# while(cap.isOpened()):
#     ret,frame=cap.read()
#
#     print(cap.get(cv2.CAP_PROP_SETTINGS))
#
#     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow('Sushant',gray)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()


#
# img= cv2.imread('RGB_color.jpg',1)
#
#
# img=cv2.line(img,(0,0),(255,255),(255,0,0),5)
# img=cv2.rectangle(img,(193,324),(549,519),(0,0,0),5)
#
#
# cv2.imshow("color",img)
# cv2.waitKey(15000)
# cv2.destroyAllWindows()
# #
#
# #

def click_event(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text= str(x)+','+str(y)
        cv2.putText(first_frame,text,(x,y),font,1,(255,255,0),2)
        cv2.imshow('Coordinate',first_frame)

video = cv2.VideoCapture("/home/sushant/PycharmProjects/opencv/sample_images/c_book.mp4")
_,first_frame = video.read()

cv2.imshow('Coordinate',first_frame)

cv2.setMouseCallback('Coordinate',click_event)
cv2.waitKey()
video.release()
cv2.destroyAllWindows()













