import csv
import pandas as pd
import plotly.figure_factory as px
import statistics as st
import random



rolls = pd.read_csv('yes.csv')
rolls = rolls['temp'].tolist()






meanp = st.mean(rolls)
standardp = st.stdev(rolls)

print(standardp, meanp)

def hi(d):
    data1 = []
    for i in range(0, d):
        position = random.randint(0, len(rolls) - 1)
        value = rolls[position]
        data1.append(value)
    mean = st.mean(data1)
    dev = st.stdev(data1)
    
    return mean



def hello():
    data = []
    for e in range(0, 1000):
        setofmeans = hi(100)
        data.append(setofmeans)
    dev = st.stdev(data)
    mean = st.mean(data)

    graph = px.create_distplot([data], ['temp'])

    graph.show()

    print(dev, mean)





hello()







