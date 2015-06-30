#exp1
###350
###有一个参数可以使程序弹出计算器，找出这个参数并把它MD5值作为flag提交。

>利用输入参数与‘dC’的异或值来控制覆盖长度，题中给出了通用jmp esp地址7ffa4512。<br>
所以，想办法让jmp esp覆盖ret地址即可。<br>
然后,发现,只要填充24个A就可以了,就知道要输入gd还是dg来着,拿着这个字符去md5一下就是flag.<br>

    echo dg > 1.dat && md5sum 1.dat | cut -b 1-32 && rm 1.dat
    
>flag is: 8bcc00839adb2f039830ad6b2ecc29dd