import cv2
from cv2 import bitwise_not
import numpy as np
import re
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
print("Bienvenido")
imagen = cv2.imread("plantilla_1.jpg")
imagen2= cv2.imread("respuestas_1.jpg")
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
grises2= cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)


_,binarizada =  cv2.threshold(grises, 10, 255, cv2.THRESH_BINARY_INV)
_,binarizada2=  cv2.threshold(grises2, 10, 255, cv2.THRESH_BINARY_INV)
inv=bitwise_not(binarizada)
inv2=bitwise_not(binarizada2)
cv2.imshow('1', binarizada)
cv2.waitKey(0)
cv2.imshow('2', binarizada2)
cv2.waitKey(0)
cv2.imshow('3', inv)
cv2.waitKey(0)
cv2.imshow('4', inv2)
cv2.waitKey(0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(10, 8))
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT,(12, 25))
erode= cv2.erode(binarizada,kernel)
erode2= cv2.erode(binarizada2,kernel)
cv2.imshow("5",erode);
cv2.waitKey(0)
cv2.imshow("6",erode2);
cv2.waitKey(0)
img1=bitwise_not(erode)
cv2.imshow("7",img1);
cv2.waitKey(0)
img2=bitwise_not(erode2)
cv2.imshow("8",img2);
cv2.waitKey(0)
result=cv2.subtract(img1,img2)
cv2.imshow("9",result);
cv2.waitKey(0)
kernel_final = cv2.getStructuringElement(cv2.MORPH_RECT,(7, 3))
erode_final=cv2.erode(result,kernel_final)
cv2.imshow("10",erode_final);
cv2.waitKey(0)
erode_final_inv=bitwise_not(erode_final)
cv2.imshow("11",erode_final_inv);
cv2.waitKey(0)
contornos,_ = cv2.findContours(erode_final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('Contornos: ', len(contornos))
font = cv2.FONT_HERSHEY_SIMPLEX
mensaje = 'Respuestas incorrectas:' + str(len(contornos))
cv2.putText(imagen2,mensaje,(10,50),font,0.75,
    (255,0,0),2,cv2.LINE_AA)
text=pytesseract.image_to_string(imagen)
for c in contornos:
  cv2.drawContours(imagen2, [c], 0, (255,0,0),2)
  cv2.imshow('12', imagen2)
  cv2.waitKey(0)
    
cv2.destroyAllWindows()
