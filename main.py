import cv2
import pyautogui
from cvzone.HandTrackingModule import HandDetector
cap=cv2.VideoCapture(1)
detector=HandDetector(detectionCon=0.8)
while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    hands,img=detector.findHands(img,flipType=False)
    if hands:
        lmList=hands[0]['lmList']
        cursor=lmList[8]
        length,info,img=detector.findDistance(lmList[8],lmList[4],img)
        if length<60:
            pyautogui.press("volumedown")
        else:
            pyautogui.press("volumeup")  
    cv2.namedWindow("img",cv2.WND_PROP_FULLSCREEN)
    cv2.imshow("img",img)
    cv2.waitKey(1)