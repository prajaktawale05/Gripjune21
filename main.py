





import cv2
import pytesseract
from pytesseract import Output


pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\praja\OneDrive\Desktop\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('OB.png')


img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(img))

def match_template(img, template):

    return cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

hImg,wImg,_=img.shape

box=pytesseract.image_to_boxes(img)

for b in box.splitlines():


    b = b.split(' ')

    img = cv2.rectangle(img, (int(b[1]), hImg - int(b[2])), (int(b[3]), hImg - int(b[4])), (0, 255, 0),0)

cv2.imshow('image',img)

cv2.waitKey(0)

