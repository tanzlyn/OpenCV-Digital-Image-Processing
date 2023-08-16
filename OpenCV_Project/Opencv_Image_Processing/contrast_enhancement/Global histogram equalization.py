#!/user/bin/env python3
# -*- coding: utf-8 -*-
import math
import cv2
import numpy as np
"""
全局直方图均衡化（HE）：
可以更好的提高对比度，但是暗区域的噪声可能会放大，变得清晰，而亮区域可能会损失信息。
为了提出该问题，提出了CLAHE
"""
"""
实现步骤：
1.计算图像的灰度直方图
2.计算灰度直方图的累加直方图
3.根据累加直方图的直方图均衡化原理得到输入灰度级和输出灰度级之间的映射关系
4.根据第三步得到的灰度级映射关系，循环得到输出图像的每个像素灰度级。
"""

# def equalHist(image):
#     # 灰度图像矩阵的高、低
#     rows,cols = image.shape[:2]
#     # 1.计算灰度直方图
#     grayHist = cv2.calcHist(image,[0],None,[255],[0,256])
#     # 2.计算累加灰度直方图
#     zeroCumuMoent = np.zeros([256],np.uint32)
#     for p in range(256):
#         if p == 0:
#             zeroCumuMoent[p] = grayHist[0]
#         else:
#             zeroCumuMoent[p] = zeroCumuMoent[p-1] + grayHist[p]
#     # 3.根据累加直方图的直方图均衡化原理得到输入灰度级和输出灰度级之间的映射关系
#     outPut_q = np.zeros([256],np.uint8)
#     cofficient = 256.0/(rows*cols)
#     for p in range(256):
#         q = cofficient*float(zeroCumuMoent[p])-1
#         if q>=0:
#             outPut_q[p] = math.floor(q)
#         else:
#             outPut_q = 0
#
#     # 4.根据第三步得到的灰度级映射关系，循环得到输出图像的每个像素灰度级。
#     equalHistImage = np.zeros(image.shape,np.uint8)
#     for r in range(rows):
#         for c in range(cols):
#             equalHistImage[r][c] = outPut_q[image[r][c]]
#
#     return equalHistImage
#
# image = cv2.imread('../Img/1685795920851.jpg')
# image = equalHist(image)
# cv2.imshow('image',image)


# 全局直方图均衡化
def equalHist(img, z_max = 255): # z_max = L-1 = 255
    # 灰度图像矩阵的高、宽
    H, W = img.shape
    # S is the total of pixels
    S = H * W

    out = np.zeros(img.shape)
    sum_h = 0
    for i in range(256):
        ind = np.where(img == i)
        sum_h += len(img[ind])
        z_prime = z_max / S * sum_h
        out[ind] = z_prime

    out = out.astype(np.uint8)
    return out

image = cv2.imread('../Img/1686370964745.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',image)
image1 = equalHist(image)
image2 = cv2.equalizeHist(image,cv2.CV_8UC1)
cv2.imshow('image1',image1)
cv2.imshow('image2',image2)
cv2.waitKey(0)
cv2.destroyAllWindows()