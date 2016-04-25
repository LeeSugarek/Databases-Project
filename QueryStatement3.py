import pymysql
import re
import random
conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='mysql')
cur = conn.cursor()
cur.execute("USE project")

def main():
  a = cur.execute("SELECT m.year FROM Movies m WHERE classification = 'R'")
  yearList = []
  for i in range (a):
    year = cur.fetchone()
    year = str(year)
    year = year[1:-2]
    year = int(year)
    yearList.append(year)
 # print(yearList)
  
  year1 = 1976
  countList = []
  count = 0
  for i in range (len(yearList)):
    if yearList[i] == year1:
      count += 1
    else:
      countList.append(count)
      year1 += 1
      count = 0
  countList.append(count)
  print(countList)
  print(len(countList))
  year1 = 1976
  yearList2 = []
  while year1 < 2016:
    yearList2.append(year1)
    year1 += 1
  print(yearList2)
  print(len(yearList2))
  
  
  

main()