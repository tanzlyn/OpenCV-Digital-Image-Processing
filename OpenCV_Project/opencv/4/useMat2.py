#!/user/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('../Guangzhou.jfif')

# shape属性中包括三个信息
# 高度、长度、通道数
print(img.shape)

# 图像占用多大空间
# 高度*长度*通道数
print(img.size)

# 图像的每个元素的位深
print(img.dtype)