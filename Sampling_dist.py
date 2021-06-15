import csv
import plotly.graph_objects as go
import pandas as pd 
import plotly.express as ps 
import plotly.figure_factory as ff
import statistics
import random
 
df=pd.read_csv("data.csv") 
data=df["temp"].tolist()
mean=statistics.mean(data)
std_dev=statistics.stdev(data)
print(std_dev)
print(mean)
fig=ff.create_distplot([data],["temp"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
fig.show()
#find mean and deviation of 100 data points
dataset=[]
for i in range (0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)
mean=statistics.mean(dataset)
std_dev=statistics.stdev(dataset)  
print(std_dev)
print(mean)
def random_set_of_mean(counter):
    dataset=[]
    for i in range (0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
#plot the MEAN ON THE GRAPH
def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()
def setup():
    mean_list=[] 
    for i in range (0,1000) :
        set_of_mean= random_set_of_mean(100)   
        mean_list.append(set_of_mean)
    show_fig(mean_list)  
setup()  
def standard_deviation():
    mean_list=[]    
    for i in range (0,1000) :
        set_of_mean= random_set_of_mean(100)   
        mean_list.append(set_of_mean)
    std_dev=statistics.stdev(mean_list)  
    print(std_dev)    
standard_deviation()    