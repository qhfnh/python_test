import cv2
from cv2 import Sobel
from cv2 import Scharr
import numpy as np
# 边缘检查
# Sobel 算子， 梯度计算 x y 分开计算更简单一些。 即卷积运算 
img = cv2.imread('asd.jpg', cv2.IMREAD_GRAYSCALE)
sobelx = Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)
soblexy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)


# Scharr 算子
img = cv2.imread('asd.jpg', cv2.IMREAD_GRAYSCALE)
scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)
scharry = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)

# Laplacian 算子 拉普拉斯算子
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

res = np.hstack((soblexy, scharrxy, laplacian))

cv2.imshow('asd', res)
cv2.waitKey(0)
cv2.destroyAllWindows()




