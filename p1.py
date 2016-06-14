import urllib2
import codecs
import cStringIO
import requests
import re
import csv
from bs4 import BeautifulSoup
from itertools import izip
from itertools import izip_longest
from itertools import chain



url = ""   #url
i=0
while i<len(url):
    url = " "
    htmlfile = urllib2.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<div class="[] " >(.+?)</div>'
    pattern = re.compile(regex)
    Telephone = re.findall(pattern,htmltext)
    print(Telephone)
    i+=1
    break
  






url = ""
i=0
while i<len(url):
    url = " "
    htmlfile = urllib2.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<div class="[]">(.+?)</div>'
    pattern = re.compile(regex)
    Fax = re.findall(pattern,htmltext)
    print(Fax)
    i+=1
    break
url = " "
i=0
while i<len(url):
    url = " "
    htmlfile = urllib2.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<div class="[]">(.+?)</div>'
    pattern = re.compile(regex)
    MobilePhone = re.findall(pattern,htmltext)
    print(MobilePhone)
    i+=1
    break
zip(zip(Telephone, Fax, MobilePhone))


result = [('Value1',',', 'Value2',',', 'value3')] + zip(zip(value1, value2, value3))
with open('file.csv', 'wb') as fin:
    writer = csv.writer(fin, delimiter = '\t')# you can change delimiter according to your parameter
    writer.writerows(result)
    header = [('value1'),('value2'),('value3')]
    result = zip(zip('value1', 'value2', 'value3'))


