from HTMLParser import HTMLParser
import urllib2

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
        data = []
        data2 = []
        good_data = [False, False]
        index = -1
        def handle_starttag(self, tag, attrs):
                if tag == "h4":
                        #print "h4"
                        if self.good_data[1]:
                                self.data.append([])
                        else:
                                self.data2.append([])
                        self.index += 1
                if len(attrs) == 0:
                        return
                for items in attrs:
                        for i in items:
                                if i == "tabFunding":
                                        self.good_data[1] = True
                                        self.index = -1
                                elif i == "tabGrants":
                                        self.good_data[1] = False
                                        self.index = -1
                                if i == "amount tip":
                                      self.good_data[0] = True 
        	#self.data2.append(attrs)
                #print "Encountered a start tag:", tag
        handle_starttag.index = -1
        def handle_endtag(self, tag):
	        pass
                #print "Encountered an end tag :", tag
        def handle_data(self, data):
                if self.good_data[0]:
                        if self.good_data[1]:
                                self.data[self.index].append(data)
                        else:
                                self.data2[self.index].append(data)
                        self.good_data[0] = False

def sum_data(data):
        S = 0
        for n in data:
                S += float(''.join(n.strip('$').split(',')))
        return S

parser = MyHTMLParser()

u = urllib2.urlopen('http://sunlightfoundation.com/about/funding/')
s = ' '.join(u.read().split())
parser.feed(s)
print parser.data
print parser.data2
for d in parser.data:
        print sum_data(d)
print "---"
for d in parser.data2:
        print sum_data(d)
#print sum_data(parser.data)
#print sum_data(parser.data2)

'''
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
        print n'''
