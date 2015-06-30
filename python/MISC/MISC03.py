#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Url__ = 'Http://www.purpleroc.com'
__author__ = 'Tracy_梓朋'

'''
道之道
300

天下万物生于有，有生于无，有序常蕴于无序之中。

这题,我也不知道要怎么描述了,额,刚开始看到rot13哈以为要全部rot13一次呢,然后就用vi给图片rot13加了个密.
再打开,发现确实有些地方变了,然后就开始纠结非字母段该如何~
好一会儿后,无果.
然后用stegsolve看了下data提取.发现了PK,哎╮(╯▽╰)╭卧槽.
然后提出来后总觉得不对.就手动修zip,还不对.然后就看了下其他颜色通道.
然后发现,其他里面也有数据.把rgb1全部提取出来差不多刚好是个zip了.然后,还是不太对.
看各个单颜色通道.把有数据的提取出来,人工组合.....

后~~~~尼玛,还是有点问题.然后脑洞打开,将所有提取到的文件内容依次亦或.终于看起来正常了点.
但还是解密失败.

对照着zip文件格式,看看哪里不对,最后定位到data段.86-118这一段,三个数据块.
然后各种亦或组合.........无果.
再然后,要学弟提取一份.
对照看,发现,在这之前还有一段是被我亦或过的.....艹啊.
然后~~~用后面注释跟的内容rot13后作为密码.得到flag.


后来发现,其实就是每一行一种颜色,进行对比,然后置位010101得到一个zip.
py如下:
comp函数由J0ker指点并提供
'''

import Image
import zipfile

def rot13(s, OffSet=13):
     def encodeCh(ch):
         f = lambda x: chr((ord(ch)-x+OffSet) % 26 + x)
         return f(97) if ch.islower() else (f(65) if ch.isupper() else ch)
     return ''.join(encodeCh(c) for c in s)

def comp(base,curpix):
    a = 0
    bv = 0
    for i in range(3):
        if(base[i] != curpix[i]):
            a = i
            if(curpix[i]>base[i]):
                bv = base[i]
            else:
                bv = curpix[i]
    return (a,bv)


if __name__ == '__main__':
    img = Image.open('../../DATA/MISC03/isccfinal.bmp')
    pix = img.load()
    w,h = img.size
    result = ""
    for i in range(h):
        base = pix[0,i]
        cmpr = ()
        for j in range(w-1):
            if (base != pix[j+1,i]):
                cmpr = comp(base,pix[j+1,i])
        for k in range(w):
            if(cmpr == ()):
                result += '0' * w
                break
            else:
                result += str(pix[k,i][cmpr[0]]-cmpr[1])
    req = []
    for i in range(0, len(result), 8):
        req.append(chr(int(result[i: i + 8],2)))
    pwd = "".join(req)[-16:]
    pwd = rot13(pwd)
    #print pwd
    open("../../DATA/MISC03/result.zip", "wb").write("".join(req))
    zip = zipfile.ZipFile("../../DATA/MISC03/result.zip", "r")
    zip.extract("flag.txt", "../../DATA/MISC03/", pwd)
    print open("../../DATA/MISC03/flag.txt").read()

