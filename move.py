import cv2
import numpy as np
video = cv2.VideoCapture(0)
i = 0
while True:
  ret, cap = video.read()
  if ret == False: break
  gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
  # Aplicamos suavizado para eliminar ruido
  gray = cv2.GaussianBlur(gray, (21, 21), 0)
  if i == 25: # corto retardo para capturar el frame de referencia (fondo)
    Fondo = gray
  if i > 25:
    dif = cv2.absdiff(gray, Fondo)
    _, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
    # Dilatamos el umbral para tapar agujeros
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
    th= cv2.dilate(th, kernel, iterations=2)
           
    cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         
   
    for c in cnts:
      area = cv2.contourArea(c)
      if area < 9000:
        continue
      x,y,w,h = cv2.boundingRect(c)
      cv2.rectangle(cap, (x,y), (x+w,y+h),(0,255,0),2)
  cv2.imshow('Frame',cap)
  i = i+1
  gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
  cv2.imshow(gray) 
  if cv2.waitKey(30) & 0xFF == ord ('q'):
    break
video.release()