from typing import List, Any

import cv2
import numpy as np
import os
import pytesseract
import regex as re

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\praja\OneDrive\Desktop\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('3648476-1.jpg')
img1=cv2.imread('3657993.jpg')
img2=cv2.imread('3642684.jpg')
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
print(pytesseract.image_to_string(img1))
print(pytesseract.image_to_string(img2))

hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    # print(b)
    b = b.split()
    # print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 1)
hImg, wImg, _ = img1.shape
boxes = pytesseract.image_to_boxes(img1)
for b in boxes.splitlines():
    # print(b)
    b = b.split()
    # print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 1)
hImg, wImg, _ = img2.shape
boxes = pytesseract.image_to_boxes(img2)
for b in boxes.splitlines():
    # print(b)
    b = b.split()
    # print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 1)



cv2.imshow('Result', img)
cv2.waitKey(0)
