# -*-coding:utf8 -*-
# author: yushan
# date: 2017-03-02

def filtered_words(word,file):
    words_lst = []
    with open(file,'r') as f:
        for line in f.readlines():
            words_lst.append(line.strip().decode("gb2312").encode('utf-8'))
    return words_lst.__contains__(word)


if __name__ == "__main__":
    file = 'filtered_words.txt'
    word = str(raw_input().strip())
    if filtered_words(word,file):
        print "Freedom"
    else:
        print "Human Rights"