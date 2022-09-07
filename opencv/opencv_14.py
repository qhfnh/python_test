import cv2
import numpy as np
# 高斯滤波
img = cv2.imread('asd.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
dst = cv2.GaussianBlur(img, (5 ,5), sigmaX=1)
cv2.imshow('asd', np.hstack((img, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()