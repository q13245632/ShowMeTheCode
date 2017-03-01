# -*-coding:utf8 -*-
# author: yushan
# date: 2017-03-01


# 统计代码及注释行数，只统计python代码格式
import os
def get_files(path):
    file_path = os.listdir(path)
    files = []
    for i in file_path:
        cur_path = path + "/" + i
        if os.path.isfile(cur_path):
            files.append(cur_path)
        elif os.path.isdir(cur_path):
            files += get_files(cur_path)
    return files


def count(files):
    lines, blanks, notes = 0, 0, 0
    for item in files:
        with open(item,'rb') as f:
            for line in f.readlines():
                lines += 1
                line = line.strip()
                if line == '':
                    blanks += 1
                    continue
                if line[0] == '#' or line[0] == '/':
                    notes += 1
                    continue
    return (lines,blanks,notes)

if __name__ == "__main__":
    path = "test"
    files = get_files(path)
    lines,blanks,notes = count(files)
    print "代码行数为",lines
    print "空格行数为", blanks
    print "注释行数为", notes
