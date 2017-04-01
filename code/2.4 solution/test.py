f = open('file1.py','rb')
pylines = f.readlines()
temp = pylines[5]
concat = ""
for letter in temp:
	tmp = ord(letter)
	concat = concat + hex(tmp)[2:]
concat = concat[:-1]
print concat
