class priority_queue(object):
        def __init__(self, values):
                self.data = values
                self.size = len(values)
        def pop(self):
                tmp = self.data[size-1]
                self.data = self.data[:size-2]
                size--
                return tmp
        def least(self):
                return self.sata[0]
        def add(self, value):
                for i in range(0, size):
                        if value <= self.data[i]:
                                self.data=self.data[:i] + [value] + self.data[i:]
                                size++
                                return
                self.data += [value]

def main():
        L = priority_queue([54,78,93,103,5003])
        print L.data

if __name__=="__main()__":
        main()
