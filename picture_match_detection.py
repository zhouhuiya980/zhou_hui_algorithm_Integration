# -*- coding:utf-8 -*-
import os
import cv2
import numpy as np
from natsort import ns, natsorted


# 过滤后缀名，防止读取文件错误
def file_name_filter(file_name):
    if file_name[-4:] == '.png':
        return True
    else:
        return False


# 获取文件路径，读取文件
def get_file_s(path):
    file_names = os.listdir(path)
    file_s = natsorted(file_names, alg=ns.PATH)
    return file_s


# 按目录顺序读取文件名
def detection(path1, path2):
    file_s1 = get_file_s(path1)
    file_s2 = get_file_s(path2)
    # 存储两张图片的像素差值之和
    match_result = []
    # print(file_s1)
    # print(file_s2)
    for file_s1_name, file_s2_name in zip(file_s1, file_s2):
        # print(file_s1_name)
        # print(file_s2_name)
        if file_name_filter(file_s1_name) == True and file_name_filter(file_s2_name) == True:
            img1 = cv2.imread(os.path.join(path1, file_s1_name), 1)
            img2 = cv2.imread(os.path.join(path2, file_s2_name), 1)
            # 获取两张图片像素差值
            err = np.abs(img1 - img2)
            err_sum = np.sum(err)
            match_result.append(err_sum)
        else:
            continue
    return match_result


if __name__ == "__main__":
    '''两个数据集中相同图片做差，检测是否相等'''
    path1 = './mobile_82000_83000'
    path2 = './mobile_82000_83000_detection'
    result = detection(path1, path2)
    print(result)
