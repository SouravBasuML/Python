# ---------------------------------------------------------------------------------------------------------------------
# Pandas: Panel Data
# ---------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np

# Dictionary:
people = {
    "first_name": ['F1', 'F2', 'F3'],
    "last_name": ['L1', 'L2', 'L3'],
    "email": ['F1@email.com', 'F2@email.com', 'F3@email.com']
}

people1 = {
    'first_name': ['F1', 'F2', 'F3'],
    'last_name': ['L1', 'L2', 'L3'],
    'email': ['F1@email.com', 'F2@email.com', 'F3@email.com'],
    'salary': [75_000, 100_000, 80_000]
}


# ---------------------------------------------------------------------------------------------------------------------
# Pandas Dataframe:
# ---------------------------------------------------------------------------------------------------------------------
# fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]},
#                            index=['2017 Sales', '2018 Sales'])
# print('\nData Frame: \n', fruit_sales)


# ---------------------------------------------------------------------------------------------------------------------
# Pandas Series:
# ---------------------------------------------------------------------------------------------------------------------
# ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'],
#                         index=['Flour', 'Milk', 'Eggs', 'Spam'],
#                         name='Dinner')
# print('\nSeries:\n', ingredients)

# ingredients.to_csv('path\filename.csv')


# ---------------------------------------------------------------------------------------------------------------------
# Datatypes:
# ---------------------------------------------------------------------------------------------------------------------
# print('\nDatatype of "fruit_sales" DataFrame:\n', fruit_sales.dtypes)
# print('\nDatatype of "Apples" Series:\n', fruit_sales.Apples.dtype)
# print('\nDatatype of the DataFrame "index":\n', fruit_sales.index.dtype)
#
# print('\nChanging Datatype of "Apples" Series to float64:\n', fruit_sales.Apples.astype('float64'))
# print('\nChanging Datatype of entire "fruit_sales" DataFrame to float64:\n', fruit_sales.astype('float64'))

# # to convert to String: fruit_sales.astype(str)

# ---------------------------------------------------------------------------------------------------------------------
# NaN (Not a Number):
# ---------------------------------------------------------------------------------------------------------------------
# # Missing entries are given the value 'NaN'. NaN values are always float64 dtype.
# df = pd.DataFrame({'Apples': [35, 41, None, None], 'Bananas': [21, 34, 45, None]},
#                            index=['2017 Sales', '2018 Sales', '2019 Sales', '2020 Sales'])
# print('\nData Frame:\n', df)
# print('\nUnavailable Apple Sales:\n', df[pd.isnull(df.Apples)])
# print('\nUnavailable Apple Sales:\n', df.Apples.isnull().sum())
# print('\nUnavailable Banana Sales:\n', df[pd.isnull(df.Bananas)])
# print('\nAvailable Apple Sales:\n', df[pd.notnull(df.Apples)])
# print('\nAvailable Banana Sales:\n', df[pd.notnull(df.Bananas)])

# df = df.fillna(0)
# print('\nData Frame:\n', df)


# ---------------------------------------------------------------------------------------------------------------------
# Visualizing Pandas Dataframe
# ---------------------------------------------------------------------------------------------------------------------
# df = pd.read_csv('survey_results_public.csv')
# schema_df = pd.read_csv('survey_results_schema.csv')

# print(df.head())                          # prints first 5 rows
# print(df.head(10))                        # prints first 10 rows
# print(df.tail())                          # prints last 5 rows
# print(df.tail(20))                        # prints last 20 rows
# print(df.sample())                        # prints a ramdom sample
# print(df.sample(10))                      # prints 10 ramdom samples


# print(df.shape)                           # (88883 x 85).         shape is an attribute of df class not a method
# print(df.size)                            # 7555055 (row x col)   size is an attribute of df class not a method
# print(df.info())                          # prints number of rows and columns + all columns and their data types
# print(df.columns)                         # prints all column names
# pd.set_option('display.max_columns', 85)  # to display 85 columns (looks better in jupyter notebook)
# print(df)
# pd.set_option('display.max_rows', 85)     # to display 85 rows
# print(schema_df)


# ---------------------------------------------------------------------------------------------------------------------
# DataFrame and Series:
# ---------------------------------------------------------------------------------------------------------------------
# # Create DataFrame from Dictionary:
# df1 = pd.DataFrame(people)
# print('\nDataFrame:')
# print(df1)
# print('\nDataFrame Columns:')
# print(df1.columns)                                  # Index(['first_name', 'last_name', 'email'], dtype='object')


# ---------------------------------------------------------------------------------------------------------------------
# Reading Columns:
# ---------------------------------------------------------------------------------------------------------------------
# # Series is a 1-D data array; it is data of a single column.
# # DataFrame is a container of multiple Series objects. Series also has index

# # Reading a single column:
# print('\nReading a single column:')
# print(df1['email'])
# print(type(df1['email']))                           # Returns a Series:     <class 'pandas.core.series.Series'>
# print(df1.email)                                    # Not the preferred way to access columns
# print(type(df1.email))                              # Returns a Series:     <class 'pandas.core.series.Series'>
# print(type(df1))                                    # Returns a DataFrame:  <class 'pandas.core.frame.DataFrame'>
# print(df1[['email']])
# print(type(df1[['email']]))                         # Returns a DataFrame:  <class 'pandas.core.frame.DataFrame'>
# print(df['Hobbyist'].value_counts())                # Groups by the column values


# ---------------------------------------------------------------------------------------------------------------------
# Reading Multiple Columns:
# ---------------------------------------------------------------------------------------------------------------------
# print('\nReading multiple columns:')
# print(df1[['last_name', 'email']])                  # Pass the columns as a list
# print(type(df1[['last_name', 'email']]))            # Will always be a DataFrame

# # Reading specific columns of specific rows:
# print('\nReading specific columns of specific rows:')
# print(df1[['last_name', 'email']][0: 2])            # Read specific columns from the first to rows


# ---------------------------------------------------------------------------------------------------------------------
# Reading Rows:
# ---------------------------------------------------------------------------------------------------------------------
# iloc is conceptually simpler than loc because it ignores the dataset's indices. When we use iloc we treat the dataset
# like a big matrix (a list of lists), one that we have to index into by position.
# loc, by contrast, uses the information in the indices to do its work. Since your dataset usually has meaningful
# indices, it's usually easier to do things using loc instead.

# iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one
# excluded. So 0:10 will select entries 0,...,9.
# loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.
# ---------------------------------------------------------------------------------------------------------------------
# # 1. iloc: Reading rows at integer locations.

# # Reading a single row:
# print('\nReading a single row:')
# print(df1.iloc[0])                                  # Reading first row as Series. Column names become the index
# print(type(df1.iloc[0]))                            # Series: <class 'pandas.core.series.Series'>
# print(df1.iloc[[0]])                                # Reading first row as a DataFrame
# print(type(df1.iloc[[0]]))                          # DataFrame: <class 'pandas.core.frame.DataFrame'>


# ---------------------------------------------------------------------------------------------------------------------
# Reading multiple rows:
# ---------------------------------------------------------------------------------------------------------------------
# print('\nReading multiple rows:')
# print(df1.iloc[[0, 1]])                             # Reading first two rows
# print(type(df1.iloc[[0, 1]]))                       # DataFrame: <class 'pandas.core.frame.DataFrame'>
# print(df1.iloc[0: 2])                               # Reading first two rows
# print(type(df1.iloc[0: 2]))                         # DataFrame: <class 'pandas.core.frame.DataFrame'>

# # Reading specific columns of specific rows: iloc[[rows], [cols]]. Can't use column names with iloc
# print('\nReading specific columns of specific rows:')
# print(df1.iloc[[0, 1], 2])                          # Reading third column of the first two rows
# print(df1.iloc[[0, 1], [0, 2]])                     # Reading first and third columns of the first two rows
# print(df1.iloc[:, 0])                               # Reading first column of all rows
# print(df1.iloc[:2, 0])                              # Reading first column of first two rows
# print(df1.iloc[-2:])                                # Reading last two rows


# ---------------------------------------------------------------------------------------------------------------------
# 2. loc: Read rows by label (index)
# ---------------------------------------------------------------------------------------------------------------------
# # Reading a single row:
# print(df1.loc[0])                                   # Reading first row, i.e. row with index 0 (as Series)
# print(df1.loc[[0]])                                 # Reading first row, i.e. row with index 0 (as DataFrame)

# # Reading multiple rows:
# print(df1.loc[[0, 1]])                              # Reading first two rows, i.e. row with index 0 and 1
# print(df1.loc[1: 2])                                # Reading rows at index 1 and 2 (last value inclusive)

# # Reading rows and columns (We can use column names):
# print(df1.loc[[0, 1], 'email'])                     # Reading email column of first two rows
# print(df1.loc[[0, 1], ['email', 'last_name']])      # Reading multiple columns
# print(df1.loc[0:2, 'first_name':'email'])           # Slicing (last value inclusive)

# print(df['Hobbyist'])
# print(df['Hobbyist'].value_counts())
# print(df.loc[0:3, 'Hobbyist':'Employment'])         # 0 and 3 are inclusive)


# ---------------------------------------------------------------------------------------------------------------------
# Index: (values need not be unique)
# ---------------------------------------------------------------------------------------------------------------------
# df2 = pd.DataFrame(people)
# df2.set_index('email', inplace=True)                # inplace=True modifies the DataFrame
# print(df2)
# print(df2.index)                                    # Index(['F1@email.com', 'F2@email.com', 'F3@email.com'])
# print(df2.loc['F1@email.com'])                      # Reading row by index as a Series
# print(df2.loc[['F1@email.com']])                    # Reading row by index as a DataFrame
# print(df2.loc['F1@email.com', 'first_name'])        # Reading specific columns
# df2.reset_index(inplace=True)                       # Resetting index
# print(df2)

# # Setting index while reading csv:
# # --------------------------------
# response_df = pd.read_csv('survey_results_public.csv', index_col='Respondent')
# schema_df = pd.read_csv('survey_results_schema.csv', index_col='Column')
# print(schema_df.loc['MgrIdiot'])
# print(schema_df.loc['MgrIdiot', 'QuestionText'])

# # Sorting index:
# # --------------
# # schema_df.sort_index(inplace=True)
# print(schema_df)
# schema_df.sort_index(ascending=False, inplace=True)
# print(schema_df)
# schema_df.reset_index(inplace=True)
# print(schema_df)
# schema_df.set_index('Column', inplace=True)
# print(schema_df)


# ---------------------------------------------------------------------------------------------------------------------
# Filtering
# ---------------------------------------------------------------------------------------------------------------------
# Conditional Operators: & and; | or; ~ not
# isin(), str.contains(), isnull(), notnull()
# ---------------------------------------------------------------------------------------------------------------------
# df3 = pd.DataFrame(people)
# print(df3['last_name'] == 'L3')                     # Returns a boolean mask as a Series
# print(df3[df3['last_name'] == 'L3'])                # Method 1: Use the mask to filter specific rows
# ln_filter = (df3['last_name'] == 'L3')              # Assign the filter mask to a variable (parenthesis not needed)
# print(df3[ln_filter])                               # Method 2: Use the variable to filter specific rows
# print(df3.loc[ln_filter])                           # Method 3: Use variable with loc to filter - preferred method
# print(df3.loc[ln_filter, 'email'])                  # You can grab specific columns if you use method 3

# # Conditional Operators (& and; | or; ~ not)
# name_filter = (df3['last_name'] == 'L3') & (df3['first_name'] == 'F3')
# print(df3.loc[name_filter])
# print(df3.loc[~name_filter, 'email'])

# response_df = pd.read_csv('survey_results_public.csv', index_col='Respondent')
# schema_df = pd.read_csv('survey_results_schema.csv', index_col='Column')

# salary_filter = (response_df['ConvertedComp'] > 1_000_000)
# print(response_df.loc[salary_filter, ['Country', 'LanguageWorkedWith', 'ConvertedComp']])

# country_list = ['United States', 'India', 'United Kingdom', 'Germany', 'Canada']
# country_filter = response_df['Country'].isin(country_list)
# print(response_df.loc[country_filter, ['Country', 'LanguageWorkedWith', 'ConvertedComp']])

# country_filter_India = (response_df['Country'] == 'India') & (response_df['ConvertedComp'] > 0)
# print(response_df.loc[country_filter_India, ['Country', 'LanguageWorkedWith', 'ConvertedComp']])

# language_filter = response_df['LanguageWorkedWith'].str.contains('Python', na=False)        # na=False removes NaN
# print(response_df.loc[language_filter, ['Country', 'LanguageWorkedWith', 'ConvertedComp']])

# notnull_filter = response_df['LanguageWorkedWith'].notnull()
# print(response_df.loc[language_filter])


# ---------------------------------------------------------------------------------------------------------------------
# Updating Columns: rename()
# ---------------------------------------------------------------------------------------------------------------------
# df4 = pd.DataFrame(people)
# print(df4)
# print(df4.columns)                                      # Index(['first_name', 'last_name', 'email'], dtype='object')

# # Updating all column names:
# df4.columns = ['first', 'last', 'emailid']              # Rename columns names. Use when changing all columns names
# print(df4.columns)                                      # Index(['first', 'last', 'emailid'], dtype='object')

# df4.columns = [x.upper() for x in df4.columns]          # Change column names to upper case (use list comprehension)
# df4.columns = df4.columns.str.replace(' ', '_')         # Replace ' ' by '_' in column names
# df4.columns = [x.lower() for x in df4.columns]          # Change column names to lower case

# # Updating specific column names:
# df4.rename(columns={'first': 'first_name', 'last': 'last_name'}, inplace=True)
# print(df4.columns)                                      # Index(['first_name', 'last_name', 'emailid'], dtype='object')

# # Renaming index:
# df4.rename(index={0: '1st', 1: '2nd', 2: '3rd'}, inplace=True)
# print(df4)


# ---------------------------------------------------------------------------------------------------------------------
# Updating Rows:
# ---------------------------------------------------------------------------------------------------------------------
# df4 = pd.DataFrame(people)

# # Updating values of all columns in a row:
# df4.loc[2] = ['F4', 'L4', 'F4@email.com']

# # Updating values of specific columns in a row (using 'loc'):
# df4.loc[2, 'last_name'] = 'L40'
# df4.loc[2, ['first_name', 'email']] = ['F40', 'F40@email.com']

# # Updating values of specific columns in a row (using 'at'):
# df4.at[1, 'last_name'] = 'L20'
# df4.at[1, ['first_name', 'email']] = ['F20', 'F20@email.com']

# # Updating values of specific columns in a row (using filters):
# email_filter = df4['email'] == 'F1@email.com'
# df4.loc[email_filter, 'last_name'] = 'L10'

# # Updating values in multiple rows:
# df4['email'] = df4['email'].str.lower()


# ---------------------------------------------------------------------------------------------------------------------
# apply() on Series objects: applies a function to every value in the Series:
# ---------------------------------------------------------------------------------------------------------------------
# df5 = pd.DataFrame(people)

# # 1. apply a built-in function:
# print(df5['email'].apply(len))                        # applies len() to every value of 'email' column


# # 2. apply a custom function:
# def update_email(email):
#     return email.upper()

# df5['email'] = df5['email'].apply(update_email)
# print(df5)


# # 3. apply a lambda function
# df5['email'] = df5['email'].apply(lambda x: x.lower())
# print(df5)


# ---------------------------------------------------------------------------------------------------------------------
# apply() on DataFrame objects: applies a function to each Series (row or column) of the DataFrame:
# ---------------------------------------------------------------------------------------------------------------------
# df6 = pd.DataFrame(people1)
# print(df6.apply(len))                                   # applies len() to each series/column in the DataFrame
# print(df6.apply(len, axis='rows'))                      # same as above. axis='rows' is default
# print(df6.apply(len, axis='columns'))                   # applies len() to each row in the DataFrame

# print(df6.apply(pd.Series.min))                         # applies min() to each series/column in the DataFrame
# print(df6.apply(lambda x: x.max()))


# ---------------------------------------------------------------------------------------------------------------------
# applymap(): applies a function to every element of the DataFrame. Does not work on Series
# ---------------------------------------------------------------------------------------------------------------------
# df7 = pd.DataFrame(people)
# print(df7.applymap(len))                                # Returns a DataFrame with length of each element of the DF
# print(df7.applymap(str.lower))


# ---------------------------------------------------------------------------------------------------------------------
# map(): Used for substituting each value within a Series with another value (Works on Series not DataFrame)
# ---------------------------------------------------------------------------------------------------------------------
# # If you do not map every value, the ones not mapped will be mapped to NaN
# df7['first_name'] = df7['first_name'].map({'F1': 'A1', 'F2': 'A2'})
# print(df7)


# ---------------------------------------------------------------------------------------------------------------------
# replace():
# ---------------------------------------------------------------------------------------------------------------------
# # Will not replace unmapped values with Nan
# df7['last_name'] = df7['last_name'].map({'L1': 'X1', 'L2': 'X2'})
# print(df7)


# ---------------------------------------------------------------------------------------------------------------------
# response_df = pd.read_csv('survey_results_public.csv', index_col='Respondent')
# schema_df = pd.read_csv('survey_results_schema.csv', index_col='Column')

# response_df.rename(columns={'ConvertedComp': 'Salary_USD'}, inplace=True)
# print(response_df.columns)

# response_df['Hobbyist'] = response_df['Hobbyist'].map({'Yes': True, 'No': False})
# print(response_df['Hobbyist'])
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# Adding/Removing Columns:
# ---------------------------------------------------------------------------------------------------------------------
# df8 = pd.DataFrame(people)
# df8['full_name'] = df8['first_name'] + ' ' + df8['last_name']
# df8['salary'] = [75_000, 100_000, 80_000]
# print(df8)

# df8.drop(columns=['first_name', 'last_name'], inplace=True)
# print(df8)

# # split full_name column into two new columns
# # str.split() returns a list. expand=True will expand the list into two different columns
# df8[['first_name', 'last_name']] = df8['full_name'].str.split(' ', expand=True)
# print(df8)


# ---------------------------------------------------------------------------------------------------------------------
# Adding/Removing Rows:
# ---------------------------------------------------------------------------------------------------------------------
# df8 = pd.DataFrame(people)
# df9 = pd.DataFrame(people1)

# # Adding a single row (Values not supplied will default to NaN):
# df8 = df8.append({'first_name': 'A1'}, ignore_index=True)
# print(df8)

# # Append a DataFrame (sort=False prevents future warning):
# df8 = df8.append(df9, ignore_index=True, sort=False)
# print(df8)

# # Dropping rows (using Index):
# df8.drop(index=3, inplace=True)
# print(df8)

# # Dropping rows (that has NaN):
# df8.dropna(inplace=True)
# print(df8)

# # Dropping rows (using filters):
# salary_filter = (df8['salary'] == 75_000)
# df8.drop(index=df8[salary_filter].index, inplace=True)
# print(df8)


# ---------------------------------------------------------------------------------------------------------------------
# Sorting Data:
# ---------------------------------------------------------------------------------------------------------------------
# df10 = pd.DataFrame(people1)

# # Sorting values (Series):
# print(df10['salary'].sort_values())

# # Sorting values (Data Frame):
# df10.sort_values(by='salary', inplace=True)
# print(df10)
# df10.sort_values(by='salary', ascending=False, inplace=True)
# print(df10)
# df10.sort_values(by=['salary', 'last_name'], ascending=[False, True], inplace=True)
# print(df10)

# # Sorting index:
# df10.sort_index(inplace=True)                               # reverts back the sort
# print(df10)

# ---------------------------------------------------------------------------------------------------------------------
# response_df = pd.read_csv('survey_results_public.csv', index_col='Respondent')
# schema_df = pd.read_csv('survey_results_schema.csv', index_col='Column')

# response_df.sort_values(['Country', 'ConvertedComp'], ascending=[True, False], inplace=True)
# print(response_df[['Country', 'ConvertedComp']].head(50))

# # Find the top 10 highest salaries:
# print(response_df['ConvertedComp'].nlargest(10))
# print(response_df.nlargest(10, 'ConvertedComp'))

# # Find the top 10 lowest salaries:
# print(response_df['ConvertedComp'].nsmallest(10))
# print(response_df.nsmallest(10, 'ConvertedComp'))
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# Aggregating Data:
# ---------------------------------------------------------------------------------------------------------------------
# response_df = pd.read_csv('survey_results_public.csv', index_col='Respondent')
# schema_df = pd.read_csv('survey_results_schema.csv', index_col='Column')

# # Aggregation functions on a column (Series) - NaNs are ignored:
# print('Median Salary:', response_df['ConvertedComp'].median())
# print('Salary Count:', response_df['ConvertedComp'].count())
# print('Mean Salary:', response_df['ConvertedComp'].mean())
# print('STD of Salary:', response_df['ConvertedComp'].std())
# print('Min Salary:', response_df['ConvertedComp'].min())
# print('Max Salary:', response_df['ConvertedComp'].max())

# # Aggregation functions on the DataFrame - Returned for numeric cols (except count()):
# print('Median: \n', response_df.median())
# print('Count: \n', response_df.count())
# print('STD: \n', response_df.std())
# print('Min: \n', response_df.min())
# print('Max: \n', response_df.max())
# print('Mean: \n', response_df.mean())

# # Statistical description (aggregation) of a column (Series):
# print(response_df['ConvertedComp'].describe())

# # Statistical description (aggregation) of the DataFrame:
# print(response_df.describe())


# ---------------------------------------------------------------------------------------------------------------------
# unique():
# ---------------------------------------------------------------------------------------------------------------------
# print(response_df['Country'].unique())


# ---------------------------------------------------------------------------------------------------------------------
# value_count(): a list of unique values and how often they occur (Group-by)
# ---------------------------------------------------------------------------------------------------------------------
# print(response_df['Hobbyist'].value_counts())
# print(schema_df.loc['SocialMedia'])
# print(response_df['SocialMedia'].value_counts())
# print(response_df['SocialMedia'].value_counts(normalize=True))              # Grouped by percentage
# print(response_df['Country'].value_counts())


# ---------------------------------------------------------------------------------------------------------------------
# Grouping Data: (1. Split the object, 2. Apply a function, 3. Combine the results)
# ---------------------------------------------------------------------------------------------------------------------
# response_df = pd.read_csv('survey_results_public.csv', index_col='Respondent')
# schema_df = pd.read_csv('survey_results_schema.csv', index_col='Column')

# # 1. Split the object (by Country column):
# # ----------------------------------------
# df.groupby() returns a DataFrameGroupBy object
# This object has multiple groups of data (in this case, groups of data grouped by countries)
# country_grp = response_df.groupby(['Country'])
# print(country_grp)
# print(country_grp.get_group('United States'))

# # Group by 'Country':
# print(response_df.groupby('Country').Country.count())
# # Average salary per country:
# print(response_df.groupby('Country').ConvertedComp.mean())


# # 2. Apply a function:
# # --------------------
# # Get the most popular social media by country
# # Returns a Series with two indices (Country and SocialMedia)
# print(country_grp['SocialMedia'].value_counts().head(50))
# print(country_grp['SocialMedia'].value_counts().loc['India'])
# print(country_grp['SocialMedia'].value_counts(normalize=True).loc['China'])


# # 3. Combine the results:
# # -----------------------
# # Median salaries by country
# print(country_grp['ConvertedComp'].median())
# print(country_grp['ConvertedComp'].median().loc['Germany'])                # Country is index, can be used with loc
# print(country_grp['ConvertedComp'].agg(['median', 'mean', 'max']))         # pass multiple aggregate functions
# print(country_grp['ConvertedComp'].agg(['median', 'mean', 'max']).loc[['India', 'United States']])

# # Number of people that use Python by country:
# # country_grp['LanguageWorkedWith'] returns a SeriesGroupBy object (not a Series) and str() is not its attribute
# print(country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum()))


# ---------------------------------------------------------------------------------------------------------------------
# Multi-Indexes:
# ---------------------------------------------------------------------------------------------------------------------
# # A multi-index differs from a regular index in that it has multiple levels.
# country_grp = response_df.groupby(['Country', 'LanguageWorkedWith'])

# # Converting multi-index back to a regular index:
# country_grp.reset_index()


# ---------------------------------------------------------------------------------------------------------------------
# Number of people that use Python by country including percentage:
# ---------------------------------------------------------------------------------------------------------------------
# response_df = pd.read_csv('survey_results_public.csv', index_col='Respondent')
# country_grp = response_df.groupby(['Country'])

# # Get total number of respondents from each country:
# country_respondents = response_df['Country'].value_counts()

# # Get total number of respondents that know Python:
# country_uses_python = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())

# # Create a new DF:
# python_df = pd.concat([country_respondents, country_uses_python], axis='columns', sort=False)

# # Rename the columns:
# python_df.rename(columns={'Country': 'NumRespondents', 'LanguageWorkedWith': 'NumKnowsPython'}, inplace=True)

# # Add percent column:
# python_df['PctKnowsPython'] = python_df['NumKnowsPython']/python_df['NumRespondents'] * 100

# # Sort by percentage:
# python_df.sort_values(by='PctKnowsPython', ascending=False, inplace=True)
# print(python_df.head(50))
# print(python_df.loc[['India', 'United States', 'Canada']])


# ---------------------------------------------------------------------------------------------------------------------
# Cleaning Data:
# ---------------------------------------------------------------------------------------------------------------------

people2 = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'],
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'],
    'email': ['CMS@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}

# df11 = pd.DataFrame(people2)
# print(df11)

# df11.dropna(inplace=True)
# print(df11)

# # axis='index': drops rows, how='any': drops row if any value is missing (Default arguments)
# df11.dropna(axis='index', how='any', inplace=True)
# print(df11)

# # axis='index': drops rows, how='all': drops row if all values are missing
# df11.dropna(axis='index', how='all', inplace=True)
# print(df11)

# # axis='columns': drops columns, how='any': drops column if any value is missing
# df11.dropna(axis='columns', how='any', inplace=True)
# print(df11)

# # axis='columns': drops columns, how='all': drops column if all values are missing
# df11.dropna(axis='columns', how='all', inplace=True)
# print(df11)
