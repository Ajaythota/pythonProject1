#pandas- panel data

import pandas as pd
#print(dir(pd))

#Series- A Pandas Series is like a column in a table.
#print(help(pd.core.series))

# s1=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])    #list
# print(s1)
# print(s1['a'])
# print(s1[1:4])
# print(s1[::-1])
# emp={'name':['john','Eric','Sam'],'dept':['IT','Acct','HR'],'salary':[111,222,333]}  #Dictionary
# res=pd.Series(data=emp)
# print(res)
# res['age']=[30,40,25]
# print(res)



#DataFrame-A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
# list1=[1,2,3,9] #list
# df0=pd.DataFrame(list1,columns=['First'])
# df0['second']=[4,5,6,7]
# print(df0)

# df=pd.DataFrame(data=emp)  #Dictionary
# print(df)
#append /concat dataframes
grp1={'name':['John','Eric','Sam'],'dept':['IT','Acct','HR'],'salary':[111,222,333]}
df1=pd.DataFrame(data=grp1)
grp2={'name':['Jai','Ravi','Shyam'],'dept':['IT','Acct','HR'],'salary':[444,555,666]}
df2=pd.DataFrame(data=grp2)
grp3={'name':['Jai','Ravi','Shyam'],'dept':['IT','Acct','HR'],'salary':[444,555,666]}
df3=pd.DataFrame(data=grp3)

# print(df1)
# print(df2)
# Using pandas.concat() Method
data=[df1,df2,df3]
DF=pd.concat(data,ignore_index=True,sort=False)
print(DF)

#,'25''65','17','5','43','50'
#44444,5555,6666,7777,8888,9999

#  Using pandas.concat() to INNER join to concat two DataFrames
import pandas as pd1
grp4={'Hike(%)':['10','10','15','25','65','17','5','43','50'],'new salary':[111,222,333,44444,5555,6666,7777,8888,9999]}
df4=pd1.DataFrame(data=grp4)
print(df4)
print(DF)
data1=[DF,df4]
DF1=pd.concat(data1,axis=1,join='inner',ignore_index=True,sort=False)
print(DF1)