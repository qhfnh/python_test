from statistics import mode
import cv2
import mediapipe as  mp

class handDetector():
    def __init__(self, model=False, maxHands=2, detectionCon=0.5, trackCon=0.5) -> None:
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.myHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon)
        self.myDraw = mp.solutions.drawing_utils

    def findHands(self, img, drawing=True):
            imgBGR = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = self.hands.process(imgBGR)
            #print(results.multi_hand_landmarks)
            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    # for id, lm in enumerate(handLms.landmark):
                    #     #print(id, lm)
                    #     h, w, c = img.shape
                    #     cx, cy = int(lm.x*w) , int(lm.y*h)
                    #     #print(cx, cy)

                    #     cv2.circle(img, (cx, cy), 15, (255 , 0, 255), cv2.FILLED)

                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
