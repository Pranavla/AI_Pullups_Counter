#importing the libraries
import cv2
import poseModule as pm
import numpy as np

cap = cv2.VideoCapture('F:\Computer_vision\Open cv\Project\SQUATS_Counter\Pullups_video.mp4')

detector = pm.poseDetector()

count = 0
dir = 0


while True:

#1.Image preprocessing
    success,image = cap.read()
    image = cv2.resize(image,(410,720))
    cv2.putText(image,'PULL-UPS COUNTER',(50,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)

#2.Find body

    image = detector.findPose(image,draw = False)
    #print(image)
    lmlist = detector.findPosition(image, draw =False)
    #print(lmlist)




#3.Find angles of specific landmark
    if len(lmlist) != 0:
        angle = detector.findAngle(image,16,14,12)
        #print(angle)


# 4.Counting

    per = np.interp(angle,(38,120),(100,0))
    #print(per)

    #print(angle,'---->',per)


    #Percentage
    if per == 0:
        if dir == 0:
            count += 0.5
            dir = 1

    if per == 100:
        if dir == 1:
            count += 0.5
            dir = 0

    #print(count)
    cv2.rectangle(image,(10,10),(75,75),(0,255,0),cv2.FILLED)
    cv2.putText(image,str(int(count)),(25,62),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),3)

    bar = np.interp(angle,(30,120),(200,700))
    #print(bar)


    cv2.rectangle(image,(320,200),(370,700),(0,255,0),1)
    cv2.rectangle(image,(320,int(bar)),(370,700),(0,255,0),cv2.FILLED)


    cv2.putText(image,str(int(per)),(300,180),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),3)


    cv2.imshow('Pull-ups Counter',image)
    if cv2.waitKey(1) & 0xFF == 27:
        break