# -*-coding:utf8 -*-
import string
import random

def generate(n):
    item = string.letters + string.digits
    key_item = "".join(random.sample(item,5))
    lst = ["-".join(["".join(random.sample(item,5)) for _ in xrange(5)]) for i in xrange(n)]
    for k in lst:
        print k
    return lst

if __name__ == "__main__":
    n = 200
    generate(200)
