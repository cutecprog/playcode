from HTMLParser import HTMLParser
import urllib2

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


def state_abbr(s):
        value = [('AK', 'Alaska'), ('AL', 'Alabama'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('DC', 'Washington D.C.'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')]
        for n in value:
                if s.lower() == n[1].lower():
                        return n[0]
        return 'NA'
       
#print state_abbr('TEXAS')

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.gunowners.org/113srat.htm")
assert "GOA" in driver.title
driver.get("http://google.com")
#elem = driver.find_element_by_name("q")
#elem.send_keys("selenium")
#elem.send_keys(Keys.RETURN)
#assert "Google" in driver.title
#driver.close()


"""
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
                data.append(state_abbr(n.strip()) + ": ")
        else:
                data2.append(n.strip())
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
