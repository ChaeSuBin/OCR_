import cv2
import numpy as np
from math import atan

#colorSepalation
src1 = cv2.imread('./result_subway/subc.jpg')
#hsv1 = cv2.cvtColor(src1, cv2.COLOR_BGR2HSV)
srcCopy = src1.copy()

lowerb = (50, 10, 0)
upperb = (255, 55, 25)

yLowerb = (0, 100, 120)
yUpperb = (25, 255, 255)

bImageA = cv2.inRange(src1, lowerb, upperb)
bImageB = cv2.inRange(srcCopy, yLowerb, yUpperb)
bImage = cv2.add(bImageA, bImageB)

################# 이 아래는 사용안됨.###################
#cv2.imshow('src', src1)
#cv2.imshow('hsv', hsv1)
#cv2.imshow('sepa', bImage)

kernel = cv2.getStructuringElement(shape = cv2.MORPH_RECT, ksize = (3,3))
bImage = cv2.dilate(bImage, kernel, iterations = 25)
bImage = cv2.erode(bImage, kernel, iterations = 25)
cv2.imshow('dilate', bImage)
    
#GetHorizontalLine
mode   = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
contours, _ = cv2.findContours(bImage, mode, method)

dst = src1.copy()
cnt = contours[0]
cv2.drawContours(dst, contours, 0, (0,0,255), 1)
#print('length: ', len(contours))
#cv2.imshow('contours', dst)

dst2 = dst.copy()
rows,cols = dst2.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
y1 =  int((-x*vy/vx) + y)
y2 = int(((cols-x)*vy/vx)+y)
cv2.line(dst2,(0,y1), (cols-1,y2),(0,0,255), 2)
cv2.imshow('dst2',  dst2)

delta = vy / vx
radian = atan(delta)*100
print(vx, vy, x, y)
print('delta:', delta)
print('radian:', radian)
'''
mask = np.zeros(src1.shape, dtype=src1.dtype)
cnt=contours[0]
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
cv2.drawContours(mask, [approx], -1, (255, 255, 0), 2)
cv2.imshow('mask', mask)
'''
'''
#detectConerPoint
K = 4
corners = cv2.goodFeaturesToTrack(bImage, maxCorners=K,
              qualityLevel=0.05, minDistance=10)
print('corners.shape=',corners.shape)
print('corners=',corners)

dstCorners = src1.copy()
corners = corners.reshape(-1, 2)
for x, y in corners:    
    cv2.circle(dstCorners, (x, y), 5, (0,0,255), -1)
cv2.imshow('dstCorners', dstCorners)

#MinimumAreaBoundingBox
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int32(box)
print('box=', box)
dst4 = dst2.copy()
cv2.drawContours(dst4,[box],0,(255,255,0),2)
cv2.imshow('dst4',  dst4)
'''
#AffineRotation
rows, cols, channels = src1.shape
M1 = cv2.getRotationMatrix2D( (rows/2, cols/2),  radian/2, 1)
result = cv2.warpAffine(src1, M1, (cols, rows))
cv2.imshow('result',  result)

#cv2.imshow('final', dst)
cv2.waitKey()
cv2.destroyAllWindows()
