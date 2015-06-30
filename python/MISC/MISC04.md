#看序列，找规律。
###350
###等差数列？NO！等比数列？NO！

>看了看,一个exe,ffi看到是vc的程序.虚拟机里运行提示Java 运行环境没找到.<br>
然后就主机上IDA\OD同时跟上,本来想逆一逆的,无奈找不到断点,F7 F8大概看了下,Java的,不熟,遂放弃这一想法.<br>
就想着用做android的思路去解决他.

>ESC+Shift+Ctrl调出任务管理器.找到ISCC.EXE.转存之.<br>
然后在里面搜了下界面上的几个字符,发现有的.还是unicode形式.<br>
然后就搜了下flag.ascii的unicode的都有.<br>
F3几次之后,看到FLAG.

    strings dump.dmp | grep flag

>后来想了想,毕竟不是re啊.是misc,对,是misc....╮(╯▽╰)╭<br>
>!^_^! You got it! flag:{99922ad4c295f66fcdc2ebc6cfb91be6}
