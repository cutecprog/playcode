# Author: Andrea Sarah
# Version: 12.09.02

from math import *

def main():
        f = lambda x: 1/x
        box = 2
        a = integrate(f, box, 1, 2, "l")
        b = integrate(f, box, 1, 2, "r")
        c = integrate(f, box, 1, 2, "m")
        d = a/6 + b/6 + (2*c/3)
        print box
        print d, log(2)-d

        box = 10
        a = integrate(f, box, 1, 2, "l")
        b = integrate(f, box, 1, 2, "r")
        c = integrate(f, box, 1, 2, "m")
        d = a/6 + b/6 + (2*c/3)
        print box
        print d, log(2)-d

        box = 50
        a = integrate(f, box, 1, 2, "l")
        b = integrate(f, box, 1, 2, "r")
        c = integrate(f, box, 1, 2, "m")
        d = a/6 + b/6 + (2*c/3)
        print box
        print d, log(2)-d

        box = 250
        a = integrate(f, box, 1, 2, "l")
        b = integrate(f, box, 1, 2, "r")
        c = integrate(f, box, 1, 2, "m")
        d = a/6 + b/6 + (2*c/3)
        print box
        print d, log(2)-d
        
        
        """print "5.1: 8"
        print integrate(cos, 10, 0, pi/2)
        print integrate(cos, 30, 0, pi/2)
        print integrate(cos, 50, 0, pi/2)
        print integrate(cos, 100, 0, pi/2)
        print ""
        print "5.2: 16"
        f = lambda x: e**-x**2
        print integrate(f, 10, 0, 2)
        print integrate(f, 30, 0, 2)
        print integrate(f, 50, 0, 2)
        print integrate(f, 100, 0, 2)
        print "Left bound"
        print integrate(f, 10, 0, 2, "l")
        print integrate(f, 30, 0, 2, "l")
        print integrate(f, 50, 0, 2, "l")
        print integrate(f, 100, 0, 2, "l")"""

def integrate(f, n, low, high, mode="l"):
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
