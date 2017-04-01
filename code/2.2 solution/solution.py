
f = open("cipher.txt", "rb")
cipher = int(f.read().strip(), 16)

g = open("./prikey.hex", "rb")
d = int(g.read().strip(), 16)

h = open("./modulus", "rb")
n = int(h.read().strip(), 16)

plaintext = pow(cipher, d, n)
print plaintext
