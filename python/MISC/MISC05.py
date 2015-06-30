#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Url__ = 'Http://www.purpleroc.com'
__author__ = 'Tracy_梓朋'
'''
先用修复一下图片吧,得到一个PNG,
然后binwalk看了下:
root@Tracker:~/Desktop# binwalk iscc.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1440 x 810, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed, uncompressed size >= 163840
1988164       0x1E5644        Zlib compressed data, default compression, uncompressed size >= 31

有两端被压缩的.取后面那段解压得到flag.
'''
from zlib import *

if __name__ == '__main__':
    data = open("../../DATA/MISC05/iscc.png", "rb").read()[0x1E5644:]
    print decompress(data)