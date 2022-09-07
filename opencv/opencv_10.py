# SIFT 算法
import cv2
import numpy as np
img = cv2.imread('asd.jpg')
img1 = cv2.imread('template.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(cv2.__version__)
sift = cv2.SIFT_create()

kp1, des1 = sift.detectAndCompute(img, None)
kp2, des2 = sift.detectAndCompute(img1, None)
bf = cv2.BFMatcher(crossCheck=True)
matches = bf.match(des1, des2)
print(type(matches))
matches =  sorted(matches, key=lambda x:x.distance)
img3 = cv2.drawMatches(img, kp1, img1, kp2, matches[:10], None, flags=2)
cv2.imshow("sd", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()