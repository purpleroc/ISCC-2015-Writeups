#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Url__ = 'Http://www.purpleroc.com'
__author__ = 'Tracy_梓朋'

'''
蛛丝马迹
150

小野入侵了一个台服务器，发现一个保存重要密码的程序代码，小野又发现了一些蛛丝马迹，他能破解么？

附件：
公司内部密钥程序.txt
0xBE,  0x2A,  0x28,  0x48,  0x7A,  0x5C,  0x2A,  0x21,  0xCB,  0x93,  0x0D,  0x2A,  0x70,  0x36,  0xD3,  0x4E,  0xC9,  0xB6,  0xCF,  0x3C,  0xB6,  0x71,  0x99,  0xF5,  0x46,  0x69,  0xA1,  0x24,  0xF9,  0x71,  0x70,  0x11,  0x2A,  0x37,  0x31,  0x27,  0x30,  0x16,  0x71,  0x90,  0x26,  0xC9,  0x18,  0x72,  0xC9,  0x09,  0x4E,  0xC9,  0x0B,  0x5E,  0xC9,  0x4B,  0xC9,  0x2B,  0x4A,  0xEF,  0x7F,  0x28,  0x48,  0x7A,  0x5C,  0x37,  0x47,  0xD7,  0xBD,  0x15,  0xBA,  0xD7,  0x22,  0xC9,  0x07,  0x7E,  0xC9,  0x0E,  0x47,  0x3A,  0x41,  0x8F,  0xC9,  0x1B,  0x62,  0x41,  0x9F,  0x71,  0xBD,  0x05,  0xC9,  0x76,  0xF9,  0x41,  0xB7,  0xDB,  0x4D,  0xFC,  0x44,  0x78,  0x86,  0x36,  0x4A,  0x83,  0x88,  0x45,  0x41,  0x92,  0x04,  0xA9,  0xB3,  0x79,  0x16,  0x66,  0x5E,  0x37,  0xA6,  0xC9,  0x1B,  0x66,  0x41,  0x9F,  0x24,  0xC9,  0x7E,  0x39,  0xC9,  0x1B,  0x5E,  0x41,  0x9F,  0x41,  0x6E,  0xF9,  0xD7,  0x1D,  0xE9,  0x15,  0x23,  0x7F,  0x28,  0x48,  0x7A,  0x5C,  0x37,  0xEB,  0x71,  0x99,  0x11,  0x2A,  0x35,  0x34,  0x36,  0x64,  0x2A,  0x14,  0x29,  0x68,  0x7A,  0xC9,  0x86,  0x11,  0x12,  0x12,  0x11,  0xBD,  0x15,  0xBE,  0x11,  0xBD,  0x15,  0xBA,  0xD2,  0xD2,  0xD2,  0xD2
企业加密方式.txt
公司内部所有的加密形式均为异或加密，且只使用异或加密，加密KEY：0x42
请牢记，保密！

异或完了后,把它放到一个exe的入口点,然后,直接运行哪个exe就可以弹出flag.
'''
pwd = "BE,  0x2A,  0x28,  0x48,  0x7A,  0x5C,  0x2A,  0x21,  0xCB,  0x93,  0x0D,  0x2A,  0x70,  0x36,  0xD3,  0x4E,  0xC9,  0xB6,  0xCF,  0x3C,  0xB6,  0x71,  0x99,  0xF5,  0x46,  0x69,  0xA1,  0x24,  0xF9,  0x71,  0x70,  0x11,  0x2A,  0x37,  0x31,  0x27,  0x30,  0x16,  0x71,  0x90,  0x26,  0xC9,  0x18,  0x72,  0xC9,  0x09,  0x4E,  0xC9,  0x0B,  0x5E,  0xC9,  0x4B,  0xC9,  0x2B,  0x4A,  0xEF,  0x7F,  0x28,  0x48,  0x7A,  0x5C,  0x37,  0x47,  0xD7,  0xBD,  0x15,  0xBA,  0xD7,  0x22,  0xC9,  0x07,  0x7E,  0xC9,  0x0E,  0x47,  0x3A,  0x41,  0x8F,  0xC9,  0x1B,  0x62,  0x41,  0x9F,  0x71,  0xBD,  0x05,  0xC9,  0x76,  0xF9,  0x41,  0xB7,  0xDB,  0x4D,  0xFC,  0x44,  0x78,  0x86,  0x36,  0x4A,  0x83,  0x88,  0x45,  0x41,  0x92,  0x04,  0xA9,  0xB3,  0x79,  0x16,  0x66,  0x5E,  0x37,  0xA6,  0xC9,  0x1B,  0x66,  0x41,  0x9F,  0x24,  0xC9,  0x7E,  0x39,  0xC9,  0x1B,  0x5E,  0x41,  0x9F,  0x41,  0x6E,  0xF9,  0xD7,  0x1D,  0xE9,  0x15,  0x23,  0x7F,  0x28,  0x48,  0x7A,  0x5C,  0x37,  0xEB,  0x71,  0x99,  0x11,  0x2A,  0x35,  0x34,  0x36,  0x64,  0x2A,  0x14,  0x29,  0x68,  0x7A,  0xC9,  0x86,  0x11,  0x12,  0x12,  0x11,  0xBD,  0x15,  0xBE,  0x11,  0xBD,  0x15,  0xBA,  0xD2,  0xD2,  0xD2,  0xD2"
key = "0x42"

if __name__ == '__main__':
    cipher = pwd.split(',  0x')
    #print "".join(cipher)
    plain = []
    temp = []
    for i in cipher:
        open("../../DATA/BASIC05/basic5.bin","ab").write(chr(int(i, 16) ^ int(key, 16)))

    print "Flag is: Vk*8wvt&"