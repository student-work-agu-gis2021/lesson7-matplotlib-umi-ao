#!/usr/bin/env python
# coding: utf-8

# ## Problem 2 - Plotting temperatures 
# 
# In this problem we will  plot monthly mean temperatures from the Helsinki-Vantaa airpot for the past 30 years.
# 
# ## Input data
# 
# File `data/helsinki-vantaa.csv` monthly average temperatures from Helsinki Vantaa airport. Column descriptions:
# 
# ### Part 1
# 
# Load the Helsinki temperature data (`data/helsinki-vantaa.csv`)
# 
# - Read the data into variable called `data` using pandas
# - Parse dates from the column `'DATE'` and set the dates as index in the dataframe 

# YOUR CODE HERE 1 to read the data into data and parse dates
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("data/helsinki-vantaa.csv",parse_dates=['DATE'],index_col = 'DATE' )
# This test print should print first five rows
print(data.head())

# Check the number of rows in the data frame
print(len(data))

# ### Part 2
# 
# Select data for a 30 year period (January 1988 - December 2018)
# 
# - Store the selection in a new variable `selection`

# YOUR CODE HERE 2
data["date_time"] = pd.to_datetime(data.index)
selection = data[(data["date_time"].dt.year >= 1988 )& (data["date_time"].dt.year <=2018 )]
# Check that the data was read in correctly:
selection.head()

# Check how many rows of data you selected:
print("Number of rows:", len(selection))


# ### Part 3
# 
# #### Part 3.1
# 
# Create a line plot that displays the temperatures (`TEMP_C`) for yeach month in the 30 year time period:
#      
# #### Part 3.2
# 
# Save your figure as PNG file called `temp_line_plot.png`.
# 

# YOUR CODE HERE 3
monthly_data = pd.DataFrame()

selection['DATA_Month'] = selection["date_time"].astype(str).str.slice(start = 0, stop = 7)

grouped = selection.groupby('DATA_Month')

data1 = grouped.mean()

monthly_data['temp_celsius_monthly'] = data1['TEMP_C']
monthly_data["TIME"] = data1.index
monthly_data["TIME"]= monthly_data["TIME"].astype(str).str.slice(start = 0, stop = 4)

start_time = pd.to_datetime('19880101')
end_time = pd.to_datetime('20201231')

monthly_data.plot.line(x = 'TIME',y='temp_celsius_monthly',style = ['k.-'], figsize=(14,6))

plt.title("Helsinki-Vantaa Airport")
plt.xlabel("Time")
plt.ylabel("Temperature (Celsius)")
plt.grid()

# Set output file name
outputfp = "temp_line_plot.png"

# Save plot as image
# YOUR CODE HERE 4
plt.savefig("temp_line_plot.png")
import os

#Check that output file exists (also open the file and check that the plot looks ok!)
os.path.exists(outputfp)


# **REMINDER**: Don't forget to upload your figure and the modified notebook into your personal GitHub repository!
# 
# ### Done!
