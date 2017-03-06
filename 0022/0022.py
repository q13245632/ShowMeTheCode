# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-06


import os
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8) # 64 bits.

    assert 8 == len(salt)
    assert isinstance(salt, str)

    if isinstance(password, unicode):
        password = password.encode('UTF-8')

    assert isinstance(password, str)

    result = password
    for i in xrange(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result


def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:8])


if __name__ == "__main__":
    password = raw_input("输入密码\n")
    encryptpassword = encrypt_password(password=password)
    again = raw_input("再次输入密码\n")
    print "设置成功" if validate_password(encryptpassword,again) else "出错，请重新设置"