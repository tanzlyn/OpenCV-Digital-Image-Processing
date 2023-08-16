#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2
def integral(img):
    rows, cols = img.shape
    # 行积分运算
    inteImageC = np.zeros(img.shape, np.float32)
    for r in range(rows):
        for c in range(cols):
            if c == 0:
                inteImageC[r][c] = img[r][c]
            else:
                inteImageC[r][c] = inteImageC[r][c - 1] + img[r][c]
    # 列积分计算
    inteImage = np.zeros(img.shape, np.float32)
    for c in range(cols):
        for r in range(rows):
            if r == 0:
                inteImage[r][c] = inteImageC[r][c]
            else:
                inteImage[r][c] = inteImage[r - 1][c] + inteImageC[r][c]
    # 上边和左边进行补零
    inteImage_0 = np.zeros((rows + 1, cols + 1), np.float32)
    inteImage_0[1:rows + 1, 1:cols + 1] = inteImage
    return inteImage_0


def fastMeanBlur(img, winSize, borderType=cv2.BORDER_DEFAULT):
    halfH = int((winSize[0] - 1) / 2)
    halfW = int((winSize[1] - 1) / 2)
    ratio = 1.0 / (winSize[0] * winSize[1])
    # 边界扩充
    paddImage = cv2.copyMakeBorder(img, halfH, halfH, halfW, halfW, borderType)
    # 图像积分
    paddIntegral = integral(paddImage)
    # 图像的高、宽
    rows, cols = img.shape
    # 均值滤波后的结果
    meanBlurImage = np.zeros(img.shape, np.float32)
    r, c = 0, 0
    for h in range(halfH, halfH + rows, 1):
        for w in range(halfW, halfW + cols, 1):
            meanBlurImage[r][c] = (paddIntegral[h + halfH + 1][w + halfW + 1] +
                                   paddIntegral[h - halfH][w - halfW] -
                                   paddIntegral[h + halfH + 1][w - halfW] -
                                   paddIntegral[h - halfH][w + halfW + 1]) * ratio
            c += 1
        r += 1
        c = 0
    return meanBlurImage


img = cv2.imread("../Img/0230610170721.png", 0)
cv2.imshow("img", img)
# 使用定义的函数
blur = fastMeanBlur(img, (9, 9))
blur = np.round(blur)
blur = blur.astype(np.uint8)
# # 使用OpenCV提供的函数
blur2 = cv2.blur(img, (9, 9)) # 均值滤波
blur3 = cv2.boxFilter(img,0,(9,9)) # 快速均值滤波
cv2.imshow("blur", blur)
cv2.imshow("blur2", blur2)
cv2.imshow("blur3", blur3)
cv2.waitKey(0)
cv2.destroyAllWindows()
