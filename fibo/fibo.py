#!/bin/python27

def main():
   print fiboD(38)
   print fibo(38)

# Dumb fibo recursion
def fibo(n):
   '''
   Given an index returns that value of the fibonacci sequence. Using dumb
   recursion.
   >>> fibo(7)
   13
   '''
   # This assumes n is positive
   if(n<2):
      return n # return 1 or 0
   return fibo(n-1) + fibo(n-2)

# Container function for Dynamic recursion
def fiboD(n):
   '''
   Removes extra return value produce by the dynamic recursion function (_fiboD)
   >>> fiboD(7)
   13
   '''
   a,b=_fiboD(n)
   return a

# Actual Dynamic recursion function, note the parameters act as return varibles
def _fiboD(n):
   '''
   Given an index returns that value of the fibonacci sequence and it's 
   previous value. Using dynamic recursion.
   >>> _fiboD(7)
   (13, 8)
   '''
   # This assumes n is positive
   if(n<2):
      return n,0 # returns 1,0 or 0,0
   a,b = _fiboD(n-1)
   return a+b, a
   
if __name__=='__main__':
   main()