from HTMLParser import HTMLParser
import urllib2
"""from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
assert "Google" in driver.title
#driver.close()"""

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
        data = []
        def handle_starttag(self, tag, attrs):
        	pass
                #print "Encountered a start tag:", tag
        def handle_endtag(self, tag):
	        pass
                #print "Encountered an end tag :", tag
        def handle_data(self, data):
                if data != ' ':
                        self.data.append(data)

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
#print parser.data
f.close()

i = 0
j = 0
data = []
data2 = []
for n in parser.data:
        if i%10 == 0 or i%10 == 1:
                data.append(n.strip() + ": ")
        else:
                data2.append(n)
        i += 1

i = 0
j = 0
for n in data:
        for i in range(0,4):
                data[j] += data2.pop(0)
                if (i + 3) % 4 == 0:
                        data[j] += ","
                data[j] += " "
        j += 1

for n in data:
        print n
