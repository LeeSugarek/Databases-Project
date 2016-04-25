import pymysql
import re
import random
conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='mysql')
cur = conn.cursor()
cur.execute("USE project")

def main():
  name = 'Will Smith'
  a = cur.execute("SELECT g.genre FROM Genres g INNER JOIN Names n \
  ON (g.Genreid = n.NameID) WHERE n.name = %s", name)
  genreList = []
  for i in range (a):
    genre = cur.fetchone()
    genre = str(genre)
    genre = genre[1:-2]
    print(genre)
    genreList.append(genre)
  genreDict = {}
  for i in range (len(genreList)):
    if genreList[i] in genreDict:
      genreDict[genreList[i]] = genreDict[genreList[i]] + 1
    else:
      genreDict[genreList[i]] = 1
  print(genreDict)
  # for i in range (len(genreDict)):
    # print(genreDict[i])
    
    
 # print(yearList)
  
  # year1 = 1976
  # countList = []
  # count = 0
  # for i in range (len(yearList)):
    # if yearList[i] == year1:
      # count += 1
    # else:
      # countList.append(count)
      # year1 += 1
      # count = 0
  # countList.append(count)
  # print(countList)
  # print(len(countList))
  # year1 = 1976
  # yearList2 = []
  # while year1 < 2016:
    # yearList2.append(year1)
    # year1 += 1
  # print(yearList2)
  # print(len(yearList2))
  
  
  

main()