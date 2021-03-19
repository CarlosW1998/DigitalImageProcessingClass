# import the necessary packages
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2


images = []

images.append(cv2.imread('01_suburbA.jpg'))
images.append(cv2.imread('01_suburbB.jpg'))

print("[INFO] stitching images...")
stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

if status == 0:
	cv2.imshow("Stitched", stitched)
	cv2.waitKey(0)

else:
	print("[INFO] image stitching failed ({})".format(status))