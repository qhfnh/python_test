import cv2
from cv2 import Mat
def showImage(imageName: str):
    img = cv2.imread(imageName)
    cv2.imshow(imageName, img)
    cv2.waitKey(0)
    cv2.destroyWindow(imageName)

 
cv2.namedWindow("video", cv2.WINDOW_NORMAL)

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
vw = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480))

while cap.isOpened():
    # 读一帧一帧数据
    ret, frame = cap.read()
    if not ret:
        break 
    vw.write(frame)
    cv2.imshow("video", frame)
    if cv2.waitKey(1) & 0xff == ord(' '): 
        break
 
cap.release()
vw.release()
cv2.destroyWindow("video")



