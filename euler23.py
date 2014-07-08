def main():
        print "euler23.py"
        print sum(proper_factors(28))
        print deficient(28)
        print perfect(28)
        print ascuii_map([(lambda(n): n%2 == 0), nil], [' ', 'X'], ['list', 0, 12, 3])

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
nil = lambda(n): True # for else condition

def ascuii_map(condition, symbol, shape):
        """Make map of range numbers using ACUII symbols.
        
        Determine symbol in space with associated condition. Determine what
        number a space represents with shape.

        >>> ascuii_map([(lambda(n): n%2 == 0), nil], [' ', 'X'], ['list', 0, 12, 3])
         X 
        X X
         X
        X X
        """
        return "Map time!"

if __name__ == "__main__":
        from doctest import testmod
        testmod()
        main()
