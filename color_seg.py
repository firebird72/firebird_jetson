import cv2
import numpy as np
import time

#Notes:
# shape detection https://www.pyimagesearch.com/2016/02/15/determining-object-color-with-opencv/
# cubic spline,
# cross track that is perpendicular distance b/w location and cubic spline
# cascade controller - heading
#


#TUNING PARAMS
erode_iterations = 2
dilate_iterations = 5

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cap.set(cv2.CAP_PROP_FPS, 30)
# CANNOT GET WHITE BALANCE WORKING IN OPENCVre
# IN V4L2UCP set whitebalance auto - off, update color temp
# TODO research if I can do this cmd line and just run init calls during setup

# white = cap.get(cv2.CAP_PROP_XI_AUTO_WB)
# cap.set(cv2.CAP_PROP_XI_AUTO_WB,1.0)
# white2 = cap.get(cv2.CAP_PROP_XI_AUTO_WB)
# red = cap.get(cv2.CAP_PROP_WHITE_BALANCE_RED_V)

record_images = True
read_camera = True

while (1):
    # Take each frame
    if read_camera:
        _, frame = cap.read()
    else:
        frame = cv2.imread(' ')
    if record_images:
        import os
        image_dir = 'images'
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
        cv2.imwrite(os.path.join(image_dir,str(time.time()) + ".png"), frame)
        cv2.imshow('frame', frame)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    else:
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

        # HARD TO TWEAK JUNK, leaving in for now.

        # noise removal
        # kernel = np.ones((3, 3), np.uint8)
        # opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=7)
        #
        # # sure background area
        # sure_bg = cv2.dilate(opening, kernel, iterations=3)
        #
        # # Finding sure foreground area
        # dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
        # ret, sure_fg = cv2.threshold(dist_transform, 0.2 * dist_transform.max(), 255, 0)
        #
        # # Finding unknown region
        # sure_fg = np.uint8(sure_fg)
        # unknown = cv2.subtract(sure_bg, sure_fg)

        # compute the exact Euclidean distance from every binary
        # pixel to the nearest zero pixel, then find peaks in this
        # distance map


        #################### Code dump 2 -- WATERSHED
        # D = ndimage.distance_transform_edt(thresh)
        # localMax = peak_local_max(D, indices=False, min_distance=20,
        #                           labels=thresh)
        #
        # # perform a connected component analysis on the local peaks,
        # # using 8-connectivity, then appy the Watershed algorithm
        # markers = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
        # labels = watershed(-D, markers, mask=thresh)
        #

        # ############## BLOB DETECTION
        # # Set up the detector with default parameters.
        # params = cv2.SimpleBlobDetector_Params()
        # params.filterByInertia = False
        # params.filterByConvexity = False
        # detector = cv2.SimpleBlobDetector(params)
        #
        #
        import cv2


        # load the image, convert it to grayscale, blur it slightly,
        # and threshold it
        # find contours in the thresholded image
        cnts = cv2.findContours(dl_mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[1]
        image = frame.copy()
        # loop over the contours
        for c in cnts:
            # compute the center of the contour
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])


            # draw the contour and center of the shape on the image
            cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
            cv2.putText(image, "center", (cX - 20, cY - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Detect blobs.
        #keypoints = detector.detect(dl_mask)

        # Draw detected blobs as red circles.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
        #im_with_keypoints = cv2.drawKeypoints(dl_mask, keypoints, np.array([]), (0, 0, 255),
        #                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # Show keypoints
        #cv2.imshow("Keypoints", im_with_keypoints)
        cv2.imshow('mask', mask)
        cv2.imshow('im_with_keypoints', image)
        cv2.imshow('dl_mask', dl_mask)
        #cv2.imshow('sure_fg', sure_fg)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
cv2.destroyAllWindows()