#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Url__ = 'Http://www.purpleroc.com'
__author__ = 'Tracy_梓朋'

# easy？
# 50
# 密文mzdvezc是用仿射函数y=5x+12加密得到的，试对其解密。



def affine(a, b):
    pwd_dic = {}
    for i in range(26):
        pwd_dic[chr(((a*i+b)%26)+97)] = chr(i+97)
    return pwd_dic

if __name__ == '__main__':
    pwd_dic = {}
    pwd = "mzdvezc"
    plain = []
    pwd_dic = affine(5, 12)
    for i in pwd:
        plain.append(pwd_dic[i])
    print "You Flag is: " + "".join(plain)