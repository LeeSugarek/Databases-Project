from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random

def main():
  html = urlopen("http://www.imdb.com/search/title?year=2015,2015&title_type=feature&sort=moviemeter,asc")
  bsObj = BeautifulSoup(html)
  classifications = bsObj.findAll('span', attrs={'title': ['G', 'PG', 'PG_13', 'R']})
  classificationList = []
  for classification in classifications:
      classificationList.append(str(classification))
  print(classificationList)
  
  classificationList2 = []
  for i in range (len(classificationList)):
    if "PG_13" in classificationList[i]:
      classificationList2.append("PG_13")
    elif "R" in classificationList[i]:
      classificationList2.append("R")
    elif "PG" in classificationList[i]:
      classificationList2.append("PG")
    elif "G" in classificationList[i]:
      classificationList2.append("G")
  print(classificationList2)
	  
main()