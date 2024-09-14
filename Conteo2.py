import cv2
from cv2 import bitwise_not
import numpy as np
imagen = cv2.imread("plantilla_1.jpg")
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

#cv2.imshow("Gris",grises)
#cv2.waitKey(0)

_,binarizada =  cv2.threshold(grises, 10, 255, cv2.THRESH_BINARY_INV)
inv=bitwise_not(binarizada)
cv2.imshow('Umbralizada', binarizada)
cv2.waitKey(0)
inv=bitwise_not(binarizada)
cv2.imshow('Umbralizada', inv)
cv2.waitKey(0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(10, 8))
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT,(14, 25))
erode= cv2.erode(binarizada,kernel)
cv2.imshow("eroded Image",erode);
cv2.waitKey(0)
#dilated = cv2.dilate(erode,kernel2)
#cv2.imshow("Dilated Image",dilated);
#cv2.waitKey(0)



contornos,_ = cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('Contornos: ', len(contornos))
font = cv2.FONT_HERSHEY_SIMPLEX

mensaje = 'Numero de Objetos:' + str(len(contornos))
cv2.putText(imagen,mensaje,(10,50),font,0.75,
    (255,0,0),2,cv2.LINE_AA)
for c in contornos:
  cv2.drawContours(imagen, [c], 0, (255,0,0),2)
  cv2.imshow('Imagen', imagen)
  cv2.waitKey(0)
    
cv2.destroyAllWindows()
