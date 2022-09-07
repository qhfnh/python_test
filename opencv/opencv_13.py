import cv2
import numpy as np
# 透视变化 即改变关系图
img = cv2.imread("asd.jpg")
h, w = img.shape[:2]
m = np.float32([[1, 0, 200], [0, 1, 0]])
n = cv2.warpAffine(img, m, dsize=(w, h))
cv2.imshow('a', n)
cv2.waitKey(0)
cv2.destroyAllWindows()