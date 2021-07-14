import os
import shutil
from natsort import ns, natsorted


# 将与'./all3/imgs'图片文件夹匹配的'./mobile_84000'json文件保存在'./all3/sketch_jsons'中
def intergration(path1, path2):
    file_name_1 = os.listdir(path1)
    # 按文件顺序读取文件名
    file_s = natsorted(file_name_1, alg=ns.PATH)
    file_name_2 = os.listdir(path2)
    file_name_1_list = []
    for file_1 in file_s:
        # 去掉文件file_1的后缀名保存在列表中
        file_name_1_list.append(file_1.split('.')[0])
    for file_name_1_list_element in file_name_1_list:
        for file_2 in file_name_2:
            if file_name_1_list_element == file_2:
                path3 = os.path.join(path2, file_2)
                path4 = file_2 + '_sketch.json'
                path = os.path.join(path3, path4)
                shutil.copy(path, './all3/sketch_jsons')


if __name__ == "__main__":
    path1 = './all3/imgs'
    path2 = './mobile_84000'
    intergration(path1, path2)
