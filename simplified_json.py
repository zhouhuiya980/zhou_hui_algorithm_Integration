import json
import os


# 创建json文件
def create_json(path):
    file_name = os.listdir(path)
    for file in file_name:
        path_1 = './json_result' + '/' + file
        with open(path_1, 'w') as f:
            f.write('')


# 简化json文件格式，只获取json文件中各个标签的（"x1", "y1", "x2", "y2", "name"）
def simplified(path1, path2):
    # 存储标签框坐标及名称
    list1 = ["x1", "y1", "x2", "y2", "name"]
    file_name = os.listdir(path1)
    for file in file_name:
        # 存储转化后的结果字典
        result_dict = {}
        result_dict_index = "labels"
        result_dict_key = []
        path = os.path.join(path1, file)
        # 读取json文件
        json_data = json.load(open(path))
        for i in range(len(json_data['shapes'])):
            # 存储标签框的坐标值及标签名
            list2 = []
            # 读取json文件中每个标签的坐标值并判断大小，坐标值在小的放在左边，坐标值大的放在右边
            if json_data['shapes'][i]['points'][0][0] > json_data['shapes'][i]['points'][1][0]:
                list2.append(json_data['shapes'][i]['points'][1][0])
                if json_data['shapes'][i]['points'][0][1] > json_data['shapes'][i]['points'][1][1]:
                    list2.append(json_data['shapes'][i]['points'][1][1])
                    list2.append(json_data['shapes'][i]['points'][0][0])
                    list2.append(json_data['shapes'][i]['points'][0][1])
                else:
                    list2.append(json_data['shapes'][i]['points'][0][1])
                    list2.append(json_data['shapes'][i]['points'][0][0])
                    list2.append(json_data['shapes'][i]['points'][1][1])
            else:
                list2.append(json_data['shapes'][i]['points'][0][0])
                if json_data['shapes'][i]['points'][0][1] > json_data['shapes'][i]['points'][1][1]:
                    list2.append(json_data['shapes'][i]['points'][1][1])
                    list2.append(json_data['shapes'][i]['points'][1][0])
                    list2.append(json_data['shapes'][i]['points'][0][1])
                else:
                    list2.append(json_data['shapes'][i]['points'][0][1])
                    list2.append(json_data['shapes'][i]['points'][1][0])
                    list2.append(json_data['shapes'][i]['points'][1][1])

            # if json_data['shapes'][i]['points'][0][0] > json_data['shapes'][i]['points'][1][0]:
            #     list2.append(json_data['shapes'][i]['points'][1][0])
            #     list2.append(json_data['shapes'][i]['points'][0][0])
            # else:
            #     list2.append(json_data['shapes'][i]['points'][0][0])
            #     list2.append(json_data['shapes'][i]['points'][1][0])
            # if json_data['shapes'][i]['points'][0][1] > json_data['shapes'][i]['points'][1][1]:
            #     list2.append(json_data['shapes'][i]['points'][1][1])
            #     list2.append(json_data['shapes'][i]['points'][0][1])
            # else:
            #     list2.append(json_data['shapes'][i]['points'][0][1])
            #     list2.append(json_data['shapes'][i]['points'][1][1])

            # 读取标签名称并保存在list2列表中
            list2.append(json_data['shapes'][i]['label'])
            dict1 = dict(zip(list1, list2))
            # print(dict1)
            result_dict_key.append(dict1)
            # print(result_dict_key)
            result_dict[result_dict_index] = result_dict_key
        # print(result_dict)
        # 将字典写入新创建的json中
        json_str = json.dumps(result_dict)
        path3 = path2 + '/' + file
        # print(path3)
        with open(path3, 'w') as json_w:
            json_w.write(json_str)


if __name__ == "__main__":
    path1 = './match_json'
    path2 = './json_result'
    create_json(path1)
    simplified(path1, path2)
