# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-06


# 通信账单使用的是别人的资源，@Jaccorot
import xlrd
def sum_phone(file):
    book = xlrd.open_workbook(file, encoding_override="utf-8")
    sheet = book.sheets()[0]
    rows = sheet.nrows
    cols = sheet.ncols
    sum_talk = 0
    sum_cost = 0
    for i in xrange(1, rows):
        seconds = int(sheet.cell_value(i, 2))
        sum_talk += seconds
        cost = float(sheet.cell_value(i, 3))
        sum_cost += cost
    return (sum_talk,sum_cost)

if __name__ == "__main__":
    file = "src.xls"
    res = sum_phone(file)
    print "通话时长共为：",res[0],"秒"
    print "话费共为：",res[1],"元"
