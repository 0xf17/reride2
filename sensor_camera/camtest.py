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

resolution = (800,600)
camera = PiCamera()
camera.resolution = resolution
camera.framerate = 30

#cap = cv2.VideoCapture(0)
cap = PiRGBArray(camera, size=resolution)

time.sleep(1)

font = cv2.FONT_HERSHEY_SIMPLEX

class Marker:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.frame = []
    def send_frame(self):
        frame.append(timestamp, corners)



# to be removed
# def fps():
#     fps = cv2.CAP_PROP_FPS

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def mid_point(p1,p2):
    x = int((p1[0]+p2[0])/2)
    y = int((p1[1]+p2[1])/2)
    return (x,y)

def distance(p1,p2):
    return int(np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2))

def get_shoulders():
    try:

        shoulder_right_id = id_list2.index(1)
        #shoulder_right=(corners[shoulder_right_id][0][0][0],corners[shoulder_right_id][0][0][1])
        shoulder_right = get_marker_center(corners[shoulder_right_id][0])

        shoulder_left_id = id_list2.index(2)
        shoulder_left = get_marker_center(corners[shoulder_left_id][0])
        #shoulder_left=(corners[shoulder_left_id][0][0][0],corners[shoulder_left_id][0][0][1])

        cv2.line(image, shoulder_left, shoulder_right,(255,0,0),2)

        draw_horizontal_from_collar(shoulder_left,shoulder_right)
        draw_vertical(mid_point(shoulder_left,shoulder_right))

        shoulder_left_label = str(int(get_marker_angle(corners[shoulder_left_id][0])))
        shoulder_right_label = str(int(get_marker_angle(corners[shoulder_right_id][0])))
        shoulder_tilt = str(int(get_angle(shoulder_left,shoulder_right)))
        cv2.putText(image, shoulder_left_label, shoulder_left,font,0.5,(255,255,0),1,cv2.LINE_AA)
        cv2.putText(image, shoulder_right_label, shoulder_right,font,0.5,(255,255,0),1,cv2.LINE_AA)
        cv2.putText(image, shoulder_tilt, mid_point(shoulder_left, shoulder_right),font,1,(255,255,0),1,cv2.LINE_AA)

    except Exception as err:
        print('Error: '+str(err))

def get_stoop():
    try:

        shoulder_right_id = id_list2.index(1)
        #shoulder_right=(corners[shoulder_right_id][0][0][0],corners[shoulder_right_id][0][0][1])
        shoulder_right = get_marker_center(corners[shoulder_right_id][0])

        shoulder_left_id = id_list2.index(2)
        shoulder_left = get_marker_center(corners[shoulder_left_id][0])
        #shoulder_left=(corners[shoulder_left_id][0][0][0],corners[shoulder_left_id][0][0][1])

        chin_id = id_list2.index(5)
        #chin=(corners[chin_id][0][0][0],corners[chin_id][0][0][1])
        chin = get_marker_center(corners[chin_id][0])

        cv2.line(image, shoulder_left, chin,(0,255,0),2)
        cv2.line(image, shoulder_right, chin,(0,255,0),2)

        #draw_horizontal_from_collar(shoulder_left,shoulder_right)
        #draw_vertical(mid_point(shoulder_left,shoulder_right))

        #shoulder_left_label = str(int(get_marker_angle(corners[shoulder_left_id][0])))
        #shoulder_right_label = str(int(get_marker_angle(corners[shoulder_right_id][0])))
        #shoulder_tilt = str(int(get_angle(shoulder_left,shoulder_right)))
        #cv2.putText(image, shoulder_left_label, shoulder_left,font,0.5,(255,255,0),1,cv2.LINE_AA)
        #cv2.putText(image, shoulder_right_label, shoulder_right,font,0.5,(255,255,0),1,cv2.LINE_AA)
        #cv2.putText(image, shoulder_tilt, mid_point(shoulder_left, shoulder_right),font,1,(255,255,0),1,cv2.LINE_AA)

    except Exception as err:
        print('Error: '+str(err))

def get_marker_center(corners):
    return mid_point(corners[0],corners[2])

def get_marker_angle(corners):
    p1,p2 = 1,0
    m = -1*(corners[p2][1]-corners[p1][1])/(corners[p2][0]-corners[p1][0])
    return np.degrees(np.arctan(m))

def get_angle(p1,p2):
    m = -1*(p2[1]-p1[1])/(p2[0]-p1[0])
    return np.degrees(np.arctan(m))

def draw_horizontal_from_collar(shoulder_left,shoulder_right):
    y = mid_point(shoulder_left,shoulder_right)[1]
    left = (0,y)
    right = (resolution[0],y)
    cv2.line(image, left, right,(0,0,0),1)

def draw_vertical(point):
    x = point[0]
    top = (x,0)
    bottom = (x,resolution[1])
    cv2.line(image, top, bottom,(0,0,0),1)


def get_head():
    try:
        head_id = id_list2.index(3)
        #head_top=(corners[head_id][0][0][0],corners[head_id][0][0][1])
        head_top=get_marker_center(corners[head_id][0])

        chin_id = id_list2.index(5)
        #chin=(corners[chin_id][0][0][0],corners[chin_id][0][0][1])
        chin = get_marker_center(corners[chin_id][0])

        cv2.line(image, head_top,chin,(0,255,0,0),2)
        nose = mid_point(head_top,chin)
        cv2.circle(image, nose, int(distance(nose,head_top)), (0,0,255),2)

        draw_vertical(chin)

        head_label = str(get_marker_angle(corners[head_id]))
        chin_label = str(get_marker_angle(corners[chin_id]))

        cv2.putText(image,head_label,head_top,font,0.5,(255,255,0),1,cv2.LINE_AA)
        cv2.putText(image,chin_label,chin,font,0.5,(255,255,0),1,cv2.LINE_AA)

    except Exception as err:
        print('Error: '+str(err))

def get_head_and_shoulders():
    get_head()
    get_shoulders()

for frame in camera.capture_continuous(cap, format="bgr", use_video_port = True):
    image = frame.array
    #cv2.Flip(frame, flipMode=-1)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
    parameters =  aruco.DetectorParameters_create()

    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    id_list = ids.tolist()

    id_list2 = []
    for i in id_list:
        id_list2.append(i[0])

    image = aruco.drawDetectedMarkers(image, corners, ids)

    get_head_and_shoulders()
    get_stoop()

    cv2.putText(image,'RR2/CamTestv0.1.2706',(10,30),font,1,(255,0,0),1,cv2.LINE_AA)
    cv2.putText(image,fps(),(10,50),font,1,(255,0,255),1,cv2.LINE_AA)
    cv2.imshow('frame',image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cap.truncate(0) # Important!

camera.close()
cv2.destroyAllWindows()
