# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-03

import json
import xlwt


with open("numbers.txt","rb") as f:
    book = xlwt.Workbook()
    sheet1 = book.add_sheet("sheet1", cell_overwrite_ok=True)
    content = f.read().decode("gb2312")
    data = json.loads(content)
    for i in xrange(len(data)):
        for j in xrange(len(data[i])):
            sheet1.write(i, j, data[i][j])
    book.save("numbers.xls")