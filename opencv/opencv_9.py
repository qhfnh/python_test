# SIFT 算法
import cv2
import numpy as np
img = cv2.imread('asd.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(cv2.__version__)
sift = cv2.SIFT_create()
kp = sift.detect(gray, None)
img = cv2.drawKeypoints(gray, kp, img)
cv2.imshow("sd", img)
cv2.waitKey(0)
cv2.destroyAllWindows()