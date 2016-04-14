from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random

def main():
  html = urlopen("http://www.imdb.com/search/title?year=2015,2015&title_type=feature&sort=moviemeter,asc")
  bsObj = BeautifulSoup(html)
  directors = bsObj.findAll('span', attrs={'class':'credit'})
  
  directorList = []
  for director in directors:
      directorList.append(director.string)
  print(directorList)
	  
main()