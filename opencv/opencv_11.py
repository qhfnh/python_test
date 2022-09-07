# 利用SIFT算法进行图片匹配 SIFT解决harris中放大缩小特征改变的事情
import cv2
import numpy as np
img1 = cv2.imread('asd.jpg')
img2 = cv2.imread('match.jpg')
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
descriptor = cv2.SIFT_create()
(kps, features) = descriptor.detectAndCompute(img1, None) # mask感兴趣的区域 features描述子进行特征匹配用
kps = np.float32([kp.pt for kp in kps])
