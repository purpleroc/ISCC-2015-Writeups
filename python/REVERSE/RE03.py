#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Url__ = 'Http://www.purpleroc.com'
__author__ = 'Tracy_梓朋'

'''
没有题目的题目
300
出题的哥哥说，没有描述，想办法弄吧 =。=

嗯,下载下来一个不能解压的apk,然后,就想着怎么玩了.
用winrar修复一次,得到一个zip,再打开,发现还是错的,然后再修复一次.
就得到apk了.apk里主要所发如下:


if(MainActivity.this.check())
    Toast.makeText(MainActivity.this, "恭喜过关", 1).show();


    private boolean check() {
        boolean v3 = false;
        byte[] v0 = new byte[]{102, 67, 119, 112, 103, 86, 72, 55, 124, 88, 93, 74, 85, 56, 37, 107, 95, 114, 127, 124, 65, 124, 102, 78, 76, 106, 106, 105, 40, 36, 93, 115};
        byte[] v1 = this.result1.getBytes();
        int v2 = 0;
    label_6:
        if(v2 < v1.length) {
            Log.d("test", ((byte)(v1[v2] ^ v2)));
            ++v2;
            goto label_6;
        }

        if(v1.length == v0.length) {
            v2 = 0;
        label_12:
            if(v2 < v0.length) {
                if((v1[v2] ^ v0[v2]) != v2) {
                    return v3;
                }

                ++v2;
                goto label_12;
            }

            v3 = true;
        }

        return v3;
    }

MainActivity.this.pswd1 = MainActivity.this.Pswd.getText().toString();
MainActivity.this.result1 = DES.encryptDES(MainActivity.this.pswd1, "poi7y6gt");

public class DES {
    private static byte[] iv;

    static {
        DES.iv = new byte[]{1, 2, 3, 4, 5, 6, 7, 8};
    }

    public DES() {
        super();
    }

    public static String encryptDES(String encryptString, String encryptKey) throws Exception {
        IvParameterSpec v3 = new IvParameterSpec(DES.iv);
        SecretKeySpec v2 = new SecretKeySpec(encryptKey.getBytes(), "DES");
        Cipher v0 = Cipher.getInstance("DES/CBC/PKCS5Padding");
        v0.init(1, ((Key)v2), ((AlgorithmParameterSpec)v3));
        return Base64.encode(v0.doFinal(encryptString.getBytes()));
    }
}

写py如下:
'''
from pyDes import *
import base64

V0 = [102, 67, 119, 112, 103, 86, 72, 55, 124, 88, 93, 74, 85, 56, 37, 107, 95, 114, 127, 124, 65, 124, 102, 78, 76, 106, 106, 105, 40, 36, 93, 115]

def DeCheck(str):
    v1 = []
    for i in range(len(str)):
        v1.append(chr(str[i] ^ i))
    xx = "".join(v1)
    ##print xx
    return base64.b64decode(xx)


if __name__ == '__main__':
    key = 'poi7y6gt'
    iv = '\x01\x02\x03\x04\x05\x06\x07\x08'
    k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    flag = k.decrypt(DeCheck(V0))
    print "Your flag is: " + flag
