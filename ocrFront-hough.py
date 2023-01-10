import cv2
import numpy as np
#import horizontalFit as fit
#from horizontalFit import result as fitRe
from pspTrans import Result as fitRe
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract64\tesseract'

#convertGRAY
#src = cv2.imread('./result_subway/sube.jpg')
src = fitRe
dst = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
#cv2.imshow('gray', dst)

#경계 이미지 추출
kernela = cv2.getStructuringElement(shape = cv2.MORPH_RECT, ksize = (3,3))
mGradiant = cv2.morphologyEx(dst, cv2.MORPH_GRADIENT, kernela, iterations = 1)
#cv2.imshow('Agradient', mGradiant)
'''
kernel = cv2.getStructuringElement(shape = cv2.MORPH_RECT, ksize = (3,3))
erode = cv2.erode(mGradiant, kernel, iterations = 5)
cv2.imshow('A-1gradient', erode)
'''
#noiseCleaning
'''
#ADAPTIVE
dst2 = cv2.adaptiveThreshold(mGradiant, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                             cv2.THRESH_BINARY, 91, 7)
cv2.imshow('Bthreshold', dst2)
'''
'''
#nonadaptive
ret, dst2 = cv2.threshold(mGradiant, 120, 255, cv2.THRESH_BINARY)
print('ret=', ret)
cv2.imshow('Bthreshold', dst2)
'''
#nonadaptive-OTSU
ret, dst2 = cv2.threshold(mGradiant, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print('ret=', ret)
cv2.imshow('Bthreshold', dst2)

#blocking
kernelb = cv2.getStructuringElement(shape = cv2.MORPH_RECT, ksize = (3,3))
#closing = cv2.dilate(dst2, kernel, iterations = 1)
closing = cv2.morphologyEx(dst2, cv2.MORPH_CLOSE, kernelb, iterations = 2)
cv2.imshow('Cclose', closing)

#LinesDetect-Hough
edges = cv2.Canny(closing, 50, 100)
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180.0, threshold=40,
                        minLineLength=8, maxLineGap = 3)
print('lines.shape=', lines.shape)

tempDark = np.zeros(src.shape, dtype=src.dtype)

for line in lines:
    x1, y1, x2, y2   = line[0]
    cv2.line(tempDark,(x1,y1),(x2,y2),(0,0,255),2)
    cv2.line(closing,(x1,y1),(x2,y2),(0,0,255),5)

cv2.imshow('Cclose_Line', tempDark)
cv2.imshow('_Line', closing)

#findContours
#mode = cv2.RETR_LIST
mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
contours, hierarchy = cv2.findContours(closing, mode, method)
'''
#DrawContours
mask = np.zeros(src.shape, dtype=src.dtype)
print(len(contours))
#mask[10, 10] = 255
#cv2.imshow('mask', mask)
cv2.drawContours(mask, contours, -1, (255, 255, 0), 1)
cv2.imshow('Dcont', mask)
print(src.shape[0], src.shape[1])
'''
'''
tempImg = src
img_rgb = cv2.cvtColor(tempImg, cv2.COLOR_BGR2RGB)
custom_oem_psm_config = r'--oem 3 --psm 3'
print(pytesseract.image_to_string(
    img_rgb, lang='kor', config=custom_oem_psm_config))
'''
#detecetBoxSizeOpt
boxNum = 0
for idx in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[idx])
    #print(w, h)
    if h > 17 and w > 17 and h != src.shape[0] and w != src.shape[1]:
         cv2.rectangle(src, (x, y), (x+w-1, y+h-1), (0, 0, 255), 2)
         
         boxNum += 1
         tempImg = src[y:y+h, x:x+w]
         reversalOut = 255-tempImg
         cv2.imshow('reversal', reversalOut)
         img_rgb = cv2.cvtColor(reversalOut, cv2.COLOR_BGR2RGB)
         
         custom_oem_psm_config = r'--oem 3 --psm 10'
         print(pytesseract.image_to_string(
             img_rgb, lang='kor', config=custom_oem_psm_config))
         cv2.waitKey()
             
cv2.imshow('detectResult', src)
print('bounding box cnt: ',boxNum)

'''
for idx in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[idx])
    mask[y:y+h, x:x+w] = 0
    cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
    r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
    if r > 0.45 and w > 8 and h > 8:
        cv2.rectangle(rgb, (x, y), (x+w-1, y+h-1), (0, 255, 0), 2)
'''
#cv2.imshow('final', dst)
cv2.waitKey()
cv2.destroyAllWindows()
