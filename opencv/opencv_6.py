## 模板匹配
import cv2
import numpy as np
img = cv2.imread('asd.jpg', 0)
tem = cv2.imread('template.jpg', 0)
h, w = tem.shape[:2]
print(img.shape)
print(tem.shape)
# 尽量使用归一化的menthod
res = cv2.matchTemplate(img, tem, cv2.TM_SQDIFF)
print(res.shape)
minVal, maxVal, minLoc, maxLocx = cv2.minMaxLoc(res)
print(minVal, maxVal, minLoc, maxLocx)
cv2.rectangle(img, minLoc, (minLoc[0]+ w, minLoc[1]+h), (0, 0, 255), 2)
cv2.imshow("123", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
