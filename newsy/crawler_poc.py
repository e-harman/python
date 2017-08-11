import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = input('Enter news page to crawl (<ENTER> for Washington Post): ')
if len(url) < 1:
    url = 'http://www.washingtonpost.com'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

count = 0
# 
tags = soup('a')
for tag in tags:
    try:
        #print (tag.contents[0])
        if re.search('Trump', tag.contents[0]) :
            count += 1
        # This is almost everything, just for debugging
        #print ('TAG:', tag)
        #print ('URL:', tag.get('href', None))
        #print ('Content:', tag.contents[0])
        #print ('')
    except:
        continue
        
print (count)