# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

#file_name pd.read_csv('file.csv') <---- format of read csv
data=pd.read_csv('transaction.csv')

data=pd.read_csv('transaction.csv',sep=';')

#summary of data
data.info()

#working with calculations

#ProfitPerItem=SellingPricePerItem-CostPerItem

#ProfitPerTransaction=NumberOfItemsPurchased*ProfitPerItem
#CostPerTransaction=NumberOfItemsPurchased*CostPerItem
#SellingPricePerTransaction=NumberOfItemsPurchased*SellingPricePerItem

#CostPerTransaction Column Calculation

#CostPerTransaction= NumberOfItemsPurchased * CostPerItem
#variable=dataframe['column_name']

CostPerItem=data['CostPerItem']

NumberOfItemsPurchased=data['NumberOfItemsPurchased']

CostPerTransaction= NumberOfItemsPurchased * CostPerItem

# adding a new column to a dataframe

data['CostPerTransaction']=CostPerTransaction

#Sales Per Transaction

data['SalesPerTransaction']=data['SellingPricePerItem']*data['NumberOfItemsPurchased']

#Profit Calculations= sales-cost ===profit/cost

data['ProfitPerTransaction']=data['SalesPerTransaction']-data['CostPerTransaction']


#Markup Calculation= (sales-Cost)/cost

data['Markup']= (data['SalesPerTransaction']-data['CostPerTransaction'])/data['CostPerTransaction']

#Rounding Marking
roundmarkup=round(data['Markup'],2)

data['Markup']=round(data['Markup'],2)

#chamge column type

day=data['Day'].astype(str)
print(day.dtype)


year=data['Year'].astype(str)
print(year.dtype)
data.info()

data['my_date']=day+'-'+data['Month']+'-'+year

#new_var=column.str.split('sep',expand=True) 

split_col=data['ClientKeywords'].str.split(',',expand=True)

data['ClientAge']=split_col[0]

data['ClientType']=split_col[1]

data['LengthOfContract']=split_col[2]

#replace function
data['ClientAge']=data['ClientAge'].str.replace('[','')

data['LengthOfContract']=data['LengthOfContract'].str.replace(']','')

#lower function

data['ItemDescription']=data['ItemDescription'].str.lower()

#how to merge files # bringing new dataset

seasons=pd.read_csv('value_inc_seasons.csv',sep=';')

data=pd.merge(data,seasons,on='Month')

#droping columns

data=data.drop('ClientKeywords',axis=1)
data=data.drop('Day',axis=1)
data=data.drop('Year',axis=1)
data=data.drop('Month',axis=1)

#export into csv

data.to_csv('ValueInc_Cleaned.csv', index=False)  
