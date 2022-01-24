import cv2
import numpy as np
import matplotlib as plt

img = cv2.imread("/home/celeritas/PycharmProjects/opencv/sample_images/arrows/arrow2_left.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Read the image
print(gray.shape)
height = gray.shape[0]
width = gray.shape[1]


# Cut the image in half
width_cutoff = width // 2
s1 = gray[:, :width_cutoff]
s2 = gray[:, width_cutoff:]




corners_1 = cv2.goodFeaturesToTrack(s1, 150, 0.5, 50)
corners_1 = np.int0(corners_1)
corners_2 = cv2.goodFeaturesToTrack(s2, 150, 0.5, 50)
corners_2 = np.int0(corners_2)


number_of_dots_1 = []
number_of_dots_2 = []


for i in corners_1:
    x, y = i.ravel()
    final_1 = cv2.circle(s1,(x,y),5, (0, 0, 255), -1)
    number_of_dots_1.append(len(corners_1))
    cv2.imshow('first part', final_1)

for j in corners_2:
    x, y = j.ravel()
    final_2 = cv2.circle(s2,(x,y),5, (0, 0, 255), -1)
    print(corners_2)
    number_of_dots_2.append(len(corners_2))
    cv2.imshow('second part', final_2)

print(number_of_dots_1)
print(number_of_dots_2)

# cv2.imshow('first part',corners_1)
# cv2.imshow('second part',corners_2)

cv2.waitKey()
cv2.destroyAllWindows()
