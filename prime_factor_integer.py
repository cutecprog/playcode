def main():
        print "test"
        print load_sieve()

def load_sieve(path = './prime_sieve'):
        """
        Load and return list (sieve) from a json data file.

        >>> import json
        """
        import json
        with open(path, 'rb') as f:
                sieve = json.loads(f.read())
        assert type(sieve) == type(list()),\
        "data file format incorrect" + " load_sieve(" + path + ") failed."
        return sieve

if __name__ == "__main__":
        main()
