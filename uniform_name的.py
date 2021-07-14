import os


# 批量更改二级目录下文件名
# 应用场景：二级目录的文件名一级目录名
def uniform_name(path):
    # 读取一级目录文件
    file_name = os.listdir(path)
    for file in file_name:
        # 过滤".DS_Store"
        if file == ".DS_Store":
            continue
        # print(file)
        path1 = os.path.join(path, file)
        # print(path1)
        # 读取二级目录文件
        file_name_name = os.listdir(path1)
        # print(file_name_name)
        for file_file in file_name_name:
            # print(file_file)
            # 更改后缀名为.png的文件名
            if file_file[-4:] == '.png':
                old_name = os.path.join(path1, file_file)
                file_file_change = file + '.png'
                new_name = os.path.join(path1, file_file_change)
                os.rename(old_name, new_name)
            # 更改后缀名为.json的文件名
            elif file_file[-5:] == '.json':
                old_name = os.path.join(path1, file_file)
                file_file_change = file + '_label.json'
                new_name = os.path.join(path1, file_file_change)
                os.rename(old_name, new_name)
            # 更改文件名末尾为_sketch.json的文件名
            elif file_file[-12:] == '_sketch.json':
                old_name = os.path.join(path1, file_file)
                file_file_change = file + '_sketch.json'
                new_name = os.path.join(path1, file_file_change)
                os.rename(old_name, new_name)


if __name__ == "__main__":
    path = './mobile_84000'
    uniform_name(path)