# -*- coding: utf-8 -*-
"""

@author: Saurav Kanchan

"""
# -*- coding: utf-8 -*-
"""

@author: Saurav Kanchan

"""
import face_recognition
import cv2
import glob2

video_capture = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("result.avi",fourcc, 20.0, (1280,720))

people = []
people_id = []

for filename in glob2.glob(".\people\*"):
    image = face_recognition.load_image_file(filename)
    people_face_encoding = face_recognition.face_encodings(image)[0]
    people.append(people_face_encoding)
    people_id.append(filename[len(".\people")+1:-4])

# abey_image = face_recognition.load_image_file("abey.PNG")
# abey_face_encoding = face_recognition.face_encodings(abey_image)[0]


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True



while True:
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # small_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if process_this_frame:
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            match = face_recognition.compare_faces(people, face_encoding)
            name = "Unknown"

            # if match[0]:
            #     name="Abey"

            for i, n in enumerate(people_id):
                if match[i]:
                    name = n

            face_names.append(name)

    process_this_frame = not process_this_frame


    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


out.release()
video_capture.release()
cv2.destroyAllWindows()