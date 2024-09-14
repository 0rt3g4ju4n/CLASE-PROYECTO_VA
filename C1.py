#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: julian
"""
## OPEN CV ####
import cv2
import numpy as np

imagen = cv2.imread('plantilla_1.jpg') 
cv2.imshow('Imagen Cargada',imagen)
cv2.imwrite('Grises.png',imagen) #Guardar imagen
cv2.waitKey(0)
cv2.destroyAllWindows()

########## COLOR ####################
## Canales de color BGR
bgr = cv2.imread('plantilla_1.jpg') 
b = bgr[:,:,0]
g = bgr[:,:,1]
r = bgr[:,:,2]
cv2.imshow('BGR',np.hstack([b,g,r])) #Muestra los tres canales al tiempo
cv2.waitKey(0)
cv2.destroyAllWindows()



### cONVERSIÓN A ESCALA DE GRISES ###########
gris= cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grises',gris)
cv2.waitKey(0)
cv2.destroyAllWindows()
#######   Umbralización
_, binarizada = cv2.threshold(gris,130,255,cv2.THRESH_BINARY) #Cuando el pixel sea mayor a 130 se asignará 255

cv2.imshow('Binarizada',binarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()

#########################

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))

eroded = cv2.erode(binarizada,kernel)

cv2.imshow("Eroded Image",eroded);
cv2.waitKey(0)
cv2.destroyAllWindows()

dilated = cv2.dilate(binarizada,kernel)

cv2.imshow("Dilated Image",dilated);

cv2.waitKey(0)
cv2.destroyAllWindows()


###########################

filtrada= cv2.medianBlur(bgr, 3)

cv2.imshow('Median Filter Processing', filtrada)

cv2.imwrite('processed_image.png', filtrada)

cv2.waitKey(0)
cv2.destroyAllWindows()



