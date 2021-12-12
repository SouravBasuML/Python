"""
-----------------------------------------------------------------------------------------------------------------------
Matplotlib: Line, Bar, Pie, Stack, Area, Histogram, Scatter, Time-Series, BoxPlot
-----------------------------------------------------------------------------------------------------------------------
"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter
import csv
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates
from pandas.plotting import register_matplotlib_converters
import random
from itertools import count
from matplotlib.animation import FuncAnimation


# print(plt.style.available)
# plt.xkcd()                      # python antigravity style
plt.style.use('ggplot')


# ---------------------------------------------------------------------------------------------------------------------
# Initial Data:
# ---------------------------------------------------------------------------------------------------------------------
# Developer Age
age_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
         36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

# Median All Developer Salaries by Age
dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928,
         67317, 68748, 73752, 77232, 78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660,
         98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]

# Median Python Developer Salaries by Age
py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000,
            71496, 75370, 83640, 84666, 84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736,
            112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

# Median JavaScript Developer Salaries by Age
js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674,
            68745, 68746, 74583, 79000, 78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660,
            102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]


# ---------------------------------------------------------------------------------------------------------------------
# Line Graph
# ---------------------------------------------------------------------------------------------------------------------
# plt.plot(age_x, dev_y, color='#444444', linestyle='-.', marker='.', label='All Developers')
# plt.plot(age_x, py_dev_y, color='#5a7d9a', linewidth=2.0, marker='.', label='Python Developers')
# plt.plot(age_x, js_dev_y, color='#adad3b', linewidth=1.0, marker='.', label='JS Developers')
# plt.title('Median Developer Salary (USD) by Age')
# plt.xlabel('Age')
# plt.ylabel('Median Salary (USD)')
# plt.legend(loc='lower right')
# plt.grid(True)
# plt.tight_layout()
# # plt.savefig('line_chart.png')
# plt.show()


# ---------------------------------------------------------------------------------------------------------------------
# Vertical Bar Graph
# ---------------------------------------------------------------------------------------------------------------------
# x_indexes = np.arange(len(age_x))   # creates a numpy array of a list of numbers from 0 to length of age_x
# width = 0.25
# plt.bar(x_indexes - width, dev_y, color='#444444', width=width, label='All Developers')
# plt.bar(x_indexes, py_dev_y, color='#5a7d9a', width=width, label='Python Developers')
# plt.bar(x_indexes + width, js_dev_y, color='#adad3b', width=width, label='JS Developers')
# plt.title('Median Developer Salary (USD) by Age')
# plt.xlabel('Age')
# plt.ylabel('Median Salary (USD)')
# plt.legend(loc='best')
# plt.xticks(ticks=x_indexes, labels=age_x)
# plt.grid(True)
# plt.tight_layout()
# # plt.savefig('line_chart.png')
# plt.show()


# ---------------------------------------------------------------------------------------------------------------------
# Horizontal Bar Graph
# ---------------------------------------------------------------------------------------------------------------------
# data = pd.read_csv('ProgrammingLanguages.csv')
# lang_responses = data['LanguagesWorkedWith']
# language_counter = Counter()
# for responses in lang_responses:
#     language_counter.update(responses.split(';'))
#
# # with open('ProgrammingLanguages.csv') as csv_file:
# #     csv_reader = csv.DictReader(csv_file)
# #     language_counter = Counter()                    # empty counter
# #     for row in csv_reader:
# #         language_counter.update(row['LanguagesWorkedWith'].split(';'))
#
# languages = []
# popularity = []
# for item in language_counter.most_common(15):       # item is a list of tuples
#     languages.append(item[0])
#     popularity.append(item[1])
#
# languages.reverse()
# popularity.reverse()
#
# plt.barh(languages, popularity, color='#444444', label='All Developers')
# plt.title('Most Popular Languages')
# plt.xlabel('Popularity')
# plt.grid(True)
# plt.tight_layout()
# plt.show()


# ---------------------------------------------------------------------------------------------------------------------
# Pie Chart
# ---------------------------------------------------------------------------------------------------------------------
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
# slices = [59219, 55466, 47544, 36443, 35917]
# explode = [0, 0, 0, 0.1, 0]
# plt.pie(slices, labels=labels, shadow=True, explode=explode, startangle=90,
#         autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
# plt.title('Popularity of Top Five Programming Languages')
# plt.tight_layout()
# plt.show()


# ---------------------------------------------------------------------------------------------------------------------
# Stack Plot
# ---------------------------------------------------------------------------------------------------------------------
# minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
# player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
# player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]
#
# labels = ['Player1', 'Player2', 'Player3']
# plt.stackplot(minutes, player1, player2, player3, labels=labels)
# plt.title('Player Points by Minutes')
# plt.xlabel('Minutes')
# plt.ylabel('Player Points')
# plt.legend(loc='upper left')
# plt.show()


# ---------------------------------------------------------------------------------------------------------------------
# Filling Areas on Line Plots
# ---------------------------------------------------------------------------------------------------------------------
# data = pd.read_csv('ProgLangSalaries.csv')
# age = data['Age']
# dev_salary = data['All_Devs']
# py_salary = data['Python']
# js_salary = data['JavaScript']
# overall_median_salary = 57287
#
# plt.plot(age, dev_salary, label='Dev Salary')
# plt.plot(age, py_salary, label='Python Salary')
# # plt.fill_between(x1, y1, y2=0, alpha=transparency)
# plt.fill_between(age, py_salary, overall_median_salary, alpha=0.25,
#                  where=(py_salary > overall_median_salary), interpolate=True,
#                  color='blue', label='Above Median Avg')
# plt.fill_between(age, py_salary, overall_median_salary, alpha=0.25,
#                  where=(py_salary <= overall_median_salary), interpolate=True,
#                  color='red', label='Below Median Avg')
# plt.title('Median Salary by Age')
# plt.xlabel('Age')
# plt.ylabel('Salary')
# plt.tight_layout()
# plt.legend()
# plt.show()


# ---------------------------------------------------------------------------------------------------------------------
# Histogram
# ---------------------------------------------------------------------------------------------------------------------
# data = pd.read_csv('Ages.csv')
# ids = data['Responder_id']
# age = data['Age']
# bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]         # 10 bars
# median_age = 29
# plt.hist(age, bins=bins, edgecolor='black', log=True)       # logarithmic scale
# plt.axvline(median_age, color='green', label='Age Median', linewidth=2)
# plt.legend()
# plt.title('Histogram of Respondent Ages')
# plt.xlabel('Ages')
# plt.ylabel('Respondents')
# plt.tight_layout()
# plt.show()


# ---------------------------------------------------------------------------------------------------------------------
# Scatter Plots
# ---------------------------------------------------------------------------------------------------------------------
# data = pd.read_csv('YouTubeData.csv')
# view_count = data['view_count']
# likes = data['likes']
# ratio = data['ratio']
#
# plt.scatter(view_count, likes, c=ratio, cmap='summer', marker='o', edgecolors='black', linewidth=1, alpha=0.75)
# color_bar = plt.colorbar()
# color_bar.set_label('Like/Dislike Ratio')
# plt.xscale('log')
# plt.yscale('log')
# plt.title('Trending YouTube Videos')
# plt.xlabel('View Count')
# plt.ylabel('Total Likes')
# plt.tight_layout()
# plt.show()


# ---------------------------------------------------------------------------------------------------------------------
# Plotting Time-Series Data
# ---------------------------------------------------------------------------------------------------------------------
# # Future Warning: Explicitly register datetime converter for a matplotlib plotting method - plt.plot_date()
# register_matplotlib_converters()
#
# data = pd.read_csv('BitCoinPrices.csv')
#
# # Sort the data in asc order of dates:
# data['Date'] = pd.to_datetime(data['Date'])     # convert date column from string to date type
# data.sort_values('Date', inplace=True)
#
# price_date = data['Date']
# price_close = data['Close']
# plt.plot_date(price_date, price_close, linestyle='solid')
#
# # Rotate the x-axis dates to fit better:
# # Run the autofmt_xdate() function on the figure (not on the plt object)
# # To get the current figure, use plt.gcf() - get current figure
# plt.gcf().autofmt_xdate()
#
# # # Format dates on the x-axis:
# # date_format = mpl_dates.DateFormatter('%b %d, %Y')      # May 25, 2020
# # # Get the axis use plt.gca() - get current axis
# # plt.gca().xaxis.set_major_formatter(date_format)
#
# plt.title('BitCoin Price Trend')
# plt.xlabel('Date')
# plt.ylabel('Closing Price (USD)')
# plt.tight_layout()
# plt.show()


# ---------------------------------------------------------------------------------------------------------------------
# Plotting Real-Time Data
# ---------------------------------------------------------------------------------------------------------------------
# x_vals = []
# y1_vals = []
# y2_vals = []
# index = count()                                 # from itertools import count
#
#
# def animate(i):
#     x_vals.append(next_node(index))                  # counts up by 1
#     y1_vals.append(random.randint(-5, 5))
#     y2_vals.append(random.randint(-5, 5))
#     plt.cla()                                   # clear axis so that it plots from scratch everytime
#     plt.plot(x_vals, y1_vals, label='Sensor 1')
#     plt.plot(x_vals, y2_vals, label='Sensor 2')
#     plt.legend(loc='upper right')
#     plt.tight_layout()
#
#
# # from matplotlib.animation import FuncAnimation
# # Parameters: current figure, function to run, interval in ms
# ani = FuncAnimation(plt.gcf(), animate, interval=200)
#
# plt.show()


# ---------------------------------------------------------------------------------------------------------------------
# Sub-Plots: 1 figure, 2 axes (plots)
# ---------------------------------------------------------------------------------------------------------------------
# fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)    # 1 figure, 2 axes (plots)
#
# ax1.plot(age_x, dev_y, color='#444444', linestyle='-.', marker='.', label='All Developers')
# ax2.plot(age_x, py_dev_y, color='#5a7d9a', linewidth=2.0, marker='.', label='Python Developers')
# ax2.plot(age_x, js_dev_y, color='#adad3b', linewidth=1.0, marker='.', label='JS Developers')
#
# ax1.legend()
# ax1.set_title('Median Developer Salary (USD) by Age')
# ax1.set_ylabel('Median Salary (USD)')
#
# ax2.legend()
# ax2.set_xlabel('Age')
# ax2.set_ylabel('Median Salary (USD)')
#
# plt.tight_layout()
# plt.show()


# ---------------------------------------------------------------------------------------------------------------------
# Sub-Plots: 2 figures, 2 axes (plots)
# ---------------------------------------------------------------------------------------------------------------------
# fig1, ax1 = plt.subplots()
# fig2, ax2 = plt.subplots()
#
# ax1.plot(age_x, dev_y, color='#444444', linestyle='-.', marker='.', label='All Developers')
# ax2.plot(age_x, py_dev_y, color='#5a7d9a', linewidth=2.0, marker='.', label='Python Developers')
# ax2.plot(age_x, js_dev_y, color='#adad3b', linewidth=1.0, marker='.', label='JS Developers')
#
# ax1.legend()
# ax1.set_title('Median Developer Salary (USD) by Age')
# ax1.set_xlabel('Age')
# ax1.set_ylabel('Median Salary (USD)')
#
# ax2.legend()
# ax2.set_title('Median Developer Salary (USD) by Age')
# ax2.set_xlabel('Age')
# ax2.set_ylabel('Median Salary (USD)')
#
# plt.tight_layout()
# plt.show()
#
# # fig1.savefig('fig1.png')
# # fig2.savefig('fig2.png')


"""
-----------------------------------------------------------------------------------------------------------------------
Box & Whisker Plot:
-----------------------------------------------------------------------------------------------------------------------
Box plot is the visual representation of the statistical five number summary of a given data set.
    Minimum
    First Quartile
    Median (Second Quartile)
    Third Quartile
    Maximum
Outlier:
    Measurements lying outside 3Q + 1.5IQR or 1Q - 1.5IQR
"""
