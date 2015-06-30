#Godlike
###300
###天空中没有留下鸟的痕迹,但我已飞过。 但是，请站在上帝视角看问题！

>挺好玩的一道题吧.拿过来直接binwalk,发现挺多东西,好多dll,还有zip.<br>
然后foremost提取得到文件.发现有个加密的zip.<br>
还以为是伪加密,尝试了下,发现不是的.<br>
然后就

    strings misc300.pcap | grep password
    strings misc300.pcap | grep pwd
    strings misc300.pcap | grep zip
    
>尝试了下.<br>
发现,zip是上传到网站的,然后还有个

    action=shell&command=unzip+-P+%22havefun%22+.%2Fhehe.zip&submit=Execute@

>然后,就得到了解压密码.havefun<br>
打开压缩包,得到hh.txt.<br/>
flag{ce8c136df237e86bb7a553347f}