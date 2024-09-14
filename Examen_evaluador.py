import cv2
from cv2 import bitwise_not
import numpy as np
from PIL import Image 
import pytesseract
import pandas as pd
import openpyxl
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
print("Bienvenido")
print("")
print("")
print("**ADVERTENCIAS DE USO")
print("")
print("")
print("1. Preguntas sin responder deben ser respondidas por el profesor en una respuesta incorrecta")
print("2. Te pedimos que subas las hojas en la carpeta llamada: ""respuestas"" " )
print("3. en la carpeta de ""Plantilla"" se debe poner una sola hoja")
print("")
print("")
def cal_score(teacher_sheet, student_sheet):

  imagen = cv2.imread(teacher_sheet)
  imagen2= cv2.imread(student_sheet)
  grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
  grises2= cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)
  _,binarizada =  cv2.threshold(grises, 10, 255, cv2.THRESH_BINARY_INV)
  _,binarizada2=  cv2.threshold(grises2, 10, 255, cv2.THRESH_BINARY_INV)
  inv=bitwise_not(binarizada)
  inv2=bitwise_not(binarizada2)
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 8))
  kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT,(8, 25))
  erode= cv2.erode(binarizada,kernel)
  erode2= cv2.erode(binarizada2,kernel)
  img1=bitwise_not(erode)
  img2=bitwise_not(erode2)
  result=cv2.subtract(img1,img2)
  kernel_d = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 4))
  dilate_ = cv2.dilate(erode2,kernel_d) 
  kernel_final = cv2.getStructuringElement(cv2.MORPH_RECT,(7, 3))
  erode_final=cv2.erode(result,kernel_final)
  contornos3,_ = cv2.findContours(dilate_, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  respondidas= len(contornos3)
  contornos2,_ = cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  c_cantidad=len(contornos2)
  contornos,_ = cv2.findContours(erode_final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  incorrect=len(contornos)
  font = cv2.FONT_HERSHEY_SIMPLEX
  mensaje = 'Respuestas incorrectas:' + str(len(contornos))
  cv2.putText(imagen2,mensaje,(10,50),font,0.75,
    (255,0,0),2,cv2.LINE_AA)
  diferencia = c_cantidad-respondidas
  c_score = ((c_cantidad - (incorrect + diferencia)) / c_cantidad) * 100
  for c in contornos:
    cv2.drawContours(imagen2, [c], 0, (255,0,0),2)
    #cv2.imshow('Imagen', imagen2)
    #cv2.waitKey(0) 
  cv2.destroyAllWindows()
  return c_score
def detect_name(StudentSheet):
  img= Image.open(StudentSheet)
  img.load()
  text = pytesseract.image_to_string(img, lang='spa')
  data=pytesseract.image_to_data(img)
  df = pd.DataFrame([x.split('\t') for x in data.split('\n')])
  nombre = df.tail(5).iloc[:,11]
  nombreT=""
  for name in range(4):
      nombreT += nombre.iloc[name] + " "
  nombreT= nombreT[:-1]
  return nombreT
teacher="Examen\Plantilla"
student= "Examen\Respuestas"

cont=0
dfNN= pd.DataFrame(columns=["Nombre del estudiante", "Nota"])
sheet_t = os.listdir(teacher)
sheets_s=os.listdir(student)

for i in range(len(sheets_s)):
  score = cal_score(os.path.join(teacher, sheet_t[0]), os.path.join(student,sheets_s[i]))
  name = detect_name(os.path.join(student,sheets_s[i]))
  dfNN=dfNN.append({"Nombre del estudiante":name, "Nota":score}, ignore_index=True)
  cont+=1

print("Tabla:")
print(dfNN)
print("Se calificaron ", cont, " examenes")
print("")
print("")
print("Conclusiones:")
conclusiones = ""
for p in range(len(dfNN.iloc[:,1])) :
    if dfNN.iloc[p,1]<60:
        conclusiones = ' deberia cambiar de carrera'
    if dfNN.iloc[p,1]==100:
        conclusiones= 'pasó de forma dudosa'
    if dfNN.iloc[p,1]>59 and dfNN.iloc[p,1]<100:
        conclusiones= 'pasó por suerte'
    print('El estudiante con el nombre: ',dfNN.iloc[p,0], conclusiones)
print("")   
print("Ya puedes abrir el excel con nombre: ""final_score"" y ver los resultados de mejor manera")
dfNN.to_excel("final_score.xlsx", encoding='utf-8')