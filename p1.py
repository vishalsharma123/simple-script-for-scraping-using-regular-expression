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



url = "file:///C:/Users/Admin/Desktop/p1.html"
i=0
while i<len(url):
    url = "file:///C:/Users/Admin/Desktop/p1.html"
    htmlfile = urllib2.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<div class="Telephone " >(.+?)</div>'
    pattern = re.compile(regex)
    Telephone = re.findall(pattern,htmltext)
    print(Telephone)
    i+=1
    break
  






url = "file:///C:/Users/Admin/Desktop/p1.html"
i=0
while i<len(url):
    url = "file:///C:/Users/Admin/Desktop/p1.html"
    htmlfile = urllib2.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<div class="Fax">(.+?)</div>'
    pattern = re.compile(regex)
    Fax = re.findall(pattern,htmltext)
    print(Fax)
    i+=1
    break
url = "file:///C:/Users/Admin/Desktop/p1.html"
i=0
while i<len(url):
    url = "file:///C:/Users/Admin/Desktop/p1.html"
    htmlfile = urllib2.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<div class="MobilePhone">(.+?)</div>'
    pattern = re.compile(regex)
    MobilePhone = re.findall(pattern,htmltext)
    print(MobilePhone)
    i+=1
    break
zip(zip(Telephone, Fax, MobilePhone))


result = [('Telephone',',', 'Fax',',', 'MobilePhone')] + zip(zip(Telephone, Fax, MobilePhone))
with open('file.csv', 'wb') as fin:
    writer = csv.writer(fin, delimiter = '\t')
    writer.writerows(result)
    header = [('Telephone'),('Fax'),('MobilePhone')]
    result = zip(zip('Telephone', 'Fax', 'MobilePhone'))
##    format_string = "{:>10}{:>10}{:>10}"
##    with open('file.csv', 'wb') as fin:
##        fin.write(format_string.format(*header))
##        fin.write('\n')
##    for row in result:
##        fin.write(format_string.format(*row))
##        fin.write('\n')

