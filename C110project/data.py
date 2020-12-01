import random 
import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff 
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()
population_mean = statistics.mean(data)
print("The population mean is "+str(population_mean))

def setup():
    mean_list=[]
    for i in range(0,100):
        mean_sets = random_means(30)
        mean_list.append(mean_sets)
    show_graph(mean_list)

def random_means(counter):
    dataset=[]
    for i in range(0,counter):
        index = random.randint(0,len(data)-1)
        value = data[index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
    print("The mean of samples is "+str(mean))

def show_graph(mean_list):
    data_1 = mean_list
    fig = ff.create_distplot([data_1],["claps"],show_hist= False)
    #fig.add_trace(go.Scatter(x=[data_1,data_1], y=[0,1], mode="lines",  name="mean"))
    fig.show()


setup()