#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
几何变换：放大、缩小、旋转等，改变空间位置
完成几何变换需要两个独立的算法：
1.实现空间坐标转换(像素如何从初始位置移动到终止位置)，
2.插值算法(完成输出图像每个像素值的灰度值）
"""
import cv2
import numpy as np
import sys
import math

# 仿射变换（二维）
image = cv2.imread('../Img/7418.jpeg')
h,w = image.shape[:2]
print(h,w)
# 缩小两倍
A1 = np.array([[0.5,0,0],[0,0.5,0]],np.float32)
d1 = cv2.warpAffine(image,A1,(w,h),borderValue = 125)

# 先缩小两倍，再平移
A2 = np.array([[0.5,0,50],[0,0.5,100]],np.float32)
d2 = cv2.warpAffine(image,A2,(w,h),borderValue = (255,255,255))

# 在d2的基础上，绕图像的中心点旋转
A3 = cv2.getRotationMatrix2D((w/2.0,h/2.0),90,0.5)
d3 = cv2.warpAffine(d2,A3,(w,h),borderValue = 0)


cv2.imshow('image',image)
cv2.imshow('d1',d1)
cv2.imshow('d2',d2)
cv2.imshow('d3',d3)
cv2.waitKey(0)
cv2.destroyAllWindows()





















