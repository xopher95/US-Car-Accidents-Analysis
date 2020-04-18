import csv
import sys
import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt
import os
from collections import Counter

os.chdir(r'D:\Parseltongue\Py4 - US Accidents')

use_col = ['Severity','Start_Time', 'State', 'Temperature(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)','Weather_Condition']


raw = pd.read_csv('US_Accidents_Dec19.csv',usecols = use_col)


raw['Start_Time'] = pd.to_datetime(raw['Start_Time'])    #row: 2974335, dtype: datetime64[ns]
raw['dates'] = pd.to_datetime(raw['Start_Time'].dt.date) # dates only, dtype: datetime64[ns]
raw['time'] = pd.to_datetime(raw['Start_Time']).dt.time # time only, dtype: object



dt = raw['dates']   #create a variable soley on raw['dates']
dates = []




for i in range(len(dt)):
    dates.append(dt[i].strftime("%m/%Y"))   #change from mm/dd/yyyy to just mm/YYYY store into a new list call dates

# I think the code runs congested here, takes longer time to load due to the conversion above. I have created a new cell so that I can process faster from next onwards.


chart_data = Counter(dates) # turns into a dictionary to keep key and value data
plt.figure(figsize=(50,40))  # width:20, height:40
plt.bar(chart_data.keys(), chart_data.values())   # plot data, x as key, y as values|
plt.show()
