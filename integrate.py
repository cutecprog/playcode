# Author: Andrea Sarah
# Version: 12.09.02

def main():
        print "5.1: 8"
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

def integrate(f, n, low, high):
        """Compute right bound Riemann's sum and return answer

        This function estimates the integral from low to high of a function
        using right bound rectangles with a certain resolution n.

        """
        total = 0
        width = float((high - low)) / n
        i = low
        while (i < high):
                total += f(i)
                i += width
        return total * width

if __name__=="__main__":
        from math import *
        main()
