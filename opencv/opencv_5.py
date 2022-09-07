import cv2
import numpy as np

img = cv2.imread("asd.jpg", cv2.IMREAD_GRAYSCALE)
v1 = cv2.Canny(img ,80, 150) #设置阈值
v2 = cv2.Canny(img, 50, 100)
res = np.hstack((v1, v2))

cv2.imshow('asd', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
