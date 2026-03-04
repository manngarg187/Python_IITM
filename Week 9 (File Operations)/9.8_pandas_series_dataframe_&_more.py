import pandas as pd
scores = pd.read_csv('cereal.csv')
print(scores)   # This will print all the data in scores.csv in a tabular form and this is entire table is referred as Dataframe and a specific column within this table or dataframe is referred as Pandas Series.
print(type(scores))
print(scores['name'], type(scores['name']))   # type(scores['name']) will give 'series' as a outpue

# Dataframe is a 2- dimentional data structure which is used to store a tabular data.
# Any specific coulumn from the dataframe is referred as series in Pandas. Series is a 1-dimentional entity

print(scores.head())  # this will only print top 5 rows from the dataframe
print(scores.tail())  # this will only print last 5 rows from the dataframe
print(scores[scores['name'] == 'Almond Delight'])   # This code will help us to get the complete information of a particular row. Technically we read this code line as 'Access the dataframe name as scores, but make sure, within that data frames name series, the value should be 'Almond Delight' 