import pandas as pd2
import os

import matplotlib.pyplot as plt
import seaborn as sns
#%config InlineBackend.figure_format='retina'
#%config InlineBackend.

#fileJobs="\Jobs_data.csv"
fileJobs="\w3data.csv"
path=os.getcwd()+fileJobs
df=pd2.read_csv(path)
pd2.set_option("display.precision",2)
#print(df)
#print(df.head(10))
# print(df.info)
#print(df.columns)
#print(df.iloc[10:100,3:9])
df1=df.sort_values(by='Calories',ascending=False)
#print(df1['Calories'].mean())
#df.groupby(by=grouping_columns)[columns_to_show].function()
#print(df1.groupby(by='Duration')[['Pulse']].mean())
#print(df1.groupby(by='Duration')[['Pulse']].count())
# print(df1.groupby(by='Duration')[['Pulse']].max())
# print(df1.groupby(by='Duration')[['Pulse']].min())


#matplotlib
#plt.plot(df['Duration'],df['Maxpulse'])
#plt.show()

#sns.countplot(x="Pulse",hue='MaxPulse', date=df
# g=sns.FacetGrid(df)
# g.map(sns.histplot,'Pulse')
# plt.show()

