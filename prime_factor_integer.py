def main():
        from random import randint
        print "Main"
        ps = load_sieve()
        last = 0
        for p in ps:
                print '\n' * (p - last - 1)
                print 'X' * p
                last = p

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

if __name__ == "__main__":
        main()
