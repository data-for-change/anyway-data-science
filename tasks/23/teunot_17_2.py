import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from gmplot import gmplot
from pyproj.transformer import Transformer
from pyproj import Proj, transform
from bidi.algorithm import get_display
import seaborn as sns

#set sample size for writing
sample_size = 10000

#set segment to split with
segment = 'injury_severity'

#set timeframe
timeframe = 'weekday'

#load data
acc_data = pd.read_csv("C://Users//user//PycharmProjects//anyway//data//views_2019//involved_markers_hebrew.csv",nrows=sample_size,low_memory=False)

# create weekday
acc_data['weekday'] = pd.to_datetime(acc_data['accident_timestamp']).apply(lambda x: x.weekday())

#get dummies for segment
dummies = list(set(pd.get_dummies(acc_data,columns=[segment]).columns) - set(acc_data.columns))
acc_data = pd.get_dummies(acc_data,columns=[segment])

#create grouped table
acc_data = acc_data.groupby([timeframe])[dummies].sum().reset_index()

#add columns of deltas
for i in dummies:
    column_name = i + "_delta"
    acc_data[column_name] =acc_data[i].pct_change(+1).round(2)


#plot line
acc_data.plot(x=timeframe,y=dummies,kind="line")

#create labels
for i in dummies:
    for x,y,z in zip(acc_data[timeframe],acc_data[i],acc_data[i+"_delta"]):
        label = z
        plt.annotate(label, # this is the text
                     (x,y), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,10), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center

plt.title("Accident YoY by injury severity")
plt.show()