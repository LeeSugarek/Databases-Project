from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random

def main():
  html = urlopen("http://www.imdb.com/search/title?year=2015,2015&title_type=feature&sort=moviemeter,asc")
  bsObj = BeautifulSoup(html)
  names = bsObj.findAll('a', href=re.compile('/name/'))
  nameList = []
  for name in names:
    if name.string != None and name.string != 'X':
      nameList.append(name.string)
  print(nameList)
	  
main()