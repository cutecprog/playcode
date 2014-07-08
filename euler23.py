def main():
        print "euler23.py"
        print proper_factors(28)

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

if __name__ == "__main__":
        main()
