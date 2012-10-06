class priority_queue(object):
        def __init__(self, values):
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
                if value > self.most():
                        self.data += [value]
                        self.size += 1
                        return
                for i in range(0, self.size):
                        if value <= self.data[i]:
                                self.data = self.data[:i] + [value] + self.data[i:]
                                self.size += 1
                                return

def main():
        """foo = priority_queue([3])
        foo.add(1)
        print foo.data"""
        L = priority_queue([54,78,93,103,5003])
        while L.size > 1:
                print L.data
                tmp = L.pop()%L.least()
                print tmp
                if tmp != 0:
                        L.add(tmp)
                        print "ADD",L.data
        print L.data

if __name__=="__main__":
        main()
