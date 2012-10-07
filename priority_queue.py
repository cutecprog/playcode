def main():
        numbers = []
        for i in range(0,4):
                numbers += [randint(6,30)]
        print "Generated integers:", numbers
        print "Minimum multiplers:", multiplers_for_common_length(numbers)

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
        """Find the lowest integer multiplers for all args to be equal. 

        """
        initial = []
        final = []
        product = 1
        for n in args:
                product *= n
        for n in args:
                initial += [(product/n)]
        GCD = gcd(initial)
        for n in initial:
                final += [n/GCD]
        return final

class priority_queue(object):
        """Pop from front of queue. All items in numeric order largest first.

        """
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
                """Insert new value such that queue is in numerical order.

                """
                index = 0
                for i in range(0, self.size):
                        if value <= self.data[i]:
                                index = i
                                break
                self.data.insert(index, value)
                self.size += 1

if __name__=="__main__":
        from random import randint
        main()
