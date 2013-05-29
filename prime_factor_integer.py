def main():
        print "Main"
        ps = load_sieve()
        itopfi(3)
        tmp = input()
        itopfi(3,ps)

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

def itopfi(integer, prime_sieve = load_sieve()):
        """Convert integer to string of prime factors.

        """
        print prime_sieve

if __name__ == "__main__":
        main()
