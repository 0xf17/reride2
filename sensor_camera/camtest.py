"""
.. module:: sensor_camera/camtest
   : platform:
   : synopsis:

.. moduleauthor:: @grvashu

"""
import numpy as np
import cv2
import cv2.aruco as aruco

from picamera.array import PiRGBArray
from picamera import PiCamera

camera = PiCamera()

#cap = cv2.VideoCapture(0)
cap = PiRGBArray(camera)

time.sleep(0.1)

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #print(frame.shape) #480x640
    # Our operations on the frame come here
    frame = rescale_frame(frame, percent=50)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
    parameters =  aruco.DetectorParameters_create()

    print(parameters)

        # detectMarkers(...)
        # detectMarkers(image, dictionary[, corners[, ids[, parameters[, rejectedI
        # mgPoints]]]]) -> corners, ids, rejectedImgPoints

    #lists of ids and the corners beloning to each id
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    print(corners)

    frame = aruco.drawDetectedMarkers(frame, corners, ids)
    #print(rejectedImgPoints)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
