#!/user/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np
img = np.zeros((460,680,3),np.uint8)
# 画矩形
cv2.rectangle(img,(20,20),(200,200),(0,0,255),-1)

# 画圆
cv2.circle(img,(320,240),100,(0,0,255))
cv2.circle(img,(320,240),5,(255,0,0),-1)

#画椭圆
# 顺时针计算
#0度是从左侧开始的
cv2.ellipse(img,(320,240),(100,50),0,0,180,(0,0,255))


cv2.imshow('draw',img)
cv2.waitKey(0)
cv2.destroyAllWindows()