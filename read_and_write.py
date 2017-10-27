#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# From: https://zhuanlan.zhihu.com/p/24425116

import cv2

# 读取一张400x600分辨率的图像
color_img = cv2.imread('images/fruits.png')
print(color_img.shape)

# 直接读取单通道
gray_img = cv2.imread('images/fruits.png', cv2.IMREAD_GRAYSCALE)
print(gray_img.shape)

# 把单通道图片保存后，再读取，仍然是3通道，相当于把单通道值复制到3个通道保存
cv2.imwrite('tmp/fruits_grayscale.jpg', gray_img)
reload_grayscale = cv2.imread('images/fruits.png')
print(reload_grayscale.shape)

# cv2.IMWRITE_JPEG_QUALITY指定jpg质量，范围0到100，默认95，越高画质越好，文件越大
cv2.imwrite('tmp/fruits_imwrite.jpg', color_img, (cv2.IMWRITE_JPEG_QUALITY, 80))

# cv2.IMWRITE_PNG_COMPRESSION指定png质量，范围0到9，默认3，越高文件越小，画质越差
cv2.imwrite('tmp/fruits_imwrite.png', color_img, (cv2.IMWRITE_PNG_COMPRESSION, 5))