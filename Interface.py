import plotly.plotly as py
import plotly.graph_objs as go

def main():
  print()
  print ("These queries use a database populated by the most popular movies from past 50 years.")
  print()
  print ("Below are the choices, select number to run query. The query might require further user input.")
  print()
  print ("1. Count of Action Movies vs. Year")
  print ("2. Rating of All Movies vs. Year")
  print ("3. Certification of All Movies vs. Year")
  print ("4. Movies Will Smith is in")
  print ("5. Ratings of Movies Will Smith is in")
  print ("6. Genres that Will Smith has Acted in")
  print()
  query = eval(input("Select desired query: "))
  print()
  
  #if (query == 1):
    py.sign_in('JDGrillo', 'ymn6lb95az')
    trace = go.Scatter(
      x = [],
      y = [],
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
        title="Action",
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
  
  #elif(query == 2):

  
  #elif(query == 3):

  
  #elif(query == 4):

  
  #elif(query == 5):
 
 
  #elif(query == 6):


  #else:
    #print("Query choice outside of range")
  
main()