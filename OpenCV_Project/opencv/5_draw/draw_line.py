#!/user/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np
img = np.zeros((460,680,3),np.uint8)  # 图像大小是(y,x)
# 画线，坐标为（x,y)
cv2.line(img,(10,20),(300,400),(0,255,0),5,16)
cv2.line(img,(80,20),(30,460),(0,0,255),1,4)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
