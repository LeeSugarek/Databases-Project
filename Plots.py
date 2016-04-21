import plotly.plotly as py
import plotly.graph_objs as go
def main():
  py.sign_in('JDGrillo', 'ymn6lb95az')
  trace = go.Scatter(
    x = [1991,1992,1993,1994],
    y = [2,4,3,9],
    mode = 'markers'
	)
  data = [trace]
  layout = go.Layout(
    xaxis=dict(
	  title="X-Axis",
      titlefont=dict(
        family='Arial, sans-serif',
        size = 18,
        color='grey'
		),
      showexponent='All'
    ),
	yaxis=dict(
      title="Y-Axis",
      titlefont=dict(
        family='Arial, sans-serif',
        size = 18,
        color='lightgrey'
		),
      showexponent='All'
    )
	
    )
  pplot = go.Figure(data = data, layout=layout)	
  py.plot(pplot,filename= 'scatter')
main()