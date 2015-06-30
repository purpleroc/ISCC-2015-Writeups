#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Url__ = 'Http://www.purpleroc.com'
__author__ = 'Tracy_梓朋'


'''
伪加密，修复下可以得到一个zip。
zip解压后得到一个arm下的程序。
看了半天，ida也分析了半天，得出结论。这货是go写的。
不会也看不懂。
然后在手机上运行了下。
输出一串奇奇怪怪的东西。以为是报错，就也没理他。
后来，把输出结果重定向到一个文件。
之后winhex打开，发现，是一个class文件。
jd-gui直接反编译。
得到flag：
import java.io.PrintStream;

class CNSSAndroid
{
  public static void main(String[] paramArrayOfString)
  {
    char[] arrayOfChar = { 'C', 'N', '5', '5', '_', 'A', 'R', 'M' };

    System.out.println(arrayOfChar);
  }
}
CN55_ARM
'''