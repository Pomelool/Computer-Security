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

def test_hack_RSA():
 	print("Testing Wiener Attack")
	f = open("./pubkey", "rb")
	g = open("./modulus", "rb")
	x = f.read().strip()
	y = g.read().strip()
	e = int(x, 16)
	n = int(y, 16)
	d = 0
    # e,n,d = RSAvulnerableKeyGenerator.generateKeys(1024)
	print "e is: "    
	print e
	print "n is: "
	print n
	print "d is: "
	print d

	hacked_d = hack_RSA(e, n)
    
	if d == hacked_d:
		print("Hack WORKED!")
	else:
		print("Hack FAILED")
        
	#print("d = ", d, ", hacked_d = ", hacked_d)
	print format(hacked_d, '#04x')
	print("-------------------------")   
if __name__ == "__main__":
	test_hack_RSA()


    


        
    
