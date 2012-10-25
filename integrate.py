# Author: Andrea Sarah
# Version: 12.10.11

a = [[1.5, 0.387298334621],
[1.50625, 0.375780437889],
[1.5125, 0.363790805271],
[1.51875, 0.35128113741],
[1.525, 0.338193731462],
[1.53125, 0.32445868381],
[1.5375, 0.309989919191],
[1.54375, 0.294679380853],
[1.55, 0.278388218141],
[1.55625, 0.260932821814],
[1.5625, 0.242061459138],
[1.56875, 0.221412369799],
[1.575, 0.19843134833],
[1.58125, 0.172187216424],
[1.5875, 0.14086784587],
[1.59375, 0.0998044963917]]


def main():
        r = .8
        f = lambda h: sqrt(2*h*r-h**2)
        #print sqrt(0)
        print f(1.6)
        print riemann_sum(f, 0, 2*r, "r")
        #print simpson_rule(lambda h: 1000*9.8*2*sqrt(2*h*r-h**2), 0, 2*r)

def simpson_rule2(f, width):
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
        return float(S * width) / 3

def simpson_rule(f, low, high, n = 256.):
        """Use function definition to compute Simpson's rule.

        This function estimates the integral from low to high of a function
        using Simpson's rule. Use Riemann's Sum to compute left, right, and mid
        end point approximations.

        """
        if type(f) == type(list()):
                return simpson_rule2(f, (high - low)/(len(f)-1))
        l = riemann_sum(f, low, high, "l", n)
        r = riemann_sum(f, low, high, "r", n)
        m = riemann_sum(f, low, high, "m", n)
        t = (l + r) / 2
        return (t + (2 * m)) / 3

def riemann_sum(f, low, high, mode = "m", n = 256.):
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
                print i, f(1.6)
                total += f(i)
                i += width
        return total * width

def d(f, default_width = 0.1e-5):
        """
        Compute the numerical derivative of a function.

        """
        def df(x, width = default_width):
                return ( f(x + width / 2) - f(x - width / 2) ) / width
        return df

if __name__=="__main__":
        from math import *
        from time import clock
        main()
