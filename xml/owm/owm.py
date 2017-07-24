# 07/14/2017
# 
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import hidden_key

base_url = 'http://api.openweathermap.org/data/2.5/weather?'
api_key = hidden_key.get_key()

city = input('Enter City, State or press Enter for current weather conditions in Ann Arbor: ')
if len(city) < 1: city = 'Ann Arbor, MI'

def build_url():
    url = base_url + 'q=' + city + '&mode=xml&units=imperial&APPID=' + api_key
    return url

url = build_url()

#print(url) #Debug
#print('Retrieving', url) #Debug

uh = urllib.request.urlopen(url)
data = uh.read()
#print('Retrieved', len(data), 'characters') #Debug
#print(data.decode()) #Debug

tree = ET.fromstring(data)
print('Current temp in', city, 'is:', tree.find('temperature').get('value'))
