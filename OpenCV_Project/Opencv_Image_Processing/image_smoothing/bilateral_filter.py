#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import math
import cv2
# 构建空间距离权重模板
def getClosenessWeight(sigma_g,H,W):
    r,c = np.mgrid[0:H:1,0:W:1]
    r -= (H-1)//2
    c -= (W-1)//2
    closeWeight = np.exp(-0.5*(np.power(r,2)+np.power(c,2))/math.pow(sigma_g,2))
    return closeWeight

def bfltGray(I,H,W,sigma_g,sigma_d):
    #构建空间距离权重模板
    closenessWeight=getClosenessWeight(sigma_g,H,W)
    #模板的中心点位置
    cH = (H - 1) // 2 #//表示整数除法
    cW = (W - 1) // 2
    #图像矩阵的行数和列数
    rows,cols=I.shape[:2]
    #双边滤波后的结果
    bfltGrayImage=np.zeros(I.shape,np.float32)
    for r in range(rows):
        for c in range(cols):
            pixel=I[r][c]
            #判断边界
            rTop=0 if r-cH<0 else r-cH
            rBottom=rows-1 if r+cH>rows-1 else r+cH
            cLeft=0 if c-cW<0 else c-cW
            cRight=cols-1 if c+cW>cols-1 else c+cW
            # 权重模板作用的区域
            region=I[rTop:rBottom+1,cLeft:cRight+1]
            #构建灰度值相似性的权重因子
            similarityWeightTemp=np.exp(-0.5*np.power(region-pixel,2.0)/math.pow(sigma_d,2))
            #similarityWeightTemp = np.exp(-0.5 * np.power(region - pixel, 2.0) / math.pow(sigma_d, 2))
            closenessWeightTemp=closenessWeight[rTop-r+cH:rBottom-r+cH+1,cLeft-c+cW:cRight-c+cW+1]
            #两个权重模板相乘
            weightTemp=similarityWeightTemp*closenessWeightTemp
            #归一化权重模板
            weightTemp=weightTemp/np.sum(weightTemp)
            #权重模板和对应的领域值相乘求和
            bfltGrayImage[r][c]=np.sum(region*weightTemp)
    return bfltGrayImage

image = cv2.imread('../Img/1686474224093.jpg')
cv2.imshow('image',image)
image1 = cv2.split(image)[1]#蓝通道
image1 = image1/255.0
float_image = image1.astype('float32')
bfltImahe = bfltGray(image1,33,33,19,0.2)
image2 = cv2.bilateralFilter(float_image,33,0.2,19)
cv2.imshow('bflt',bfltImahe)
cv2.imshow('bilateral',image2)
cv2.waitKey(0)
cv2.destroyAllWindows()