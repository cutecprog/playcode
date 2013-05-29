import numpy as np
import scipy.misc.pilutil as smp

def main():
        from random import randint
        print "Main"
        ps = load_sieve()
        print len(ps)

        # Create a 1024x1024x3 array of 8 bit unsigned integers
        data = np.zeros( (10000,3000,3), dtype=np.uint8 )
        for i in range(0, 10000):
                #print i
                s = itopfi(i,ps)
                #print s
                data[i] = bit_line(s)

        img = smp.toimage( data )       # Create a PIL image
        img.show()                      # View in default viewer

def load_sieve(path = './prime_sieve'):
        """Load and return list (sieve) from a json data file.

        >>> import json

        """
        import json
        with open(path, 'rb') as f:
                sieve = json.loads(f.read())
        assert type(sieve) == type(list()),\
        "data file format incorrect" + " load_sieve(" + path + ") failed."
        return sieve

def itopfi(n, prime_sieve = load_sieve()):
        """Convert integer to string of prime factors.

        """
        pfi = ""
        for prime in prime_sieve:
                while(n%prime == 0):
                        pfi += "1"
                        n /= prime
                if n == 1:
                        break
                pfi += "0"
        return pfi

def bit_line(pfi_string):
        line = np.zeros( (3000,3), dtype=np.uint8 )
        i = 0
        for c in pfi_string:
                if c == '1':
                        line[i] = [255,255,255]
                i += 1
        return line
                        

if __name__ == "__main__":
        main()
