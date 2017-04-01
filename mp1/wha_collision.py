import binascii
import array

inputStr = "NI THE 1800S SO MANY MEN USED MACASSAR OIL IN THEIR HAIR THAT SOFA COVERS CALLED THESE WERE DEVELOPED"
print "input string: " + inputStr

MASK = 0x3FFFFFFF
outHash = 0
for c in inputStr:
    byte = ord(c)
    intermediate_value = ((byte ^ 0xCC) << 24) | ((byte ^ 0x33) << 16) | ((byte ^ 0xAA) << 8)  | (byte  ^ 0x55)
    outHash = (outHash & MASK) + (intermediate_value & MASK)
print format(outHash, '#04x')

