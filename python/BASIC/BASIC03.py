#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Url__ = 'Http://www.purpleroc.com'
__author__ = 'Tracy_梓朋'

'''
恶作剧or机密？
100
小锐最近get一份公司的文档，听说里面有很多重要的内部资料，可惜的是，他不会破解文档，你能帮帮他吗？
见附件：企业年度财政报表.docx
hint1: 加密密码只有4位
附件下载
很无脑的一道题,跑密码,而且是很无脑的一个密码:hj7k~
'''

import base64
#'ZHVhbmcyMDE1ZHVhbmdkYQo=\n'
print "Your flag is:" + base64.b64decode(base64.b64decode("WkhWaGJtY3lNREUxWkhWaGJtZGtZUW89Cg=="))
#'duang2015duangda\n'