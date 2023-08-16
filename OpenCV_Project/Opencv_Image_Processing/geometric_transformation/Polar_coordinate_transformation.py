#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
笛卡尔坐标和极坐标是两种不同的描述平面上点位置的方式。

笛卡尔坐标系是平面直角坐标系，用两个垂直的轴（通常是x轴和y轴）来描述平面上任意一点的位置。
每个点的坐标用一个有序的数对 (x,y) 来表示，其中第一个数表示点在x轴上的距离，第二个数表示点在y轴上的距离。

极坐标系则是将平面上的点描述为一个距离和一个角度的组合。
用极坐标系描述点的方式是将点与原点的连线看作是一个半径，
而这个半径与x轴的夹角（通常用弧度表示）就是点的极角。点的坐标用一个有序的数对 (r,θ) 来表示，
其中r表示点到原点的距离，θ表示点与x轴的夹角。
"""
"""
极坐标变换：通常用来校正图像中圆形物体或者被包含在圆环中的物体
"""
import cv2
import numpy as np
import math

# 1.将笛卡尔坐标转化为极坐标

# 举例：(11,13)以(3,5)为中心进行极坐标变换：
r = math.sqrt(math.pow(11-3,2)+math.pow(13-5,2))
theta = math.atan2(13-5,11-3)/math.pi*180
print(r, "\n", theta)

# 举例：计算（0,0）（1,0）（2,0）（0,1）（1,1）（2,1）（0,2）（1,2）（2,2）这9个点以（1,1）为中心进行的极坐标变换。
x = np.array([[0,1,2],[0,1,2],[0,1,2]],np.float64)-1
y = np.array([[0,0,0],[1,1,1],[2,2,2]],np.float64)-1
r, theta = cv2.cartToPolar(x,y,angleInDegrees=True)
print(r, "\n", theta)


# 2.将极坐标转换为笛卡尔坐标

# 举例：已知极坐标（角度，半径）中的（30,10）、（31,10）、（30,11）、（31,11）.
# 求笛卡尔坐标中哪四个坐标以（-12,15）为中心经过极坐标变换后得到这四个坐标
angle = np.array([[30,31],[30,31]],np.float32)
r = np.array([[10,10],[11,11]],np.float32)
x,y = cv2.polarToCart(r,angle,angleInDegrees=True)
x = x-12
y = y+15
print(x, "\n", y)


# 3.利用极坐标变换对图像进行变换

a = np.array([[1,2],[3,4]])
b = np.tile(a,(2,3)) # 将a分别在垂直方向和水平方向上复制2次和3次
print(b)

# 参数分别为：输入图像、极坐标变换中心、二元元组(代表最大距离和最小距离）、rstep=r的变换步长，
# thetastep=角度的变换步长，默认为1/4,

def polar(I,center,r,theta=(0,360),rstep=1.0,thetastep=360.0/(180*8)):
    # 获取极坐标变换中心坐标
    cx, cy = center

    # 得到距离最小、最大范围
    minr, maxr = r

    # 角度的范围
    mintheta,maxtheta = theta

    # 输出图像的宽、高
    H = int((maxr-minr)/rstep)+1
    W = int((maxtheta-mintheta)/thetastep)+1
    O = 125*np.ones((H,W),I.dtype)
    print(O)
    # 极坐标变换
    r = np.linspace(minr,maxr,H)
    r = np.tile(r,(W,1))
    r = np.transpose(r)
    theta = np.linspace(mintheta,maxtheta,W)
    theta = np.tile(theta,(H,1))
    x,y = cv2.polarToCart(r,theta,angleInDegrees=True)

    # 最近邻插值
    for i in range(H):
        for j in range(W):
            px = int(round(x[i][j])+cx)
            py = int(round(y[i][j])+cy)
            if((px>=0 and px<=w-1) and (py>=0 and py<=h-1)):
                O[i][j] = I[py][px]

    return O



I = cv2.imread("../Img/1685776846611.jpg")
i = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
h,w = I.shape[:2]
# 极坐标变换中心
cx, cy = 550,550  # 圆形
cv2.circle(I,(int(cx),int(cy)),10,(255.0,0,0),3)
#j
O = polar(i,(cx,cy),(0,550))  # 范围
O = cv2.flip(O,0)
# cv2.imshow('I',I)
# cv2.imshow('O',O)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 3.1 线性极坐标变换linearPolar
import cv2

src = cv2.imread('../Img/1685776846611.jpg')
# cv2.imshow("src",src)
dst = cv2.linearPolar(src,(550,550),550,cv2.INTER_LINEAR) # 变换中心，变换的最大距离
# cv2.imshow('dst',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 3.2 对数极坐标函数logPolar
import cv2

src = cv2.imread('../Img/1685776846611.jpg')
cv2.imshow("src",src)
dst = cv2.logPolar(src,(550,550),150,cv2.INTER_LINEAR) # 变换中心，系数（大一点）
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

