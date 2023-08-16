#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
图像平滑：
每幅图像都包含某种程度的噪声，噪声可以理解为由一种或者多种原因造成的（灰度值的随机变换）
大多数情况下，通过平滑技术（滤波技术）进行抑制或者去除
常用的平滑技术包括：
"""

# 1.卷积的三种形式：
# full卷积:I和K的卷积，K旋转180°得到K‘，然后和CNN一样
# valid卷积：I全部覆盖K’
# same卷积：对K‘设置一个锚点，将这个锚点与I的每个元素逐个相乘
import numpy as  np
from scipy import signal
I = np.array([[1,2],[3,4]],np.float32)
H1,W1 = I.shape[:2]
K = np.array([[-1,-2],[2,1]],np.float32)
H2,W2 = K.shape[:2]
c_full = signal.convolve2d(I,K,mode='full') #
kr,kc = 0,0
c_same = c_full[H2-kr-1:H1+H2-kr-1,W2-kc-1:W1+W2-kc-1]
print(c_full)
print(c_same)

# 2.可分离卷积：
# 卷积核至少由两个尺寸比它小的卷积核full卷积而成，并且在计算过程中在所有边界处均匀进行扩充零的操作，则是可分离卷积核。
# full卷积不满足交换律，但是一维水平方向和一维垂直方向上的卷积核full是满足交换律的

import numpy as np
from scipy import signal
kernel1 = np.array([[1,2,3]],np.float32)
kernel2 = np.array([[4,5,6]],np.float32)
# 计算两个核的全卷积
kernel = signal.convolve2d(kernel1,kernel2,mode='full')
print(kernel)

# 离散卷积的性质
# full卷积的性质
#
