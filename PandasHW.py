import pandas as pd3
import os

path=os.getcwd()+"\Pandas\Automobile_data.csv"

df=pd3.read_csv(path)
print(df)
#: From given data set print first and last five rows
# print(df.head())
#print(df.tail())

# Find the most expensive car company name
pMax=df['price'].max()
print(pMax)
print(df[df['price']==pMax]['company'])

#Print All Toyota Cars details
print(df[df['company']=='toyota'])

#Count total cars per company
print(df.groupby(by='company')[['company']].count())

#Find each company’s Higesht price car
print(df.groupby(by='company')[['price']].max())

#Find the average mileage of each car making company
print(df.groupby(by='company')[['average-mileage']].mean())

#Sort all cars by Price column
print(df.sort_values('price'))