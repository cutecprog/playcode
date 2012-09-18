# Author: Andrea Sarah
# Version: 12.09.02

from math import *
from time import *

def main():
        f = lambda x: 1/x
        F = log
        low = 1
        high = 20
        for i in range(1, 21):
                print i
                start = clock()
                tmp = simpson_rule(f, 2**i, low, high) - (F(high) - F(low))
                end = clock()
                print "S(%i) = " % 2**i, tmp, end - start
                start = clock()
                tmp = riemann_sum(f, 3*2**i, low, high) - (F(high) - F(low))
                end = clock()
                print "M(%i) = " % (3*2**i), tmp, end - start 
        

def simpson_rule(f, n, low, high):
        """Use Riemann's sum to compute Simpson's rule and return answer.

        This function estimates the intefral from low to high of a function
        using Simpson's rule.

        """
        l = riemann_sum(f, n, low, high, "l")
        r = riemann_sum(f, n, low, high, "r")
        m = riemann_sum(f, n, low, high, "m")
        return (l / 6) + (r / 6) + ((2 * m) / 3)

def riemann_sum(f, n, low, high, mode="m"):
        """Compute mode bound Riemann's sum and return answer.

        This function estimates the integral from low to high of a function
        using mode bound rectangles with a certain resolution n.

        """
        total = 0
        width = float((high - low)) / n
        i = low
        if mode == "r":
                i += width
                high += width
        elif mode == "m":
                i += width / 2
                high += width / 2
        while i < high:
                total += f(i)
                i += width
        return total * width

if __name__=="__main__":
        from math import *
        main()
