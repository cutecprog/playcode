from sympy import factorint

def main():
        print "euler23.py"
        print sum(proper_factors(28))
        print deficient(28)
        print perfect(28)
        print factorint(28)
        abridged_abundant = lambda(x): x%6 != 0 and x%28 != 0 and x%496 != 0 and abundant(x)
        print ascuii_map([('X', abridged_abundant), (' ', nil)], ['list', 0, 8000, 60])
        #for i in range(2, 100):
        #        print i, sum(proper_factors(i)), ' ' if deficient(i) else '\tX'

def proper_factors(n):
        """Calculate proper factors of n.

        >>> proper_factors(28)
        [1, 2, 4, 7, 14]

        """
        pf = [1]
        for i in range(2, n):
                if n%i == 0:
                        pf.append(i)
        
        return pf

deficient = lambda(n): sum(proper_factors(n)) < n
perfect = lambda(n): sum(proper_factors(n)) == n
abundant = lambda(n): sum(proper_factors(n)) > n
nil = lambda(n): True # for else condition

def ascuii_map(symbols, shape):
        """Make map of range numbers using ACUII symbols.
        
        Determine symbol in space with associated condition. Determine what
        number a space represents with shape.

        >>> print ascuii_map([('0', lambda(n): n%2 == 0), ('X', nil)], ['list', 0, 12, 3])
        0X0|
        X0X|
        0X0|
        X0X<--

        """
        if shape[0] != 'list':
                return "Error: Bad shape type"

        low = shape[1]
        high = shape[2]
        row_size = shape[3]
        ascuii_map = ""

        for i in range(low, high):
                if (i - low) % row_size == 0 and (i - low) != 0:
                        ascuii_map += '|\n'
                for symbol in symbols:
                        if symbol[1](i):
                                ascuii_map += symbol[0]
                                break;
        return ascuii_map+"<--"

if __name__ == "__main__":
        from doctest import testmod
        from os import system
        system("clear")
        testmod()
        main()
