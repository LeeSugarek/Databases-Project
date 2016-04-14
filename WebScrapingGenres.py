from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random

def main():
  html = urlopen("http://www.imdb.com/search/title?year=2015,2015&title_type=feature&sort=moviemeter,asc")
  bsObj = BeautifulSoup(html)
  genres = bsObj.findAll('span', attrs={'class':'genre'})
  genreList = []
  for genre in genres:
      genreList.append(genre)
  temp = []
  for i in range (0,50):
    genres1 = (genreList[i].findAll('a', href=re.compile('/genre/')))
    temp2 = []
    for genre1 in genres1:
      temp2.append(genre1.string)
    temp.append(temp2)
    temp2=[]
  print(temp)
  
  
  

 # for i in range (len(genreList)):
  #  print(type(genreList[i]))
#    print(genreList[i].string)
main()