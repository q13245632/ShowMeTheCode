# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-03

import xlrd,codecs
from lxml import etree


def get_data(file):
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheets()[0]
    city_dict = {}
    for i in xrange(sheet.nrows):
        city_dict[str(sheet.cell_value(i,0))] = sheet.cell_value(i,1).encode("utf-8")
    return city_dict

def build_xml(data):
    xml = codecs.open("city.xml","w","utf-8")
    root = etree.Element("root")
    city_xml = etree.ElementTree(root)
    city = etree.SubElement(root, 'city')
    city.append(etree.Comment(u'城市信息'))
    city.text = str(data)
    xml.write(etree.tounicode(city_xml.getroot()))
    xml.close()

if __name__ == "__main__":
    data = get_data("city.xls")
    build_xml(data)