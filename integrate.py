# Author: Andrea Sarah
# Version: 12.10.04

def main():
        f = lambda x: 1 / x
        F = log
        n = 64
        low = 1
        high = 2
        print "Natural log of 2"
        print "About:", simpson_rule(f, n, low, high)
        print "Exact:", F(high) - F(low)

def simpson_rule(f, n, low, high):
        """Use Riemann's sum to compute Simpson's rule and return answer.

        This function estimates the integral from low to high of a function
        using Simpson's rule.

        """
        l = riemann_sum(f, n, low, high, "l")
        r = riemann_sum(f, n, low, high, "r")
        m = riemann_sum(f, n, low, high, "m")
        t = (l + r) / 2
        return (t + (2 * m)) / 3

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
        from time import clock
        main()
