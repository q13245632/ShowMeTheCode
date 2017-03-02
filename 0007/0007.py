# -*-coding:utf8 -*-
# author: yushan
# date: 2017-03-02


# 统计代码及注释行数，只统计python代码格式
# 03/02 添加Java的统计
import os
def get_files(path):
    file_path = os.listdir(path)
    files = []
    for i in file_path:
        cur_path = path + "/" + i
        print cur_path
        if os.path.isfile(cur_path):
            files.append(cur_path)
        elif os.path.isdir(cur_path):
            files += get_files(cur_path)
    return files


def count(item):
    lines, blanks, notes = 0, 0, 0
    with open(item, 'rb') as f:
        if item.split('.')[-1] == 'java':
            for line in f.readlines():
                lines += 1
                line = line.strip()
                if line == '':
                    blanks += 1
                    continue
                if line[0] == "/":
                    notes += 1
                    continue
        elif item.split('.')[-1] == 'py':
            for line in f.readlines():
                lines += 1
                line = line.strip()
                if line == '':
                    blanks += 1
                    continue
                if line[0] == "#" or line[0] == '/':
                    notes += 1
                    continue
    return (lines,blanks,notes)


if __name__ == "__main__":
    path = "test"
    files = get_files(path)
    for file in files:
        lines,blanks,notes = count(file)
        print "该文件",file,"统计的代码数："
        print "代码行数为",lines
        print "空格行数为", blanks
        print "注释行数为", notes
