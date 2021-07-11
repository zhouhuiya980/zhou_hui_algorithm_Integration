import os
import cv2
import json
import numpy as np
import pandas as pd
from natsort import ns, natsorted
from tkinter import _flatten


# 过滤后缀名，防止读取文件错误
def file_name_filter(file_name):
    if file_name[-4:] == '.png':
        return True
    else:
        return False


# 获取文件路径，读取文件
def get_file_s(path):
    file_names = os.listdir(path)
    # 按目录顺序读取文件名
    file_s = natsorted(file_names, alg=ns.PATH)
    return file_s


def compute(path):
    file_s = get_file_s(path)
    # per_image_Rmean = []
    # per_image_Gmean = []
    per_image_Bmean = []
    for file_name in file_s:
        if file_name_filter(file_name) == True:
            # 读取图像数据，1为彩色图片，0为灰度图
            img = cv2.imread(os.path.join(path, file_name), 1)
            # 计算B通道上均值
            per_image_Bmean.append(np.mean(img[:, :, 0]))
            # per_image_Gmean.append(np.mean(img[:, :, 1]))
            # per_image_Rmean.append(np.mean(img[:, :, 2]))
        else:
            continue
    return per_image_Bmean


if __name__ == "__main__":
    '''根据原始图片和发布图片计算每张图片的B通道上均值，根据均值相等匹配相同图片'''
    path1 = './mobile_83000_84000'
    path2 = './mobile_83000_84000_post_picture'
    # 获取图片B通道上均值
    dict_index1 = compute(path1)
    dict_index2 = compute(path2)
    dict_index1_value1 = []
    dict_index2_value2 = []
    # 获取文件顺序下图片名称
    for files1 in natsorted(os.listdir(path1), alg=ns.PATH):
        dict_index1_value1.append(files1)
    # 原始图片中的B通道上的均值以及图片对应名称转化为字典
    dict1 = dict(zip(dict_index1, dict_index1_value1))
    # 将字典转化为DataFrame,并根据发布图片的B通道上均值匹配原始图片名称
    match = pd.DataFrame(dict_index2)
    match.columns = ['per_image_Bmean']
    match['名称'] = match['per_image_Bmean'].map(dict1)
    match_result = match.iloc[:, 1:]
    # match_result.to_excel('./mobile_82000_83000_match_result.xlsx')    将匹配图片名称保存在excel中
    # 将DataFrame转换为列表并降成一维
    match_result_tolist = match_result.values.tolist()
    match_result_tolist_flatten = list(_flatten(match_result_tolist))
    original_picture_name = []
    file_s2 = get_file_s(path2)
    for file in file_s2:
        original_picture_name.append(file)
    dict2 = dict(zip(original_picture_name, match_result_tolist_flatten))
    # 将匹配信息写入字典中
    with open('./mobile_83000_84000.json', 'w') as f:
        f.write(json.dumps(dict2))
