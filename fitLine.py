# 0813.py
import cv2
import numpy as np

#1
src = cv2.imread('./data/banana.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, bImage = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)
##bImage = cv2.erode(bImage, None)
bImage = cv2.dilate(bImage, None)
##cv2.imshow('src',  src)
##cv2.imshow('bImage',  bImage)

mode   = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
contours, _ = cv2.findContours(bImage, mode, method)

dst = src.copy()
##cv2.drawContours(dst, contours, -1, (255,0,0), 3)
cnt = contours[0]
cv2.drawContours(dst, [cnt], 0, (255,0,0), 3)

#2
dst2 = dst.copy()
rows,cols = dst2.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
y1 =  int((-x*vy/vx) + y)
y2 = int(((cols-x)*vy/vx)+y)
cv2.line(dst2,(0,y1), (cols-1,y2),(0,0,255), 2)
cv2.imshow('dst2',  dst2)

cv2.waitKey()
cv2.destroyAllWindows()
