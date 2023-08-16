#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
投影变换(三维）：
"""
import cv2
import numpy as np
import math
image = cv2.imread('../Img/7418.jpeg')
h,w = image.shape[:2]
print(h)
print(w)
# 原图的4个点，与投影变换的4个点
src = np.array([[0,0],[w-1,0],[0,h-1],[w-1,h-1]],np.float32)
dst = np.array([[550,50],[600,50],[0,500],[w-1,500]],np.float32)

# 计算投影变换矩阵
p = cv2.getPerspectiveTransform(src,dst)

# 利用计算出的投影变换矩阵进行头像的投影变换
r = cv2.warpPerspective(image,p,(w,h),borderValue=125)
cv2.imshow('image',image)
cv2.imshow('warpPerspective',r)
cv2.waitKey(0)
cv2.destroyAllWindows()