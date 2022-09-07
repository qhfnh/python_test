import cv2
import numpy as np
# 适应二值化
img = cv2.imread('asd.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 0)

cv2.imshow('asd',  dst)
cv2.waitKey(0)
cv2.destroyAllWindows()