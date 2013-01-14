#!/usr/bin/python

from sys import argv

#test = [['a1','b1','c1','d1','e1',''],['a2','','c2','d2','',''],['','b3','','d3','','f3'],['','','','','e4','']]

class row(object):
        def __init__(self, lastname, firstname, pvs_id, ftm_id):
                self.lastname = lastname
                self.firstname = firstname
                self.pvs_id = pvs_id
                self.ftm_id = ftm_id
        def __str__(self):
                return "%s,%s,%s,%s" % (self.lastname, self.firstname, self.pvs_id, self.ftm_id)
        

def main():
        print "Unique ID Matcher"
        print 'Number of arguments:', len(argv), 'arguments.'
        print 'Argument List:', argv
        f = open(argv[1], "r")
        data = csv_to_list(f.read(), '\t')
        candidate_name = []
        for n in data[1:]:
                if n[4] == "2013":
                        candidate_name.append(n[5])
                        print n[5]
        f.close()

def csv_to_list(csv_str, dem = ','):
        """Convert a str in CSV format into a 2d list.
        
        >>> csv_to_list("a1,b1,c1,d1,e1,")
        [['a1', 'b1', 'c1', 'd1', 'e1', '']]
        >>> csv_to_list("a2,,c2,d2,,")
        [['a2', '', 'c2', 'd2', '', '']]
        >>> csv_to_list(",b3,,d3,,f3")
        [['', 'b3', '', 'd3', '', 'f3']]
        >>> csv_to_list(",,,,e4,")
        [['', '', '', '', 'e4', '']]
        
        """
        lines = csv_str.strip('\n').split('\n')
        csv_data = []
        for l in lines:
                csv_data.append(l.strip('\r').split(dem))
        return csv_data

if __name__=="__main__":
        import doctest
        doctest.testmod()
        main()
