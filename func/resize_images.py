import cv2

def resize_image(path):
    image = cv2.imread(path)
    print(image.shape)
    scale_percent = 60  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    print('Resized Dimensions : ', resized.shape)

    return resized

# cv2.imshow("Resized image", resized)

resize_image('/home/celeritas/PycharmProjects/opencv/sample_images/aehemad.jpg')

cv2.waitKey()
cv2.destroyAllWindows()



