import cv2
import numpy as np
img = cv2.imread('asd.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = cv2.cornerHarris(gray, 2, 3, 0.04) # 角点检测 
img[dst > 0.01*dst.max()] = [0,0,255] 
cv2.imshow("sd", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
