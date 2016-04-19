from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random

def main():
  html = urlopen("http://www.imdb.com/search/title?year=2015,2015&title_type=feature&sort=moviemeter,asc")
  bsObj = BeautifulSoup(html, "html.parser")
  names = (bsObj.findAll('span', attrs={'class':'credit'}))
  #names = bsObj.findAll('a', href=re.compile('/name/'))
  nameList = []
  for name in names:
    name = str(name)
    name = name.split('"credit"')
    #name.string.split('"credit"')
    nameList.append(name)
  nm = []
  for i in range(len(nameList)):
    splitname = nameList[i][1].split('</a>')
    for j in range(len(splitname)):
      
    

main()