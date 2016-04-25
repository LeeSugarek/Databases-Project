import pymysql
import re
import random
conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='mysql')
cur = conn.cursor()
cur.execute("USE project")

def main():
  a = cur.execute("SELECT m.year, m.rating FROM Movies m")
  alldata = []
  for i in range (a):
    data = cur.fetchone()
    data = str(data)
    data = data[1:-1]
    data = data.split(',')
 #   print(data)
    alldata.append(data)

  year1 = 1976
  yearList = []
  ratingList = []
#  print(alldata)
  for i in range (len(alldata)):
    if alldata[i][0] == str(year1):
      yearList.append(alldata[i][0])
      ratingList.append(alldata[i][1])
      year1 += 1
    else:
      continue
  print(yearList)
  print(ratingList)
	  
      
  #print(yearList)
  
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