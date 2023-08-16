#!/user/bin/env python3
# -*- coding: utf-8 -*-
import cv2

# 创建VideoWriter为写多媒体文件
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
vw = cv2.VideoWriter('./out.mp4',fourcc,25,(1080,720))
# 创建窗口
cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640,360)
# 获取视频设备
cap = cv2.VideoCapture(0)
# 从多媒体文件中读取视频帧
# cap = cv2.VideoCapture()# 视频文件地址

#判断摄像头是否为打开状态
while cap.isOpened():
    ret ,frame = cap.read()
    if ret == True:
        # 将视频帧在窗口显示
        cv2.imshow('video',frame)
        #写数据到多媒体文件
        vw.write(frame)
        #等待键盘事件，如果为q，退出
        key = cv2.waitKey(5)
        if(key & 0xFF == ord('q')):
            break
    else:
        break

# 释放Videocapture
cap.release()
vw.release()
cv2.destroyAllWindows()
