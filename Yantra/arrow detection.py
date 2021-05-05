import numpy as np
import cv2

path = '/home/celeritas/PycharmProjects/opencv/sample_images/arrows/arrow2_left.png'
gray = cv2.imread(path, 0)
print(gray)

# global thresholding
ret1, thresholding1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Otsu's thresholding
ret2, thresholding2 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
# Otsu's thresholding after gussian filter
Gussian_gray = cv2.GaussianBlur(gray, (5, 5), 0)
ret3, thresholding3 = cv2.threshold(Gussian_gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)

#morphological transform
kernel = np.ones((5,5),np.uint8)

image = cv2.morphologyEx(thresholding3,cv2.MORPH_OPEN,kernel)
# Display the resulting frame
# cv2.imshow('grayscale', gray)
# cv2.imshow('binary', thresholding1)
# cv2.imshow('Otsu+binary', thresholding2)
cv2.imshow('Gussian + Otsu+binary', thresholding3)
cv2.imshow('morphological', image)



cv2.waitKey(0)
cv2.destroyAllWindows()
