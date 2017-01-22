# -*-coding:utf8 -*-
# author: yushan
# date: 2017-01-22
# summary: 找到文档中重要的词语
import os
import os.path
import re
from collections import Counter


def word_count(content):
    word_pattern = r'[a-zA-Z-]+'
    words = re.findall(word_pattern, content)
    return Counter(words).most_common(1)


root_dir = "text"
lst_dir = os.listdir(root_dir)
for i in lst_dir:
    file_name = "text\\" + i
    with open(file_name) as f:
        content = f.read().lower()
        (word, freq) = word_count(content)[0]
        print "在" + i + "中，最重要的词是" + word + ",出现了" + str(freq) + "次"