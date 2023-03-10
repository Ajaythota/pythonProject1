import pandas as pd1
import os

filecsv="\w3data.csv"
filexl="\w3excel.xlsx"
fileJsn="\data.js"
path=os.getcwd()+filecsv
df_c=pd1.read_csv(path)
#print(df_c.to_string())

path=os.getcwd()+filexl
df_e=pd1.read_excel(path)

path=os.getcwd()+fileJsn
df_j=pd1.read_json(path)

data=[df_e,df_c,df_j]
df=pd1.concat(data,ignore_index=True,sort=False)
print(type(df))
#print(pd1.isnull)
print(df)
#iloc-  location (rows and column as input)
# print(df.iloc[1,2])
# print(df.iloc[[4,1],[2,3]])
# print(df.iloc[:,2])
# print(df.iloc[3,:])
# print(df.iloc[3:15,1:3])
# print(df.head(10))

#loc - label (rows and column as input)
# print(df.loc[1,'Maxpulse'])
# print(df.loc[:,['Maxpulse','Calories']])
# print(df.loc[:,'Duration':'Maxpulse'])
# print(df.loc['100':'150','Duration':'Maxpulse'])