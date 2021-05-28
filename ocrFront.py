import cv2
import numpy as np

#흑백변환
src = cv2.imread('./result_subway/subf.jpg')
dst = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
#cv2.imshow('gray', dst)

#경계 이미지 추출
kernela = cv2.getStructuringElement(shape = cv2.MORPH_RECT, ksize = (3,3))
mGradiant = cv2.morphologyEx(dst, cv2.MORPH_GRADIENT, kernela, iterations = 1)
cv2.imshow('Agradient', mGradiant)
'''
kernel = cv2.getStructuringElement(shape = cv2.MORPH_RECT, ksize = (3,3))
erode = cv2.erode(mGradiant, kernel, iterations = 5)
cv2.imshow('A-1gradient', erode)
'''
#잡영제거
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

#구멍 채우기
kernelb = cv2.getStructuringElement(shape = cv2.MORPH_RECT, ksize = (5,3))
#closing = cv2.dilate(dst2, kernel, iterations = 1)
#cv2.imshow('Cdlt', closing)
closing = cv2.morphologyEx(dst2, cv2.MORPH_CLOSE, kernelb, iterations = 5)
cv2.imshow('Cclose', closing)

#컨투어 찾기
mode = cv2.RETR_LIST
#mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
contours, hierarchy = cv2.findContours(closing, mode, method)

#컨투어 그리기
mask = np.zeros(src.shape, dtype=src.dtype)
print(len(contours))
#mask[10, 10] = 255
#cv2.imshow('mask', mask)
cv2.drawContours(mask, contours, -1, (255, 255, 0), 1)
cv2.imshow('Dcont', mask)
print(src.shape[0], src.shape[1])

#박스 검출 크기지정
for idx in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[idx])
    #print(w, h)
    if h > 30 and w > 60 and h != src.shape[0] and w != src.shape[1]:
         cv2.rectangle(dst, (x, y), (x+w-1, y+h-1), 255)
cv2.imshow('rect', dst)

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
