#!/usr/bin/python

from sys import argv

#test = [['a1','b1','c1','d1','e1',''],['a2','','c2','d2','',''],['','b3','','d3','','f3'],['','','','','e4','']]

def main():
        print "Unique ID Matcher"
        print 'Number of arguments:', len(argv), 'arguments.'
        print 'Argument List:', argv
        f = open(argv[1], "r")
        print f.read()
        #print test
        f.close()

def csv_to_list(csv_str):
        """Convert a str in CSV format into a 2d list.
        
        >>> csv_to_list("a1,b1,c1,d1,e1,")
        [['a1', 'b1', 'c1', 'd1', 'e1', '']]
        >>> csv_to_list("a2,,c2,d2,,")
        [['a2', '', 'c2', 'd2', '', '']]
        >>> csv_to_list(",b3,,d3,,f3")
        [['','b3','','d3','','f3']]
        >>> csv_to_list(",,,,e4,")
        [['', '', '', '', 'e4', '']]
        
        """
        pass

if __name__=="__main__":
        import doctest
        doctest.testmod()
        main()
