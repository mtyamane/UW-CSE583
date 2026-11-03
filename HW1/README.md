# HW1: python data analysis basics

This homework assignment is a set of pandas and matplotlib exercises using publically available data of bicycles crossing the Fremont Bridge since 2012 (as described in <https://data.seattle.gov/Transportation/Fremont-Bridge-Hourly-Bicycle-Counts-by-Month-Octo/65db-xm6k>).

The end product for this assignment was this figure:

![Counts of cyclists on Fremont Bridge Sidewalks](/src/hw1_data_analysis/counts_by_hour.png)

### 8. Describe your process for doing this homework. (If you used an AI assist, please tell us so here. It will not affect your grade as long as you tell us.) Answer this question by editing the README.md file. (1pt)

I built up the assignment in VSCode and referenced multiple sites for documentation of the various pandas and matplotlib functions, mainly for argument specification. I was pretty familiar with pandas prior to this assignment, so I didn't use AI for this one.

### Bonus

In this assignment, I converted the "Date" column into Pandas datetimes. Datetimes allow for data manipulation of dates and times in a way that is intuitive. There are three common packages that can convert date and time strings into datetime objects `datetime.datetime`, Numpy, and Pandas. Python's `datetime` package has `datetime.datetime` which is native, so no additional packages are required to install but Python is naturally a slow language so `datetime` functions and instantiations are slow. Numpy is C-compiled so most operations, including `np.datetime64` instantiation and manipulation are much faster than `datetime.datetime`. Pandas works off a wrapper for Numpy, so `pd.to_datetime` uses `np.datetime64` but provides additional flexibility and often handles more common errors. I used `pd.to_datetime` out of convenience.

Additional reference [here](https://daviskirkendall.com/2015/02/19/datetime-vs.-numpy-vs.-pandas/).