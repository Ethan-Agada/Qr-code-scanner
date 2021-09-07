
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import webbrowser

#img=cv2.imread('C:\\Users\\jeremy\Downloads\\download.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while True:
    succesful,img = cap.read()
    for barcode in decode(img):
        Data = barcode.data.decode('utf-8')
        webbrowser.open_new(Data)
        print(Data)
        pts = np.array([barcode.polygon],np.int32)
        pts= pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2 = barcode.rect
        cv2.putText(img, Data,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255,0,255),2)
    cv2.imshow("Qr code scaner", img)
    cv2.waitKey(1)
    