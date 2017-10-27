#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# From: https://zhuanlan.zhihu.com/p/24425116

# 缩放，裁剪和补边

# 缩放通过cv2.resize()实现，裁剪则是利用array自身的下标截取实现，
# 此外OpenCV还可以给图像补边，这样能对一幅图像的形状和感兴趣区域实现各种操作。
# 下面的例子中读取一幅400×600分辨率的图片，并执行一些基础的操作

import cv2

# 读取一张照片
img = cv2.imread('images/fruits.png')

# 缩放成200x200的方形图像
img_200x200 = cv2.resize(img, (200, 200))

# 不直接指定缩放后大小，通过fx和fy指定缩放比例，0.5则长宽都为原来一半
# 等效于img_200x300 = cv2.resize(img, (300, 200))，注意指定大小的格式是(宽度,高度)
# 插值方法默认是cv2.INTER_LINEAR，这里指定为最近邻插值
img_200x300 = cv2.resize(img, (0, 0), fx=0.5, fy=0.5,
                              interpolation=cv2.INTER_NEAREST)

# 在上张图片的基础上，上下各贴50像素的黑边，生成300x300的图像
img_300x300 = cv2.copyMakeBorder(img, 50, 50, 0, 0,
                                       cv2.BORDER_CONSTANT,
                                       value=(0, 0, 0))

# 对照片中树的部分进行剪裁
patch_tree = img[20:150, -180:-50]

cv2.imwrite('tmp/fruits_cropped_tree.jpg', patch_tree)
cv2.imwrite('tmp/fruits_resized_200x200.jpg', img_200x200)
cv2.imwrite('tmp/fruits_resized_200x300.jpg', img_200x300)
cv2.imwrite('tmp/fruits_bordered_300x300.jpg', img_300x300)