import cv2
import time
import math


video = cv2.VideoCapture("C:/Users/rajka/Downloads/PRO-c116-Teacher-Reference-Code-main (1)/PRO-c116-Teacher-Reference-Code-main/bb3.mp4")
tracker = cv2.TrackerMIL_create()
returned,img=video.read()

bbox = cv2.selectROI("Tracking",img,False)
tracker.init(img,bbo)
print(bbox)

def drawBox(img, bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,0),3,1)
    cv2.putText(img,"tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

def goal_track(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,0),3,1)
while True: 
    check,img = video.read()
    success,bbox=tracker.update(img)
    if success:
        drawBox(img,bbox)
    else:
        cv2.putText(img,"lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)    
    cv2.imshow("result",img)
    key = cv2.waitKey(0)
    if key==32:
        print("Stopped") 
        break

    video.release()
    cv2.destroyALLWindows()