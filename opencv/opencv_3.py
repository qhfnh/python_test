import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)
r, g, b = cv2.split(img)
b[10: 100, 10: 100] = 255
g[10: 100, 10: 100] = 255

img2 = cv2.merge((b, g, r))

cv2.imshow("as", np.hstack((b, g)))
cv2.imshow("as12", np.hstack((img, img2)))
cv2.waitKey(0)
cv2.destroyAllWindows()
