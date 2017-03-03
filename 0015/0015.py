# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-03

import json
import xlwt


with open("city.txt","rb") as f:
    book = xlwt.Workbook()
    sheet1 = book.add_sheet("sheet1", cell_overwrite_ok=True)
    content = f.read().decode("gb2312")
    data = json.loads(content)
    data = sorted(data.items(),key=lambda k:k[0])
    print data
    i = 0
    for item in data:
        k,v = item
        sheet1.write(i,0,k)
        sheet1.write(i,1,v)
        i += 1
    book.save("city.xls")