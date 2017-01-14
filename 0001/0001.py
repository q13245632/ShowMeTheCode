# -*-coding:utf8 -*-
# Author: yushan
# Time: 2017/1/14
import string
import random


def generate(n):
    item = string.letters + string.digits
    lst = ["-".join(["".join(random.sample(item, 5)) for _ in xrange(5)]) for _ in xrange(n)]
    for k in lst:
        print k
    return lst

if __name__ == "__main__":
    m = 200
    generate(m)
