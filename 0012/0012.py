# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-03


def filtered_words(file):
    words_lst = []
    with open(file,'r') as f:
        for line in f.readlines():
            words_lst.append(line.strip().decode("gb2312").encode('utf-8'))
    return words_lst

def change_word(sentence,lst):
    sen_later = sentence
    for i in lst:
        if i.isalpha():
            sen_later = sen_later.replace(i,"*")
        else:
            con = "*" * (len(i) / 3)
            sen_later = sen_later.replace(i,str(con))
    return sen_later

if __name__ == "__main__":
    sen = raw_input().strip()
    lst = filtered_words("filtered_words.txt")
    new = change_word(sen,lst)
    print new