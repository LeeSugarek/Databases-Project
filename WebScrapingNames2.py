from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random

def main():
  html = urlopen("http://www.imdb.com/search/title?year=1974,1974&title_type=feature&sort=moviemeter,asc")
  bsObj = BeautifulSoup(html, "html.parser")
  AllNames = (bsObj.findAll('span', attrs={'class':'credit'}))
  AllNameList = []
  for MovieName in AllNames:
    MovieNameList = []
    MovieName = str(MovieName)
#    print(MovieName)
   # name.string.split('"credit"')
    for i in range (len(MovieName)):
      if MovieName[i] == '>':
        IndividualName = ""
        j = i+1
        while (j < len(MovieName)) and (MovieName[j] != '<'):
          IndividualName = IndividualName + MovieName[j]
          j = j+1
        if IndividualName != ', ':
          if '    ' not in IndividualName:
            if IndividualName != '\n' and IndividualName != '':
              MovieNameList.append(IndividualName)
    AllNameList.append(MovieNameList)	  
  print(AllNameList)
  print(len(AllNameList))
    

main()