#import modules
import csv
import pandas as pd

#source of data is basketball-reference.com located "http://www.basketball-reference.com/playoffs/series.html"
#open csv file and read to dataframe
df = pd.read_csv('NBA Playoffs data.csv', sep=',',skiprows = 1 ) #skip first row to get appropriate column headers
#print df
#remove all unnamed columns
for col in df.columns:
    if 'Unnamed' in col:
        del df[col]
#remove league column
del df['Lg']

df2 = df[df.Series =='Finals'] #get only finals games

df3 = df2[['Yr','Team','W','Team.1','W.1']] #get only necessary columns
df3['Total_Games'] = df3['W'] + df3['W.1'] #create a new column showing total games played in each series
df3.index = range (0,76,1) #reset index

for i in range(4,8):
    no_of_games = float(df3[df3.Total_Games ==i]['Total_Games'].size)/76.
    print "Percent of %i-game NBA finals series: "%(i)+'{percent:.1%}'.format(percent = no_of_games)
