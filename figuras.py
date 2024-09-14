import cv2
import numpy as np
image = cv2.imread('geometria.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10, 150)
cv2.imshow('Filtro Canny',canny)
cv2.waitKey(0)

Contours,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html

azulBajo = np.array([100,100,20],np.uint8)
azulAlto = np.array([125,255,255],np.uint8)
while True:
  frameHSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(frameHSV,azulBajo,azulAlto)
  contornos, y = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cv2.drawContours(image, contornos, -1, (0,0,255), 3)
    
  cv2.imshow('maskAzul',mask)
  cv2.imshow('frame',image)
  if cv2.waitKey(1) & 0xFF == ord('s'):
    break
cv2.destroyAllWindows()


for c in Contours:
  perimeter = cv2.arcLength(c,True)
  epsilon=0.01*perimeter
  vertices = cv2.approxPolyDP(c,epsilon,True)

  x,y,w,h = cv2.boundingRect(vertices)
  if len(vertices)==3:
    cv2.putText(image,'Triangulo', (x,y-5),1,1.5,(0,255,0),2)
  if len(vertices)==4:
    aspect_ratio = float(w)/h
    print('aspect_ratio= ', aspect_ratio)
    if aspect_ratio == 1:
      cv2.putText(image,'Cuadrado', (x,y-5),1,1.5,(0,255,0),2)
    else:
      cv2.putText(image,'Rectangulo', (x,y-5),1,1.5,(0,255,0),2)
  if len(vertices)==5:
    cv2.putText(image,'Pentagono', (x,y-5),1,1.5,(0,255,0),2)
  if len(vertices)==6:
    cv2.putText(image,'Hexagono', (x,y-5),1,1.5,(0,255,0),2)
  if len(vertices)>10:
    cv2.putText(image,'Circulo', (x,y-5),1,1.5,(0,255,0),2)
  cv2.drawContours(image, [vertices], 0, (0,255,0),2)
  cv2.imshow('image',image)
  cv2.waitKey(0)
  