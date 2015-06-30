#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Url__ = 'Http://www.purpleroc.com'
__author__ = 'Tracy_梓朋'
'''
逆向新手
250
小白是一名逆向新手，他希望能够提升自己的实力。于是他就写了一个简单的程序来锻炼自己。现在他把这个程序给了你，聪明的你能否解开小白题目的答案呢?


    程序写的挺好的,思路也挺好的.
    程序运行,首先内置了几个int用来干扰调试.而后,为了增加静态难度,把kernel32.dll\ loadlibrary\ messagebox\ SetUnhandleExceptionFilter
    而且,在目测为检测key的地方,故意构造了一个异常.
    让人不明白作者要判断的内容.而且防止调试.
    正真的判断在异常触发的那个函数里.
    只要输入的值通过一个简单的算法让结果为1168863433,就会弹出 :)  的对话框.
    注册机算法如下.
'''

import random
# value = 0x45AB70C9   1168863433
target = 1168863433
#rand = random.randint(4, 10)

def get_key(value):
    flag = []
    while (value):
        rand = 5
        if (value + 48) < 57:
            x = value + 48
            value = 0
            flag.append(chr(x))
        else:
            x = (value + 48)%10
            if (rand*10 + x) >57:
                rand = 4
                x = rand*10 + x
            else:
                x = rand*10 + x
            value = (value + 48 - x)/10
            flag.append(chr(x))
    return flag

def org_alg(str):
    ret = 0
    for i in str:
        ret = 10*ret + ord(i) - 48
    return ret

if __name__ == '__main__':
    if org_alg("".join(get_key(target))[::-1]) == target:

        print "Your Key is: "+"".join(get_key(target))[::-1]
    #print org_alg("AAA")
    #print org_alg("A@K")