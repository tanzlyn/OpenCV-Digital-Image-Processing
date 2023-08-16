#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
src = np.array([[123,234,68],[33,51,17],[48,98,234],[129,89,27],[45,167,134]])
src[src>150] = 255
src[src<=150] = 0
print(src)

import numpy as np
import cv2

src = np.array([[123,234,68],[33,51,17],[48,98,234],[129,89,27],[45,167,134]],np.uint8)
#手动设置阈值
threshold = 150
maxval = 255
dst = cv2.threshold(src, threshold, maxval,cv2.THRESH_BINARY)
# Otsu 阈值处理
otsu_threshold = 0
otsuThe,dst_Otsu = cv2.threshold(src,otsu_threshold, maxval,cv2.THRESH_OTSU)
print(otsuThe,dst_Otsu)
# TRIANGLE 阈值处理
tri_threshold = 0
triThe,dst_tri = cv2.threshold(src, tri_threshold, maxval, cv2.THRESH_TRIANGLE)
print(triThe,dst_tri)

'''
输出
98.0                # Otsu 自动计算的阈值
[[255 255   0]
 [  0   0   0]
 [  0   0 255]
 [255   0   0]
 [  0 255 255]]
232.0 							# Triangle自动计算的阈值
[[  0 255   0]
 [  0   0   0]
 [  0   0 255]
 [  0   0   0]
 [  0   0   0]]
'''
