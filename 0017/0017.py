# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-03

import xlrd,codecs
from lxml import etree


def get_data(file):
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheets()[0]
    student_dict = {}
    for i in xrange(sheet.nrows):
        lst = []
        print sheet.row_len(i)
        for j in xrange(sheet.row_len(i)):
            if j == 0:
                continue
            if j == 1:
                lst.append(sheet.cell_value(i,j).encode("utf-8"))
                continue
            lst.append(int(sheet.cell_value(i,j)))
        student_dict[sheet.cell_value(i,0)] = lst
    return student_dict

def build_xml(data):
    xml = codecs.open("student.xml","w","utf-8")
    root = etree.Element("root")
    student_xml = etree.ElementTree(root)
    student = etree.SubElement(root, 'student')
    student.append(etree.Comment(u'学生信息表\n\"id\": [名字，数学，语文，英语]'))
    student.text = str(data)
    xml.write(etree.tounicode(student_xml.getroot()))
    xml.close()

if __name__ == "__main__":
    data = get_data("student.xls")
    build_xml(data)