import wmi
import time
import math
import cv2 as cv
import numpy as np
import mediapipe as mp
import hand_tracking_module as htm

c = wmi.WMI(namespace="root\\wmi")
brightness_info = c.WmiMonitorBrightness()
methods = c.WmiMonitorBrightnessMethods()[0]

if brightness_info:
    for monitor in brightness_info:
        level = monitor.level
        min_brightness = min(level)
        max_brightness = max(level)
else:
    print("No WmiMonitorBrightness instances found.")

w_cam, h_cam = 640, 480
ptime = 0
bright = 0
bright_bar = 400
bright_percentage = 0

detector = htm.HandDetector()

cap = cv.VideoCapture(0)
cap.set(3,w_cam)
cap.set(4,h_cam)
while True:
    isTrue, img = cap.read()
    try:
        if not isTrue:
            print("There is an while capturing video")
            break

        img = detector.findHands(img)
        lm_list,label = detector.find_position(img,draw=False)
        if lm_list:
            x1, y1 = lm_list[4][1], lm_list[4][2]
            x2, y2 = lm_list[8][1], lm_list[8][2]
            c_x, c_y = (x1+x2)//2, (y1+y2)//2

            cv.circle(img,(x1,y1),15,(255,0,255),cv.FILLED)
            cv.circle(img,(x2,y2),15,(255,0,255),cv.FILLED)
            cv.line(img,(x1,y1),(x2,y2),(255,0,255),3)
            cv.circle(img,(c_x,c_y),15,(255,0,0),cv.FILLED)

            length = math.hypot(x2-x1, y2-y1)
            brightness = np.interp(length,[50,300],[min_brightness,max_brightness])
            bright_bar = np.interp(length,[50,300],[400,150])  # Changed from [400,0] to [400,150]
            bright_percentage = np.interp(length,[50,300],[0,100])
            methods.WmiSetBrightness(int(brightness), 0)
            if length < 0:
                cv.circle(img,(c_x,c_y),15,(255,0,0),cv.FILLED)
        cv.rectangle(img,(50,150),(85,400),(0,255,0),3)
        cv.rectangle(img,(50,int(bright_bar)),(85,400),(0,255,0),cv.FILLED)
        cv.putText(img,f'{int(bright_percentage)} %',(40,450),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,245),2)
            
        
        ctime = time.time()
        fps = 1/(ctime- ptime)
        ptime = ctime

        cv.putText(img, f'FPS: {int(fps)}', (20,50),cv.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)
        cv.imshow("Video ",img)

        if cv.waitKey(1) & 0xFF == ord('d'):
            break
    except Exception as e:
        print(f'The following error occured {e}')
        break
cap.release()
cv.destroyAllWindows()