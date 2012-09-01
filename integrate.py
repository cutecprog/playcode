from math import *

def integrate(f, n, low, high):
        sig = 0
        width = (high - low) /n
        i = low
        while (i < high):
                #print i/pi
                sig += f(i)
                i += width
        return sig*width

print integrate(cos, 10, 0, pi/2)
print integrate(cos, 30, 0, pi/2)
print integrate(cos, 50, 0, pi/2)
print integrate(cos, 100, 0, pi/2)
