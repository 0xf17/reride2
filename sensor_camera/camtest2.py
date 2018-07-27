"""
.. module:: sensor_camera/camtest
   : platform:
   : synopsis:

.. moduleauthor:: @grvashu

"""
import numpy as np
import cv2
import cv2.aruco as aruco
import time

from picamera.array import PiRGBArray
from picamera import PiCamera

from reride import client

resolution = (800,600)
camera = PiCamera()
camera.resolution = resolution
camera.framerate = 30

#cap = cv2.VideoCapture(0)
cap = PiRGBArray(camera, size=resolution)

time.sleep(1)

font = cv2.FONT_HERSHEY_SIMPLEX

class CamData:
    def __init__(self, id_list):
        self.R = id_list.index(1)
        self.L = id_list.index(2)
        self.H = id_list.index(5)
        self.C = id_list.index(3)

    def get_data(self):
        self.cam_R = corners[self.R][0]
        self.cam_L = corners[self.L][0]
        self.cam_H = corners[self.H][0]
        self.cam_C = corners[self.C][0]

    def send_data(self):
        L = [self.cam_H, self.cam_C, self.cam_L, self.cam_R]
        client.send_data(L)


for frame in camera.capture_continuous(cap, format="bgr", use_video_port = True):
    image = frame.array

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
    parameters =  aruco.DetectorParameters_create()

    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    id_list = ids.tolist()

    id_list2 = []
    for i in id_list:
        id_list2.append(i[0])

    cd = CamData(id_list2)
    cd.get_data()
    cd.send_data()

    image = aruco.drawDetectedMarkers(image, corners, ids)

    # get_head_and_shoulders()
    # get_stoop()

    cv2.putText(image,'RR2/CamTestv0.1.2706',(10,30),font,1,(255,0,0),1,cv2.LINE_AA)
    cv2.putText(image,fps(),(10,50),font,1,(255,0,255),1,cv2.LINE_AA)
    cv2.imshow('frame',image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cap.truncate(0) # Important!

camera.close()
cv2.destroyAllWindows()
