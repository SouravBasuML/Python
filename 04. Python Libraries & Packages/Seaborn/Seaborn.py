import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ---------------------------------------------------------------------------------------------------------------------
# Seaborn:
# ---------------------------------------------------------------------------------------------------------------------
# Themes: 'darkgrid', 'whitegrid', 'dark', 'white', 'ticks'
sns.set_style('whitegrid')


# ---------------------------------------------------------------------------------------------------------------------
# Line Plot:
# ---------------------------------------------------------------------------------------------------------------------
# Line charts are best to show trends over a period of time, and multiple lines can be used to show trends in more
# than one group.
# ---------------------------------------------------------------------------------------------------------------------

# fifa = pd.read_csv('fifa.csv', index_col='Date', parse_dates=True)
# print(fifa.head())
#
# plt.figure(figsize=(16, 6))                         # in inches
# # sns.lineplot(data=fifa)
#
# sns.lineplot(data=fifa['ARG'], label='ARG')
# sns.lineplot(data=fifa['BRA'], label='BRA')
#
# plt.xlabel('Date')
# plt.ylabel('Ranking')
# plt.title(' FIFA Rankings')
# plt.show()


# ---------------------------------------------------------------------------------------------------------------------
# Bar Chart:
# ---------------------------------------------------------------------------------------------------------------------
# Bar charts are useful for comparing quantities corresponding to different groups.
# ---------------------------------------------------------------------------------------------------------------------

flight_delay = pd.read_csv('flight_delay.csv', index_col='Month')
print(flight_delay.head())

plt.figure(figsize=(10, 6))
sns.barplot(x=flight_delay.index, y=flight_delay['AS'])

plt.xlabel('Month')
plt.ylabel('Delay in minutes')
plt.title('Average Monthly Flight Delay of Alaskan Airlines (in minutes)')
plt.show()


# ---------------------------------------------------------------------------------------------------------------------
# Heat Map:
# ---------------------------------------------------------------------------------------------------------------------
# Heatmaps can be used to find color-coded patterns in tables of numbers.
# ---------------------------------------------------------------------------------------------------------------------

# flight_delay = pd.read_csv('flight_delay.csv', index_col='Month')
# print(flight_delay.head())
#
# # By default seaborn uses cmap = sns.cm.rocket. To invert the heat map, set cmap = sns.cm.rocket_r
# # Other examples:
# #   cmap = 'Blues' or cmap = 'Blues_r'
# #   cmap = 'YlGnBu' or cmap = 'YlGnBu_r' etc.
# cmap = 'YlGnBu'
#
# plt.figure(figsize=(14, 7))
# sns.heatmap(data=flight_delay, annot=True, cmap=cmap)
# plt.title('Average Monthly Flight Delay (in minutes)')
# plt.show()


# ---------------------------------------------------------------------------------------------------------------------
# Scatter Plot, Regression Plot, Swarm Plot (Categorical Scatter Plot):
# ---------------------------------------------------------------------------------------------------------------------
# 1. Scatter plots show the relationship between two continuous variables; if color-coded, we can also show the
#    relationship with a third categorical variable.
# 2. A regression line in the scatter plot makes it easier to see any linear relationship between two variables.
# 3. LML Plot is useful for drawing multiple regression lines, if the scatter plot contains multiple, color-coded
#    groups
# 4. Swarm Plot (Categorical scatter plots) show the relationship between a continuous variable and a categorical
#    variable.
# ---------------------------------------------------------------------------------------------------------------------

# insurance = pd.read_csv('insurance.csv')
# print(insurance.head())
#
# plt.figure(figsize=(8, 6))
#
# # Scatter Plot:
# sns.scatterplot(x=insurance['bmi'], y=insurance['charges'])
#
# # Regression Plot:
# sns.regplot(x=insurance['bmi'], y=insurance['charges'])
#
# # Color-Coded Scatter Plots (to display the relationships between three variables):
# sns.scatterplot(x=insurance['bmi'], y=insurance['charges'], hue=insurance['smoker'])
#
# # Regression Plot on Color-coded scatter plot:
# sns.lmplot(x='bmi', y='charges', hue='smoker', data=insurance)
#
# # Swarm Plot (Categorical Scatter Plot)
# sns.swarmplot(x=insurance['smoker'], y=insurance['charges'])
# # plt.xlabel('Smoker')
#
#
# plt.title('Insurance Charges')
# plt.xlabel('BMI')
# plt.ylabel('Ins. Charge')
# plt.show()


# ---------------------------------------------------------------------------------------------------------------------
# Histogram, Kernel Density Estimate (KDE):
# ---------------------------------------------------------------------------------------------------------------------
# 1. Histograms show the distribution of a single numerical variable.
# 2. KDE plots (or 2D KDE plots) show an estimated, smooth distribution of a single numerical variable (or two
#    numerical variables).
# 3. Joint Plot is useful for simultaneously displaying a 2D KDE plot with the corresponding KDE plots for each
#    individual variable.
# ---------------------------------------------------------------------------------------------------------------------

# # distplot is deprecated. Use:
# #   `displot` (a figure-level function with similar flexibility) or
# #   `histplot` (an axes-level function for histograms)
#
# iris = pd.read_csv('iris.csv', index_col='Id')
# print(iris.head())
# print(iris.columns)
#
#
# # Histogram:
# # kde = True also adds a kde plot along with the histogram
# plt.figure(figsize=(8, 6))
# sns.distplot(a=iris['SepalWidthCm'], kde=False)
#
#
# # Kernel Density Estimate (KDE):
# # shade=True shades the area under the kde curve
# sns.kdeplot(data=iris['SepalWidthCm'], shade=False)
#
#
# # 2D KDE Plots
# # kind='kde' -> plots a contour plot and kde plots (x-axis) on top and right (y-axis)
# # Without kind='kde' -> plots a scatter plot and histograms on top (x-axis) and right (y-axis)
# sns.jointplot(x=iris['PetalLengthCm'], y=iris['SepalWidthCm'], kind='kde')
#
# plt.title('Iris Distributions')
# plt.show()


# ---------------------------------------------------------------------------------------------------------------------
# Color-Coded Plots (Histogram, KDE):
# ---------------------------------------------------------------------------------------------------------------------

# iris = pd.read_csv('iris.csv', index_col='Id')
# iris_set = iris[iris.Species == 'Iris-setosa']
# iris_ver = iris[iris.Species == 'Iris-versicolor']
# iris_vir = iris[iris.Species == 'Iris-virginica']
#
# # Color-Coded Histogram:
# # sns.distplot(a=iris_set['PetalLengthCm'], label='Iris-Setosa', kde=False)
# # sns.distplot(a=iris_ver['PetalLengthCm'], label='Iris-Versicolor', kde=False)
# # sns.distplot(a=iris_vir['PetalLengthCm'], label='Iris-Virginica', kde=False)
#
# # Color-Coded KDE Plot:
# sns.kdeplot(data=iris_set['PetalLengthCm'], label="Iris-Setosa", shade=True)
# sns.kdeplot(data=iris_ver['PetalLengthCm'], label="Iris-Versicolor", shade=True)
# sns.kdeplot(data=iris_vir['PetalLengthCm'], label="Iris-Virginica", shade=True)
#
# plt.title('Distribution of Petal Lengths, by Species')
# plt.legend()
# plt.show()
