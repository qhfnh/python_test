# shi-Tomasi角点检测
import cv2
import numpy as np

# 焦点 哈里斯角点检测
blockSize = 3
ksize = 3
k =0.04
img = cv2.imread('asd.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray, maxCorners=1000, qualityLevel=0.01, minDistance=10)
corners = np.int0(corners)
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (255 , 0 , 0), -1)
cv2.imshow('asd', img)
cv2.waitKey(0)
