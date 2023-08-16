#!/user/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np
"""
Contrast Limited Adaptive Histogram Equalization限制对比度自适应直方图均衡化
原理：
1.将图像划分为不重叠的区域块
2.对每个块分别进行直方图均衡化
3.在没有噪声的情况下，每个小区域的灰度直方图会被限制在一个小的灰度级范围内；
  在有噪声的情况下，每一个分割的区域执行直方图均衡化后，噪声会放大。
  为了避免出现噪声这种情况，提出限制对比度，如果直方图的bin超过了提前预设好的“限制对比度”，
  那么就将超出的部分剪裁并均匀分布到其他的bin,这样就重构了直方图
"""
# src = cv2.imread('../Img/1686056402582.jpg',cv2.IMREAD_ANYCOLOR)
src = cv2.imread('../Img/1685800648022.jpg',cv2.IMREAD_ANYCOLOR)
src = cv2.imread('../Img/26.jpg',cv2.IMREAD_ANYCOLOR)
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(clipLimit=5.0,tileGridSize=(8,8))
dst = clahe.apply(gray)
cv2.imshow('gray',gray)
cv2.imshow('clahe',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()