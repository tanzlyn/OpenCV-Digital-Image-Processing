#!/user/bin/env python3
# -*- coding: utf-8 -*-

# Numpy创建矩阵
# 1.创建数组array()
# 2.创建全0数组zeros()、one()
# 3.创建全值数组full（）
# 4.创建单元数组identity（）、eye()
import cv2

import numpy as np
a = np.array([1,2,3])
b = np.array([[1,2,3],[4,5,6]])
c = np.zeros((8,6,3),np.uint8)
d = np.ones((8,6,3),np.uint8)
f = np.full((8,6),255,np.uint8)
e = np.identity(8)
g = np.eye(5,7,k=2)
# print(g)



# 矩阵的检索和赋值
# 二维。三维

img = np.zeros((480,640,3),np.uint8)
print(img[100,100])
img[100,100]=255
count = 50

while count < 200 :
    img[count, 100,1] = 255
    # img[count, 100] = [0,255,0]  # 两种赋值方式
    img[100,count,0] = 255
    img[50, count,2] = 255
    count = count +1

# cv2.imshow('img',img)
# cv2.waitKey(0)


# numpy获取子矩阵

img = np.zeros((480,640,3),np.uint8)

roi = img[100:300,100:200]
roi[:,:] = [0,0,255]
# roi[:] = [0,0,255]  # 和上面写法相同
roi[10:30,20:50] = [0,255,0]
cv2.imshow('img',img)
cv2.waitKey(0)