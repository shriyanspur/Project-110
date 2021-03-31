import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random
import pandas as pd
import csv

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

def randSetofMeans(limit):
  dataSet = []
  for i in range(0, limit):
    randIndex = random.randint(0, len(data)-1)
    value = data[randIndex]
    dataSet.append(value)

  mean = st.mean(dataSet)

  return mean

def show_chart(mean_list):
  df = mean_list
  mean = st.mean(df)
  fig = ff.create_distplot([df], ['reading_time'], show_hist = False)

  fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = 'lines', name = 'mean'))
  fig.show()

def setup():
  mean_list = []
  for i in range(0, 1000):
    setofMeans = randSetofMeans(100)
    mean_list.append(setofMeans)
  show_chart(mean_list)
  mean = st.mean(mean_list)
  stDev = st.stdev(mean_list)
  print('Mean of samples:',mean)
  print('StDev of samples:',stDev)

setup()