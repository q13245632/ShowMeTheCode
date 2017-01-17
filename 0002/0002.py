# -*-coding:utf8 -*-
import string
import random
import MySQLdb

def generate(n):
    item = string.letters + string.digits
    key_item = "".join(random.sample(item,5))
    lst = ["-".join(["".join(random.sample(item,5)) for _ in xrange(5)]) for i in xrange(n)]
    db = MySQLdb.connect("localhost","root","123456","test")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS KEYCODE")
    create_sql = """CREATE TABLE KEYCODE (
             Id INT PRIMARY KEY AUTO_INCREMENT,
             KEYCODE VARCHAR(30) NOT NULL)"""
    cursor.execute(create_sql)

    for k in lst:
        print k
        insert_sql = "INSERT INTO KEYCODE (KEYCODE) VALUES ('%s')" % k
        cursor.execute(insert_sql)

    db.commit()
    db.close()
    return lst

if __name__ == "__main__":
    n = 200
    generate(200)
