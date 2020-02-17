import threading
import os


def removeDir(file_name):
    if not os.path.isdir(file_name):  # os.path.isdir()函数判断某一路径是否为目录
        os.remove(file_name);  # 直接删除文件
    else:
        files = os.listdir(file_name);  # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
        for file in files:
            filePath = os.path.join(file_name, file);  # 拼接路径
            # 这一步很重要 主要作用是拼接目录下的目录
            if os.path.isfile(filePath):  # 判断filepath是否为文件
                os.remove(filePath);  # 删除文件
            elif os.path.isdir(filePath):  # 得到当前目录下的目录
                removeDir(filePath);  # 删除文件夹
        os.rmdir(file_name);  # os.rmdir() 方法用于删除指定路径的目录。仅当这文件夹是空的才可以,否则, 抛出OSError。



if __name__ == '__main__':
    # 指定源目录和目标目录
    # source_dir = input("输入源目录：")
    # print(source_dir)
    # source_file_list = os.listdir()
    # source_file_list = ['19-09-01','19-09-02','19-09-03','19-09-04','19-09-05','19-09-06','19-09-07','19-09-08','19-09-09','19-09-10']
    source_dir = 'D:\img\indexcache'
    for file_name in source_dir:
        print(file_name)
        del_thread = threading.Thread(target=removeDir, args=(file_name,))
        print(del_thread)
        del_thread.start()
    else:
        print("请确认源目录是否存在或者是否拼写错误")