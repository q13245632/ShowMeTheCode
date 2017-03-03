# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-03

import xlrd,codecs
from lxml import etree


def get_data(file):
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheets()[0]
    lst = []
    for i in xrange(sheet.nrows):
        item = []
        for j in xrange(sheet.ncols):
            item.append(int(sheet.cell_value(i,j)))
        lst.append(item)
    return lst

def build_xml(data):
    xml = codecs.open("numbers.xml","w","utf-8")
    root = etree.Element("root")
    numbers_xml = etree.ElementTree(root)
    numbers = etree.SubElement(root, 'numbers')
    numbers.append(etree.Comment(u'数字信息'))
    numbers.text = str(data)
    xml.write(etree.tounicode(numbers_xml.getroot()))
    xml.close()

if __name__ == "__main__":
    data = get_data("numbers.xls")
    build_xml(data)