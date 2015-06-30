#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Url__ = 'Http://www.purpleroc.com'
__author__ = 'Tracy_梓朋'

import re

'''
先接出来得到要输入:
iscc_2015_have_fun
然后看到下面这句:
x0r_iscc2015_f0r_pe __3kJoker
写py异或处理
rdata段为: 0x1200-0x1800
居然是依次异或iscc2015中的每一位.
J0ker又教了我一招,如何异或...
'''

data = open("../../FILES/REVERSE/iscc2015.exe", "rb").read()
key = "iscc2015"
re_key = 0x00
for i in range(len(key)):
    re_key ^= ord(key[i])

result = []

if __name__ == '__main__':
    for i in range(int(0x1200), int(0x1800)):
        result.append(chr(re_key ^ ord(data[i])))
    #print "".join(result)
    open("../../DATA/RE07.dat","wb").write("".join(result))
    print re.findall(r'flag:.*', "".join(result))[0]