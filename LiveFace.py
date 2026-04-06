import cv2



face_cascade = cv2.CascadeClassifier('C:/Users/rajka/Downloads/PRO-c116-Teacher-Reference-Code-main (1)/PRO-c116-Teacher-Reference-Code-main/haarcascade_frontalface_default.xml')
vid = cv2.VideoCapture(0)


while(True):
    ret,frame = vid.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in faces:
      cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0),2)
    cv2.imshow('frame',frame)
    

    if cv2.waitKey(25)==32:
        break

vid.release()
cv2.destroyAllWindows()