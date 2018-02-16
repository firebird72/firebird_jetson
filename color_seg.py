import cv2
import numpy as np


#Notes:
# shape detection https://www.pyimagesearch.com/2016/02/15/determining-object-color-with-opencv/
# cubic spline,
# cross track that is perpendicular distance b/w location and cubic spline
# cascade controller - heading
#


#TUNING PARAMS
erode_iterations = 2
dilate_iterations = erode_iterations

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cap.set(cv2.CAP_PROP_FPS, 30)
while (1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([5, 150, 100])
    upper_blue = np.array([20, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)
    er_mask = cv2.erode(mask, None, iterations=erode_iterations)
    dl_mask = cv2.dilate(er_mask,None,iterations=dilate_iterations)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('dler_mask', dl_mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()