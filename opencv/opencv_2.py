import cv2
import numpy as np
def mouseCallback(event, x, y , flags, userdata):
    print(event, x, y, flags, userdata)

cv2.namedWindow('mouse', cv2.WINDOW_NORMAL)
cv2.resizeWindow('mouse', 640, 360)
cv2.setMouseCallback("mouse", mouseCallback, '123')

img = np.zeros((360, 640, 3), np.uint8)
while True:
    cv2.imshow("mouse", img)
    key = cv2.waitKey(1)
    if key == ord(' '):
        break
cv2.destroyAllWindows()