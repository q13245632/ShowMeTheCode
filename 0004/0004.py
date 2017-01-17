# -*-coding:utf8 -*-
import re
from collections import Counter


def word_count(content):
    word_pattern = r'[a-zA-Z-]+'
    words = re.findall(word_pattern, content)
    return Counter(words).items()

if __name__ == '__main__':
    txt = open('test.txt', 'r').read().lower()
    for k in word_count(txt):
        print k
