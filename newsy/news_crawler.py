import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = input('Enter news page to crawl (<ENTER> for Washington Post): ')
if len(url) < 1:
    url = 'http://www.washingtonpost.com'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

count = 0

tags = soup('a')
print ('Length of tags:', len(tags)) #debug

# Now remove some
trimmed_tags = [tag for tag in tags if str(tag).find('<img') == -1 and str(tag).find('nav_') == -1]
print ('Length of trimmed_tags:', len(trimmed_tags)) #debug

for tag in tags:
    try:
        if re.search('Trump', tag.contents[0]) :
            count += 1
        # This is almost everything, just for debugging
        #print ('TAG:', tag)
        #print ('Content:', tag.contents[0])
        #print ('URL:', tag.get('href', None))
        #print ('')
    except:
        continue
        
print ('Number of stories about Trump:', count)