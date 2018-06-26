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
camera.framerate = 12

#cap = cv2.VideoCapture(0)
cap = PiRGBArray(camera, size=resolution)

time.sleep(1)

font = cv2.FONT_HERSHEY_SIMPLEX

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
    return int(np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p1[0])**2))

def get_shoulders():
    try:

        shoulder_right_id = id_list2.index(2)
        #print('shoulder_right_id: %d'%shoulder_right_id)
        shoulder_right=(corners[shoulder_right_id][0][0][0],corners[shoulder_right_id][0][0][1])

        shoulder_left_id = id_list2.index(1)
        #print('shoulder_left_id: %d'%shoulder_left_id)
        shoulder_left=(corners[shoulder_left_id][0][0][0],corners[shoulder_left_id][0][0][1])

        cv2.line(image, shoulder_left, shoulder_right,(255,0,0),2)

        cv2.putText(image,'shoulder_left',shoulder_left,font,0.5,(255,255,0),1,cv2.LINE_AA)
        cv2.putText(image,'shoulder_right',shoulder_right,font,0.5,(255,255,0),1,cv2.LINE_AA)

    except Exception as err:
        print('ValueError: '+str(err))

def get_head():
    try:

        head_id = id_list2.index(3)
        head_top=(corners[head_id][0][0][0],corners[head_id][0][0][1])

        chin_id = id_list2.index(5)
        chin=(corners[chin_id][0][0][0],corners[chin_id][0][0][1])

        cv2.line(image, head_top,chin,(0,255,0,0),2)
        nose = mid_point(head_top,chin)
        cv2.circle(image, nose, int(distance(nose,head_top)/2), (0,0,255),2)

        cv2.putText(image,'Head_top',head_top,font,0.5,(255,255,0),1,cv2.LINE_AA)
        cv2.putText(image,'Chin',chin,font,0.5,(255,255,0),1,cv2.LINE_AA)

    except Exception as err:
        print('ValueError: '+str(err))


for frame in camera.capture_continuous(cap, format="bgr", use_video_port = True):
    image = frame.array

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
    parameters =  aruco.DetectorParameters_create()

    #lists of ids and the corners beloning to each id
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    id_list = ids.tolist()
    print('ids:'+str(ids))
    id_list2 = []
    for i in id_list:
        id_list2.append(i[0])

    print('id_list:'+str(id_list))
    image = aruco.drawDetectedMarkers(image, corners, ids)



    get_shoulders()
    get_head()


    '''
        try:
            #head_top=(corners[head_id][0][0][0],corners[0][0][0][1])
            #chin=(corners[chin_id][0][0][0],corners[1][0][0][1])
            #shoulder_right=(corners[shoulder_right_id][0][0][0],corners[2][0][0][1])
            #shoulder_left=(corners[shoulder_left_id][0][0][0],corners[3][0][0][1])
            cv2.line(image, head_top,chin,(0,255,0,0),2)
            cv2.circle(image, mid_point(head_top,chin),50,(0,0,255),2)
            cv2.line(image, shoulder_left, shoulder_right,(255,0,0),2)
        except IndexError:
            print('IndexError')
    '''



    cv2.putText(image,'RR2/CamTestv0.1.2606',(10,30),font,1,(255,0,0),1,cv2.LINE_AA)
    cv2.imshow('frame',image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cap.truncate(0)

# When everything done, release the capture
# cap.release()
camera.close()
cv2.destroyAllWindows()
