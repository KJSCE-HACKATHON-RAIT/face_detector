# -*- coding: utf-8 -*-
"""

@author: Saurav Kanchan

"""
import cv2
import sys
import numpy as np

# ----------------------------------------------------------------------------------------
import winsound
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)


while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (0, 20)
    fontScale = 1
    fontColor = (0, 0, 255)
    lineType = 2

    cv2.putText(frame, 'People Count:-'+str(len(faces)),
                bottomLeftCornerOfText,
                font,
                fontScale,
                fontColor,
                lineType)
    # Display the resulting frame
    cv2.imshow('Video', frame)
    if len(faces) > 1:
        winsound.Beep(1000, 1000)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
