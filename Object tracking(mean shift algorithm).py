import cv2
import numpy as np

video = cv2.VideoCapture("/home/sushant/PycharmProjects/opencv/sample_images/c_book.mp4")
_,first_frame = video.read()

# roi = first_frame[243:144,414:398]
roi = first_frame[242:145,415,400]
print(roi)
cv2.imshow('rot',first_frame)
cv2.imshow('roit',roi)
# while True:
#     _,frame = video.read()
#     # cv2.imshow('Frame',frame)
#
#
#     key = cv2.waitKey(60)
#     if key == 32:
#         break
cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()