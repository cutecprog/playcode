def main():
        numbers = []
        for i in range(0,4):
                numbers += [randint(6,30)]
        print "Generated numbers:", numbers
        multiplers_for_common_length(numbers)

def gcd(args):
        """Find the greatest common divisor using Euclid's Algorithm.

        """
        L = priority_queue()
        for n in args:
                L.add(n)
        while L.size > 1:
                tmp = L.pop()%L.least()
                if tmp != 0:
                        L.add(tmp)
        return L.pop()

def multiplers_for_common_length(args):
        initial = []
        final = []
        GCD = 1
        product = 1
        L = priority_queue()
        for n in args:
                product *= n
        for n in args:
                initial += [(product/n)]
        print "Initial Multipler:", initial
        GCD = gcd(initial)
        print "GCD:", GCD
        for n in initial:
                final += [n/GCD]
        print "Minimum Multipler:", final

class priority_queue(object):
        def __init__(self, values = []):
                self.data = values
                self.size = len(values)
        def pop(self):
                tmp = self.data[self.size-1]
                self.data = self.data[:self.size-1]
                self.size -= 1
                return tmp
        def least(self):
                return self.data[0]
        def most(self):
                return self.data[self.size-1]
        def add(self, value):
                if self.size == 0 or value > self.most():
                        self.data += [value]
                        self.size += 1
                        return
                for i in range(0, self.size):
                        if value <= self.data[i]:
                                self.data = self.data[:i] + [value] + self.data[i:]
                                self.size += 1
                                return

if __name__=="__main__":
        from random import randint
        main()
