#!/usr/bin/python


def main():
    primeNumbers = []
    for i in range(2,10000):
        if isPrime(i):
            primeNumbers.append(i)
    #print primeNumbers
    #primeFactors(200,primeNumbers)

def primeFactors(n, pf):
    i=2
    pf=[]
    while not isIn(n, pf):
        if n%i==0:
            pf.append(i)
            n/i
        i = nextPrime(i,pf)
    return pf

def nextPrime(n,pf):
    n+=1
    if isIn(n,pf):
        return n
    return nextPrime(n,pf)

def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1

def isIn(n,pf):
    for i in pf:
        if n==i:
            return 1
    return 0
            

if __name__ == "__main__":
    main()
