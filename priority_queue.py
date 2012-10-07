def main():
        demo()

def gcd(initial):
        L = priority_queue()
        for n in initial:
                L.add(n)
        while L.size > 1:
                tmp = L.pop()%L.least()
                if tmp != 0:
                        L.add(tmp)
        return L.pop()
def demo():
        numbers = []
        initial = []
        final = []
        GCD = 1
        product = 1

        # Generation of numbers
        for i in range(0,4):
                numbers += [randint(6,30)]
        print "Generated numbers:", numbers
        
        # Algorithm
        for n in numbers:
                product *= n
        L = priority_queue()
        for n in numbers:
                initial += [(product/n)]
        print "Initial:", initial
        GCD = gcd(initial)
        print "GCD:", GCD
        for n in initial:
                final += [n/GCD]
        print "Minium Factors:", final


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
