#############################################
# Universidad Tecnica Particular de Loja    #
#############################################
# Professor:                                #
# Rodrigo Barba        lrbarba@utpl.edu.ec  #
#############################################
# Students:                                 #
# Marcelo Bravo        mdbravo4@utpl.edu.ec #
# Galo Celly           gscelly@utpl.edu.ec  #
# Nicholas Earley      nearley@utpl.edu.ec  #
#############################################

#!/bin/hbpython

#import libraries
import cv2
import numpy as np


#We define the mask
def mkmask(img, roi_corners):
    mask = np.zeros(img.shape, dtype=np.uint8)
    # roi_corners = np.array([[(10,10), (300,300), (10,300)]], dtype=np.int32)
    white = (255, 255, 255)
    cv2.fillPoly(mask, roi_corners, white)
    return mask

#We define the mask
def mkmask(w, h, c, roi_corners):
    mask = np.zeros((h, w, c), dtype=np.uint8)
    # roi_corners = np.array([[(10,10), (300,300), (10,300)]], dtype=np.int32)
    white = (255, 255, 255)
    cv2.fillPoly(mask, roi_corners, white)
    return mask

#We define the mask
def mkmask(w, h, roi_corners):
    mask = np.zeros((h, w), dtype=np.uint8)
    # roi_corners = np.array([[(10,10), (300,300), (10,300)]], dtype=np.int32)
    white = (255, 255, 255)
    cv2.fillPoly(mask, roi_corners, white)
    return mask


def applymask(img, msk):
    return cv2.bitwise_and(img, msk)

#we define the mask (video)
#for exit or continued the detecction, prees q
if __name__ == "__main__":
    camera = cv2.VideoCapture(0)
    (grabbed, frame) = camera.read()
    if not grabbed:
        exit(0)
    msk = mkmask(frame, np.array([[(200, 100), (500, 100), (700, 300), (500, 700)]], dtype=np.int32))
    while True:
        (grabbed, frame) = camera.read()
        if not grabbed:
            exit(0)
        cv2.imshow("Video - Original", frame)
        mskd = applymask(frame, msk)
        cv2.imshow("Video - Masked", mskd)
        cv2.imshow("Mask", msk)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break