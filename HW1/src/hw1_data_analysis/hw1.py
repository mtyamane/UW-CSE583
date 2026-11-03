#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: hw1.py
Author: Mark Yamane
Date: 2026-11-03
Description: 
    This homework assignment is a set of pandas and matplotlib exercises using publically
    available data of bicycles crossing the Fremont Bridge since 2012.

Contact: mtyamane@uw.edu
Dependencies: pandas, matplotlib

https://www.geeksforgeeks.org/python/what-is-the-common-header-format-of-python-files/
"""
import pandas as pd
import matplotlib.pyplot as plt

"""
1. Read the CSV file into a pandas dataframe. (1pt)
"""
df = pd.read_csv('./bicycle_data.csv')

"""
2. In a comment, describe the columns in the dataframe and what data types they should
   be. If the data types in the dataframe do not match what you think they should be,
   update them. (1pt)

   Date:
     Date and time in MM/DD/YYYY HH:MM:SS format (should be type datetime)
   Fremont Bridge Sidewalks, south of N 34th St Total:
     Total count of bikes south of N 34th St (should be type int)
   Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk:
     Count of bikes south of N 34th St on the west sidewalk (should be type int)
   Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk:
     Count of bikes south of N 34th St on the east sidewalk (should be type int)

   The data types in the data frame do not match these expectations.
"""
# convert object to datetime
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %I:%M:%S %p')

# int coercion based on https://medium.com/analytics-vidhya/pandas-part-two-2973075d6484
df = df.astype({
    'Fremont Bridge Sidewalks, south of N 34th St Total': 'Int64',
    'Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk': 'Int64',
    'Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk': 'Int64'
})
# NOTE: Int64 handles NaNs, but np.int64 does not


"""
3. Add columns to the dataframe containing:
     The total (East + West) bicycle count. (1pt)
     The hour of the day. (1pt)
     The year. (1pt)
"""
df['total'] = df['Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk'] \
    + df['Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk']
df['hour'] = df['Date'].dt.hour
df['Year'] = df['Date'].dt.year


"""
#  4. Create a new dataframe with the subset of data from the year 2016. (1pt)
"""
df_2016 = df[df['Year'] == 2016]

"""
5. For the dataframe you created in 4, are there any time points with missing data? If so,
   do something to make sure missing data does not impact parts 6 and 7. In a comment in 
   the code write out the number of points with missing data. (1pt)
"""
# print row(s) with missing data; https://stackoverflow.com/questions/30447083/python-pandas-return-only-those-rows-which-have-missing-values
print(f'Row(s) with missing data:\n{df_2016[df_2016.isnull().any(axis=1)]}')

# 03/13/2016 has missing data at 02:00:00. I will drop this row.
df_2016 = df_2016.dropna()

"""
6. For the dataframe you created in 4, use pandas + matplotlib to plot the counts by hour
   (i.e. hour of the day on the x-axis, total daily counts on the y-axis). Add an appropriate
   title and name the axes and save the image to a file called counts_by_hour.png. (1pt)
"""
# color properties; https://stackoverflow.com/questions/39297093/change-the-facecolor-of-boxplot-in-pandas
color_props = {
    "boxes": "gray",
    "whiskers": "k",
    "medians": "k",
    "caps": "k"
}
ax = df_2016.boxplot(by='hour',
                     column='total',
                     grid=False,         # remove grid
                     color=color_props,  # use custom colors
                     patch_artist=True)  # fill boxes
ax.set_ylim(0, None)                     # set bottom of y-axis to 0

ax.set_xlabel('Hour')
ax.set_ylabel('Count (East + West)')
ax.set_title('Counts of cyclists on Fremont Bridge Sidewalks\nsouth of N 34th St ' \
             'in 2016, grouped by hour of day')
plt.suptitle('') # df boxplot default is an auto-generated suptitle, remove this

plt.tight_layout()
plt.savefig('./counts_by_hour.png')  # save to working directory

"""
7. For the dataframe you created in 4, use python (and pandas) programming to computationally
   determine what is (on average) the busiest hour of the day. In a comment in the code write
   out the busiest hour (1pt)
"""
print('The busiest hour of the day on average in 2016 for cyclists on the Fremont Bridge:')
print(f'{df_2016[['total', 'hour']].groupby('hour').median().idxmax()}')

# Hour 17, or 5 pm, was the busiest time of day on average for cyclists on the Fremont Bridge in 2016.