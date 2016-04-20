from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random

def main():
  html = urlopen("http://www.imdb.com/search/title?year=1979,1979&title_type=feature&sort=moviemeter,asc")
  bsObj = BeautifulSoup(html)
  classifications = bsObj.findAll('span', attrs={'certificate'})
  classificationList = []
  for classification in classifications:
      classificationList.append(str(classification))
  print(classificationList)
  classificationList2 = []
  for i in range (len(classificationList)):
    if '"R"' in str(classificationList[i]):
      classificationList2.append('R')
    elif '"PG_13"' in str(classificationList[i]):
      classificationList2.append('PG_13')
    elif '"PG"' in str(classificationList[i]):
      classificationList2.append('PG')
    elif '"G"' in str(classificationList[i]):
      classificationList2.append('G')
    elif '"NC_17"' in str(classificationList[i]):
      classificationList2.append('NC_17')
    else:
      classificationList2.append('other')
      
  print(classificationList2)	  
main()