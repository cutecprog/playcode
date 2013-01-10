print "hello CS internship"

from HTMLParser import HTMLParser
import urllib2

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
        data = ''
        def handle_starttag(self, tag, attrs):
        	pass
                #print "Encountered a start tag:", tag
        def handle_endtag(self, tag):
	        pass
                #print "Encountered an end tag :", tag
        def handle_data(self, data):
                if data != ' ':
                        self.data += data + '\n'

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

#u = urllib2.urlopen('http://www.gunowners.org/113srat.htm')
#s = ' '.join(u.read().split())
#print s
#parser.feed(s)
#print parser.data

f = open("./tmp_data", "r")

u = f.read()
s = ' '.join(u.split())
parser.feed(s)
print parser.data

f.close()

