# 二值化处理 未成功
import cv2
from cv2 import COLOR_RGB2GRAY
img = cv2.imread('asd.jpg', 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY) # 有阈值
cv2.imshow('THRESH_BINRY', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()