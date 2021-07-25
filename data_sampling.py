import csv
import pandas as pd
import plotly.figure_factory as ff
import random
import statistics

df = pd.read_csv('medium_data.csv')
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print("Population mean:- ",str(population_mean))

def randomSetOfMeans(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
        mean = statistics.mean(dataset)
        return(mean)

def showFig(meanList):
    df = meanList
    fig = ff.create_distplot([df],["temp"],show_hist= False)
    fig.show()

def setup():
    meanList = []
    for i in range(0,100):
        set_of_means = randomSetOfMeans(30)
        meanList.append(set_of_means)
    showFig(meanList)

setup()