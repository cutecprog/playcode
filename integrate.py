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
        print simpson_rule2([5.8, 20.3, 26.7, 29.0, 27.6, 27.3, 23.8, 20.5, 15.1], 20)

#test
def simpson_rule2(f, h):
        """Use a list of exact values to compute simpson's rule.

        """
        l = len(f)
        S = f[0] + f[l-1]
        for i in range(1, l - 1):
                if i % 2:
                        S += 4*f[i]
                else:
                        S += 2*f[i]
        return float(S * h) / 3

def simpson_rule(f, n, low, high):
        """Use function definition to compute Simpson's rule.

        This function estimates the integral from low to high of a function
        using Simpson's rule. Use Riemann's Sum to compute left, right, and mid
        end point approximations.

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
