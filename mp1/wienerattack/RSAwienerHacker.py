# The following code is modified from code existing in the following git repository !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# The following code is modified from code existing in the following git repository !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# The following code is modified from code existing in the following git repository !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# The following code is modified from code existing in the following git repository !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# The following code is modified from code existing in the following git repository !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# https://github.com/pablocelayes/rsa-wiener-attack
'''
Created on Dec 14, 2011

@author: pablocelayes
'''

import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator

def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d

# TEST functions


print("Testing Wiener Attack")
f = open("./szhou42_public_key.hex", "rb") #modified .hex
g = open("./szhou42_modulo.hex", "rb")#modified .hex
h = open("./szhou42_ciphertext.hex", "rb")
c = h.read().strip()
x = f.read().strip()
y = g.read().strip()
c = int(c, 16)
e = int(x, 16)
n = int(y, 16)
d = hack_RSA(e, n)
# e,n,d = RSAvulnerableKeyGenerator.generateKeys(1024)
print "e is: "    
print e
print "n is: "
print n
print "d is: "
print d
    
#print("d = ", d, ", hacked_d = ", hacked_d)
plaintext = pow(c,d,n)
#print format(hacked_d, '#04x')
print("-------------------------")   
print hex(plaintext)[2:]
print("-------------------------")   
print plaintext

    


        
    
