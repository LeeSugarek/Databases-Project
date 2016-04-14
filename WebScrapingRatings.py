from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random

def main():
  html = urlopen("http://www.imdb.com/search/title?year=2015,2015&title_type=feature&sort=moviemeter,asc")
  bsObj = BeautifulSoup(html)
  ratings = bsObj.findAll('span', attrs={'class':'value'})
  ratingList = []
  for rating in ratings:
      ratingList.append(rating.string)
  print(ratingList)
	  
main()