import plotly.plotly as py
import plotly.graph_objs as go
import pymysql
import re
import random
conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='mysql')
cur = conn.cursor()
cur.execute("USE project")

# main query function
def main():
  # Selects which query you want to run
  print()
  print ("These queries use a database populated by the most popular movies from past 50 years.")
  print()
  print ("Below are the choices, enter a number to run that query. The query might require further user input.")
  print()
  print ("1. Number of movies of a genre through the years")
  print ("2. Rating of the top movie of each year")
  print ("3. Number of movies with a certain classification through the years")
  print ("4. Movies a person has acted in or directed")
  print ("5. Genres that an actor has acted in or directed")
  print ("6. Ratings of movies of an actor or director")
  print()
  query = eval(input("Select desired query: "))
  print()
  
  # Query 1 function
  if (query == 1):
    # input for query 1
    genre = input("Enter Genre:")
    # SQL statement for query 1
    a = cur.execute("SELECT m.year FROM Movies m INNER JOIN Genres g \
    ON (m.id = g.GenreID) WHERE genre = %s", genre)
    
    # Builds lists of data to be used for graph
    yearList = []
    for i in range (a):
      year = cur.fetchone()
      year = str(year)
      year = year[1:-2]
      year = int(year)
      yearList.append(year)
    #print(yearList)
  
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
    # print(countList)
    # print(len(countList))
    year1 = 1976
    yearList2 = []
    while year1 < 2016:
      yearList2.append(year1)
      year1 += 1
    # print(yearList2)
    # print(len(yearList2))
	
    # Creates the graph
    py.sign_in('JDGrillo', 'ymn6lb95az')
	
    trace = go.Scatter(
      x = yearList2,
      y = countList,
      mode = 'markers'
	  )
    data = [trace]
    layout = go.Layout(
      xaxis=dict(
      
	    title="Year",
        titlefont=dict(
          family='Arial, sans-serif',
          size = 18,
          color='grey'
		  ),
        showexponent='All'
      ),
	  yaxis=dict(
        title="Number of Movies",
        titlefont=dict(
          family='Arial, sans-serif',
          size = 18,
          color='grey'
		  ),
        showexponent='All'
      )
	
    )
    pplot = go.Figure(data = data, layout=layout)	
    py.plot(pplot,filename= 'scatter')  
  
  # Query 2 function
  elif(query == 2):
    #SQL statement to execute
    a = cur.execute("SELECT m.year, m.rating FROM Movies m")
    
    # Builds lists to be used to graph
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
    # print(yearList)
    # print(ratingList)
    
    # builds graph
    py.sign_in('JDGrillo', 'ymn6lb95az')
	
    trace = go.Scatter(
      x = yearList,
      y = ratingList,
      mode = 'markers'
	  )
    data = [trace]
    layout = go.Layout(
      xaxis=dict(
	    title="Year",
        titlefont=dict(
          family='Arial, sans-serif',
          size = 18,
          color='grey'
		  ),
        showexponent='All'
      ),
	  yaxis=dict(
        title="Rating of Movie",
        titlefont=dict(
          family='Arial, sans-serif',
          size = 18,
          color='grey'
		  ),
        showexponent='All'
      )
	
    )
    pplot = go.Figure(data = data, layout=layout)	
    py.plot(pplot,filename= 'scatter')  
	  

  # Query 3 function
  elif(query == 3):
    # Input statement for query 3
    classification = input("Enter Classification(G, PG, PG_13, R, other):")
    # SQL statement for query 3
    a = cur.execute("SELECT m.year FROM Movies m WHERE classification = %s", classification)
    
    # Builds lists to be used to graph
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
    # print(countList)
    # print(len(countList))
    year1 = 1976
    yearList2 = []
    while year1 < 2016:
      yearList2.append(year1)
      year1 += 1
    # print(yearList2)
    # print(len(yearList2))
    
    # Builds the graph
    py.sign_in('JDGrillo', 'ymn6lb95az')
	
    trace = go.Scatter(
      x = yearList2,
      y = countList,
      mode = 'markers'
	  )
    data = [trace]
    layout = go.Layout(
      xaxis=dict(
      autotick = False,
      ticks = 'outside',
      tick0=0,
      dtick=1,
	    title="Year",
        titlefont=dict(
          family='Arial, sans-serif',
          size = 18,
          color='grey'
		  ),
        showexponent='All'
      ),
	  yaxis=dict(
        autotick=False,
        ticks='outside',
        tick0=0,
        dtick=1,
        title="Number of Movies",
        titlefont=dict(
          family='Arial, sans-serif',
          size = 18,
          color='grey'
		  ),
        showexponent='All'
      )
	
    )
    pplot = go.Figure(data = data, layout=layout)	
    py.plot(pplot,filename= 'scatter')  
  
  

  # Query 4 function
  elif(query == 4):
    # Input for query 4
    name = input("Enter Name:")
    # SQL statement for query 4
    a = cur.execute("SELECT m.title, m.year, m.rating, m.classification FROM Movies m INNER JOIN Names n \
    ON (m.id = n.NameID) WHERE n.name = %s", name)
    # Builds list to print out
    yearList = []
    for i in range (a):
      movie = cur.fetchone()
      movie = str(movie)
      print(movie)

  # Query 5 function
  elif(query == 5):
    # Input for query 5
    name = input("Enter Name:")
    # SQL Statement for query 5
    a = cur.execute("SELECT g.genre FROM Genres g INNER JOIN Names n \
    ON (g.Genreid = n.NameID) WHERE n.name = %s", name)
    # Builds dictionary of data
    genreList = []
    for i in range (a):
      genre = cur.fetchone()
      genre = str(genre)
      genre = genre[1:-2]
      # print(genre)
      genreList.append(genre)
    genreDict = {}
    for i in range (len(genreList)):
      if genreList[i] in genreDict:
        genreDict[genreList[i]] = genreDict[genreList[i]] + 1
      else:
        genreDict[genreList[i]] = 1
    # print(genreDict)
    # Prints out the dictionary data
    for i in genreDict:
      print(repr(i)[2:-2], ":", genreDict[i])
 
  # Query 7 function
  #elif(query == 6):


  else:
    print("Query choice outside of range")
  
main()
