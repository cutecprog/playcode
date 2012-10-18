# Author: Andrea Sarah
# Version: 12.10.11

def main():
        print simpson_rule([5.8, 20.3, 26.7, 29.0, 27.6, 27.3, 23.8, 20.5, 15.1], 0, 160)
        print d(log)(2)

def simpson_rule2(f, h):
        """Use a list of exact values to compute simpson's rule.

        h = (b - a)/n

        """
        l = len(f)
        S = f[0] + f[l-1]
        for i in range(1, l - 1):
                if i % 2:
                        S += 4*f[i]
                else:
                        S += 2*f[i]
        return float(S * h) / 3

def simpson_rule(f, low, high, n = 256.):
        """Use function definition to compute Simpson's rule.

        This function estimates the integral from low to high of a function
        using Simpson's rule. Use Riemann's Sum to compute left, right, and mid
        end point approximations.

        """
        if type(f) == type(list()):
                return simpson_rule2(f, (high - low)/(len(f)-1))
        l = riemann_sum(f, low, high, n, "l")
        r = riemann_sum(f, low, high, n, "r")
        m = riemann_sum(f, low, high, n, "m")
        t = (l + r) / 2
        return (t + (2 * m)) / 3

def riemann_sum(f, low, high, n = 256., mode = "m"):
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

def d(f, h = 0.1e-5):
        """
        Compute the numerical derivative of a function.

        """
        def df(x, _h = h):
                return ( f(x + _h/2) - f(x - _h/2) )/_h
        return df

if __name__=="__main__":
        from math import *
        from time import clock
        main()
