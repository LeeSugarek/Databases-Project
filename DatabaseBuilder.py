from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='mysql')
cur = conn.cursor()
cur.execute("USE project")

# This function stores movies into the movies database table
# The movie database table contains the movieID, title, rating, and classification of each movie
def storeMovie(title, year, rating, classification):
  insert_stmt = ("INSERT INTO Movies (id,title,year,rating,classification) " \
  "VALUES (NULL, %s, %s, %s, %s)" )
  data = (title, year, rating, classification)
  cur.execute(insert_stmt, data)
  cur.connection.commit()	

# This function stores genres into the genres database table
# The genre database table contains the movieID and the genres associated with a movie
def storeGenre(GenreID, genre):
  insert_stmt = ("INSERT INTO Genres (GenreID, genre)" \
  "VALUES (%s, %s)")
  data = (GenreID, genre)
  cur.execute(insert_stmt, data)
  cur.connection.commit()

# This function stores names into the names database table
# The names database table contains the movieID and the actors and directors associated with a movie
def storeName(NameID, name):
  insert_stmt = ("INSERT INTO Names (NameID, name)" \
  "VALUES (%s, %s)")
  data = (NameID, name)
  cur.execute(insert_stmt, data)
  cur.connection.commit()

# The main function that builds all the databases
def main(): 
  year = 1976
  GenreID = 1
  NameID = 1
  for year in range (1976,2016):
    #html link that changes with each year for a span of 40 years
    html = urlopen("http://www.imdb.com/search/title?year=" + str(year) + "," + str(year) + "&title_type=feature&sort=moviemeter,asc")
    bsObj = BeautifulSoup(html, "html.parser")
	
	# Scraping Titles of the Movies
    titles = bsObj.findAll('a', href=re.compile('/title/'))
    titleList = []
    for title in titles:
      if title.string != None and title.string != 'X':
        titleList.append(title.string)
    # print(titleList)
    # print(len(titleList))
	
    #Scraping Ratings of the Movies
    ratings = bsObj.findAll('span', attrs={'class':'value'})
    ratingList = []
    for rating in ratings:
        ratingList.append(rating.string)
    # print(ratingList)
    # print(len(ratingList))
 
    #Scraping Associated Genres of the Movies
    genres = bsObj.findAll('span', attrs={'class':'genre'})
    genreList = []
    for genre in genres:
      genreList.append(genre)
    genreList2 = []
    for i in range (0,50):
      genres1 = (genreList[i].findAll('a', href=re.compile('/genre/')))
      genre3 = []
      for genre1 in genres1:
        genre3.append(genre1.string)
      genreList2.append(genre3)
      genre3=[]
    # print(genreList2)
    # print(len(genreList2))
	
    #Scraping Classification of the Movies
    classifications = bsObj.findAll('span', attrs={'certificate'})
    classificationList = []
    for classification in classifications:
      classificationList.append(str(classification))
    #print(classificationList)
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
      
    # print(classificationList2)
    # print(len(classificationList2))

    #Scraping Names of the Directors and Actors in each Movies
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
    # print(AllNameList)
    # print(len(AllNameList))	
	
    # inserting movie data into mysql tables
    for i in range (0,50):
      storeMovie(titleList[i], year, ratingList[i], classificationList2[i])
    
    # inserting genre data into mysql tables
    for i in range (0,50):
      for j in range (len(genreList2[i])):
        storeGenre(GenreID, genreList2[i][j])
      GenreID += 1

    # inserting name data into mysql tables
    for i in range (0, 50):
      for j in range (len(AllNameList[i])):
        storeName(NameID, AllNameList[i][j])
      NameID += 1
	
main()