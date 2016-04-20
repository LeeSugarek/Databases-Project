from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random

def main():
  year = 2010
  for year in range (2010,2016):
    html = urlopen("http://www.imdb.com/search/title?year=" + str(year) + "," + str(year) + "&title_type=feature&sort=moviemeter,asc")
    bsObj = BeautifulSoup(html)
    titles = bsObj.findAll('a', href=re.compile('/title/'))
    titleList = []
    for title in titles:
      if title.string != None and title.string != 'X':
        titleList.append(title.string)
    print(titleList)
    print(len(titleList))
main()