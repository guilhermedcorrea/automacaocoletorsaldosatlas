from pdf2image import convert_from_path, convert_from_bytes
import tempfile
import cv2
import pytesseract
import re
import pandas as pd
from  itertools import zip_longest
from os import listdir, path, makedirs
from os.path import isfile, join
import shutil
import pyodbc
import time
import re


pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Crawler\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
imagens_files = 'D:\\Trabalhos Python\\IMAGENS ATLAS\\'


lista_imagens_all = [f for f in listdir(imagens_files) if isfile(join(imagens_files, f))]
print(lista_imagens_all)

lista_codigo = []
lista_saldo = []

for lista in lista_imagens_all:
    imagem = cv2.imread(f'D:\\Trabalhos Python\\IMAGENS ATLAS\\{lista}')
    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    texto = pytesseract.image_to_string(imagem_gray, config="tessedit_char_whitelist ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.^´;/")
    valor = texto.split("\n")
    remov_espac = [x for x in valor if x !='' if x !=' ']

    print(lista, remov_espac)






  
