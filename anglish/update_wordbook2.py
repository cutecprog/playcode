from bs4 import BeautifulSoup
from urllib2 import urlopen
from pickle import dump

addr = "http://anglish.wikia.com/wiki/English_Wordbook"
pages = []

# Mine for letter groups
letters = []
for i in range(0,26):
        letters.append(chr(ord('A')+i))
print letters

# Download pages of letter groups
for letter in letters: # Skip previously downloaded pages
        print letter
        page = urlopen(addr+"/"+letter).read()
        pages.append(page)

with open('tmp2.data', 'wb') as f:
        dump(pages, f)
'''
# Mine for words
mined_data = ""
for page in pages[1:]: # Skip main pages
        print page
        soup = BeautifulSoup(page)
        for word in soup.find_all('table')[1:]:
                mined_data += word.prettify()
with open('anglish_workbook.html', 'w') as f:
        f.write(mined_data.encode('utf8'))
'''
