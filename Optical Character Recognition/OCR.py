import pytesseract
import os
from PIL import Image


pytesseract.Pytesseract.tesseract_cmd = r"c:\Program Files\Image -OCR\Image.exe" 

def convert()
    img = Image.open('img.jpg')
    text = pytesseract.Image_to_string(img)
    print(text)


convert()
