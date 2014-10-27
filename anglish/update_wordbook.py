from bs4 import BeautifulSoup
from urllib2 import urlopen

addr = "http://anglish.wikia.com/wiki/Anglish_wordbook"
pages = []

# Load data of downloaded pages
"""try:
        print "Loading previous page downloads..."
        with open('tmp.data','r') as f:
                pages = f.read().split('\n><><><><><><><\n')
                print len(pages)
except IOError:
        print "No previous page downloads"
        page = urlopen(addr).read()
        pages.append(BeautifulSoup(page))
        #with open('tmp.data', 'w') as f:
        #        f.write(page)                   # Save data
        #        f.write('\n><><><><><><><\n')   # Page separator
"""
page = urlopen(addr).read()
pages.append(BeautifulSoup(page))

# Mine for letter groups
letters = []
for link in pages[0].find('table').find_all('a'):
        letters.append(link.string.encode('utf8'))
print letters

# Download pages of letter groups
for letter in letters: # Skip previously downloaded pages
        print letter
        page = urlopen(addr+"/"+letter).read()
        pages.append(page)
        #with open('tmp.data', 'w') as f:
        #        f.write(page)                   # Save data
        #        f.write('\n><><><><><><><\n')   # Page separator

# Mine for words
mined_data = ""
for page in pages[1:]: # Skip main pages
        print page
        soup = BeautifulSoup(page)
        for word in soup.find_all('table')[1:]:
                mined_data += word.prettify()
with open('anglish_workbook.html', 'w') as f:
        f.write(mined_data.encode('utf8'))

