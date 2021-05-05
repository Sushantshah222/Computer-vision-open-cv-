import cv2,time

img = cv2.imread('/home/celeritas/PycharmProjects/opencv/sample_images/arrows/arrow2_left.png')
img2 = img

height, width, channels = img.shape
# Number of pieces Horizontally
CROP_W_SIZE  = 3
# Number of pieces Vertically to each Horizontal
CROP_H_SIZE = 2

for ih in range(CROP_H_SIZE ):
    for iw in range(CROP_W_SIZE ):

        x = width/CROP_W_SIZE * iw
        y = height/CROP_H_SIZE * ih
        h = (height / CROP_H_SIZE)
        w = (width / CROP_W_SIZE )
        print(x,y,h,w)
        img = img[y:y+h, x:x+w]



        NAME = str(time.time())
        cv2.imwrite("CROP/" + str(time.time()) +  ".png",img)
        img = img2