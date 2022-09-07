import cv2
import numpy as np
# 进行二值化 和 寻找 轮廓
img = cv2.imread('./asd.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cnts, h = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(type(cnts))
for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 2)

cv2.imshow('asd', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
