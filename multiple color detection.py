'''
Work Flow Description:
Step 1: Input: Capture video through webcam.
Step 2: Read the video stream in image frames.
Step 3: Convert the imageFrame in BGR(RGB color space represented as three matrices of red, green and blue with integer values from 0 to 255) to HSV(hue-saturation-value) color space.
    Hue describes a color in terms of saturation, represents the amount of gray color in that color and value describes the brightness or intensity of the color.
    This can be represented as three matrices in the range of 0-179, 0-255 and 0-255 respectively.
Step 4: Define the range of each color and create the corresponding mask.
Step 5: Morphological Transform: Dilation, to remove noises from the images.
Step 6: bitwise_and between the image frame and mask is performed to specificaly detect that particular color and discrad others.
Step 7: Create contour for the individual colors to display the detected colored region distinguishly.
Step 8: Output: Detection of the colors in real-time.

'''

import cv2
import numpy as np

video=cv2.VideoCapture(1)
while True:
    _,frame = video.read()

    img_HSV= cv2.cvtColor(image,cv2.COLOR_BGR2HSV)


    red_lower = np.array([136,87,111],uint8)
    red_upper = np.array([180,255,255],uint8)
    red_mask = cv2.inRange(img_HSV,red_lower,red_upper)

    blue_lower = np.array([94,80,2],uint8)
    blue_upper = np.array([120,255,255],uint8)
    blue_mask = cv2.inRange(img_HSV,blue_lower,blue_upper)

    green_lower = np.array([25,52,72],uint8)
    green_upper = np.array([102,255,255],uint8)
    green_mask = cv2.inRange(img_HSV,green_lower,green_upper)

    kernel = np.ones((5, 5), "uint8")


    red_mask = cv2.dilate(red_mask,kernel)
    res_red = cv2.bitwise_and(image,image,mask=red_mask)

    blue_mask = cv2.dilate(blue_mask,kernel)
    res_blue = cv2.bitwise_and(image,image,mask=blue_mask)

    green_mask = cv2.dilate(green_mask,kernel)
    res_green = cv2.bitwise_and(image,image,mask=green_mask)

    #
    # # creating countour to track red color
    # contours, hierachy = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #
    # for i, contour in enumerate(contours):
    #     area = cv2.contourArea(contour)
    #     if (area > 300):
    #         x,y,w,h = cv2.boundingRect(contour)
    #         image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    #         cv2.putText(image,"Red Colour",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255))
    #
    #
    #
    # # creating countour to track blue color
    # contours, hierachy = cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #
    # for i, contour in enumerate(contours):
    #     area = cv2.contourArea(contour)
    #     if (area > 300):
    #         x,y,w,h = cv2.boundingRect(contour)
    #         image = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    #         cv2.putText(image,"Blue Colour",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
    #
    #
    # # creating countour to green red color
    # countours, hierachy = cv2.findContours(green_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #
    # for i, contour in enumerate(contours):
    #     area = cv2.contourArea(contour)
    #     if (area >300):
    #         x,y,w,h = cv2.boundingRect(contour)
    #         image = cv2.rectangle(image,(x,y),(x+h,y+w),(0,255,0),2)
    #         image = cv2.putText(image,"Green Colour",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0))
    #
    # cv2.imshow("Multiple Color Detection in Real-TIme", image)
    # if cv2.waitKey(10) & 0xFF == ord('q'):
    #     cap.release()
    #     cv2.destroyAllWindows()
    #     break
    #
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            image = cv2.rectangle(image, (x, y),
                                       (x + w, y + h),
                                       (0, 0, 255), 2)

            cv2.putText(image, "Red Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))

            # Creating contour to track green color
    contours, hierarchy = cv2.findContours(green_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            image = cv2.rectangle(image, (x, y),
                                       (x + w, y + h),
                                       (0, 255, 0), 2)

            cv2.putText(image, "Green Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 255, 0))

            # Creating contour to track blue color
    contours, hierarchy = cv2.findContours(blue_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            image = cv2.rectangle(image, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 0), 2)

            cv2.putText(image, "Blue Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 0, 0))

            # Program Termination
    cv2.imshow("Color Detection ", image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break


#
# # working code
# import numpy as np
# import cv2
#
# webcam = cv2.VideoCapture(1)
#
# while (True):
#
#
#     _,imageFrame = webcam.read()
#
#
#     hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
#
#
#     red_lower = np.array([136, 87, 111], np.uint8)
#     red_upper = np.array([180, 255, 255], np.uint8)
#     red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
#
#     green_lower = np.array([25, 52, 72], np.uint8)
#     green_upper = np.array([102, 255, 255], np.uint8)
#     green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
#
#
#     blue_lower = np.array([94, 80, 2], np.uint8)
#     blue_upper = np.array([120, 255, 255], np.uint8)
#     blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
#
#     kernal = np.ones((5, 5), "uint8")
#
#     red_mask = cv2.dilate(red_mask, kernal)
#     res_red = cv2.bitwise_and(imageFrame, imageFrame,
#                               mask=red_mask)
#
#     green_mask = cv2.dilate(green_mask, kernal)
#     res_green = cv2.bitwise_and(imageFrame, imageFrame,
#                                 mask=green_mask)
#
#     blue_mask = cv2.dilate(blue_mask, kernal)
#     res_blue = cv2.bitwise_and(imageFrame, imageFrame,
#                                mask=blue_mask)
#
#     contours, hierarchy = cv2.findContours(red_mask,
#                                            cv2.RETR_TREE,
#                                            cv2.CHAIN_APPROX_SIMPLE)
#
#     for pic, contour in enumerate(contours):
#         area = cv2.contourArea(contour)
#         if (area > 300):
#             x, y, w, h = cv2.boundingRect(contour)
#             imageFrame = cv2.rectangle(imageFrame, (x, y),
#                                        (x + w, y + h),
#                                        (0, 0, 255), 2)
#
#             cv2.putText(imageFrame, "Red Colour", (x, y),
#                         cv2.FONT_HERSHEY_SIMPLEX, 1.0,
#                         (0, 0, 255))
#
#     contours, hierarchy = cv2.findContours(green_mask,
#                                            cv2.RETR_TREE,
#                                            cv2.CHAIN_APPROX_SIMPLE)
#
#     for pic, contour in enumerate(contours):
#         area = cv2.contourArea(contour)
#         if (area > 300):
#             x, y, w, h = cv2.boundingRect(contour)
#             imageFrame = cv2.rectangle(imageFrame, (x, y),
#                                        (x + w, y + h),
#                                        (0, 255, 0), 2)
#
#             cv2.putText(imageFrame, "Green Colour", (x, y),
#                         cv2.FONT_HERSHEY_SIMPLEX,
#                         1.0, (0, 255, 0))
#
#             # Creating contour to track blue color
#     contours, hierarchy = cv2.findContours(blue_mask,
#                                            cv2.RETR_TREE,
#                                            cv2.CHAIN_APPROX_SIMPLE)
#     for pic, contour in enumerate(contours):
#         area = cv2.contourArea(contour)
#         if (area > 300):
#             x, y, w, h = cv2.boundingRect(contour)
#             imageFrame = cv2.rectangle(imageFrame, (x, y),
#                                        (x + w, y + h),
#                                        (255, 0, 0), 2)
#
#             cv2.putText(imageFrame, "Blue Colour", (x, y),
#                         cv2.FONT_HERSHEY_SIMPLEX,
#                         1.0, (255, 0, 0))
#
#     cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         cap.release()
#         cv2.destroyAllWindows()
#         break