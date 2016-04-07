from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random

def main():
  html = urlopen("http://www.imdb.com/search/title?year=2015,2015&title_type=feature&sort=moviemeter,asc")
  bsObj = BeautifulSoup(html)
  titles = bsObj.findAll('a', href=re.compile('/title/'))
  spans = bsObj.findAll('span', attrs={'class':'number'})
  titleList = []
  for title in titles:
    if title.string != None and title.string != 'X':
      titleList.append(title.string)
  print(titleList)
	  
main()