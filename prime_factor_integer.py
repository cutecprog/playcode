def main():
        print "test"
        print load_sieve()

def load_sieve(path = './prime_sieve'):
        import json
        with open(path, 'rb') as f:
                sieve = json.loads(f.read())
        return sieve

if __name__ == "__main__":
        main()
