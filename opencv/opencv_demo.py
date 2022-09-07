# 背景和前景

import cv2
from cv2 import Mat
def showImage(imageName: str):
    img = cv2.imread(imageName)
    cv2.imshow(imageName, img)
    cv2.waitKey(0)
    cv2.destroyWindow(imageName)

 
cv2.namedWindow("video", cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture(0)
# 形态学操作需要
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
# 创建混合高斯模型进行背景建模
fgbg = cv2.createBackgroundSubtractorMOG2()

while cap.isOpened():
    # 读一帧一帧数据
    ret, frame = cap.read()
    if not ret:
        print("break", ret)
        break 
    fgmask = fgbg.apply(frame)
    # 进行开运算 先腐蚀在膨胀 取掉噪音点
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    # 寻找视频中的轮廓
    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
            # 计算周长
            perimeter = cv2.arcLength(c, True)
            if perimeter > 188:
                # 找到一个直角矩形 不会旋转
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("video", frame)
    cv2.imshow("msk", fgmask)
    if cv2.waitKey(150) & 0xff == ord(' '): 
        break
 
cap.release()
cv2.destroyAllWindows()