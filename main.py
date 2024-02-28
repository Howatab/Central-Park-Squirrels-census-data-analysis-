import csv
import pandas

data = [ ]

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240227.csv")
color_count = {"black" : 0 , "cinnamon":0 ,"gray": 0}

Fur_colors = data["Primary Fur Color"].str.lower()
color_count = data["Primary Fur Color"].value_counts()

Counts_datagram = pandas.DataFrame(color_count).reset_index()
Counts_datagram.to_csv("ColorCounts.csv")
print(Counts_datagram)