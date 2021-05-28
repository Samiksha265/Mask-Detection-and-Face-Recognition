from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
import imutils
import time
from cv2 import cv2
import os
from datetime import datetime
import face_recognition 
import csv

path = 'Face_Dataset'
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList



def markName(name):

    filename = datetime.now()
    x = filename.strftime("%d_%B_%Y")+'.csv'
    p = "D:\\PROJECT\\Fine\\"+x
    if os.path.exists(p):
        with open(p, 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList and name !='Unknown' and name != 'Mask':
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}') 

    else:                
        with open(p, 'w') as f:

            nameList = []
            if name not in nameList and name!='Unknown' and name != 'Mask':
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')


encodeListKnown = findEncodings(images)
print('Encoding Complete')



faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = load_model("mask_detector1.model")
imagep = "D:\\1.jpg"
video_capture = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    #frame = cv2.imread(imagep)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(60, 60),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
    faces_list=[]
    preds=[]

    facesCurFrame = face_recognition.face_locations(frame)
    encodesCurFrame = face_recognition.face_encodings(frame, facesCurFrame)
    faces_name = []

    for encodeFace in encodesCurFrame:
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        name = 'Unknown'
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
# print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()

        faces_name.append(name)

    for (x, y, w, h) in faces:
        face_frame = frame[y:y+h,x:x+w]
        face_frame = cv2.cvtColor(face_frame, cv2.COLOR_BGR2RGB)
        face_frame = cv2.resize(face_frame, (224, 224))
        face_frame = img_to_array(face_frame)
        face_frame = np.expand_dims(face_frame, axis=0)
        face_frame =  preprocess_input(face_frame)
        faces_list.append(face_frame)

        if len(faces_list)>0:
            preds = model.predict(faces_list)

        for pred in preds:
            (mask, withoutMask) = pred

        if mask > withoutMask:
            label = "Mask" 
        else:
            for (top, right, bottom, left), name in zip(facesCurFrame, faces_name):
                label = name
            markName(label)
            
        color = (0, 255, 0) if label == "Mask" else (255, 0, 0)

        cv2.putText(frame, label, (x, y- 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
 
        cv2.rectangle(frame, (x, y), (x + w, y + h),color, 2)
        # Display the resulting frame

    cv2.imshow("LIVE", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()