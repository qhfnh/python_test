import cv2
import numpy as np
# 焦点 哈里斯角点检测
blockSize = 3
ksize = 3
k =0.04

img = cv2.imread('asd.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = cv2.cornerHarris(gray, blockSize, ksize, 0.04)
# Harris角点展示
img[dst>0.01*dst.max()] = [0, 0, 255]

cv2.imshow('asd', img)
cv2.waitKey(0)
cv2.destroyAllWindows()