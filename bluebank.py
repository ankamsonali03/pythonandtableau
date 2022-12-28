import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
#transform to dataframe
loandata = pd.DataFrame(data)

#finding unique values for Purpose column

loandata['purpose'].unique()
loandata.describe()

#describe data by specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annual_income'] = income

length = len(loandata)
ficocat = []
for x in range(0, length):
    category = loandata['fico'][x]
    
    try:        
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'    
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
            cat = 'Unknown'
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat

    
#df.loc as conditional statement
#df.loc[df[column_name] condition, newcolumn_name] = 'value if condition is met'

#for interest rates a new column is wanted. rate > 0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#number of loans or rows by fico category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'blue', width = 0.5)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'green', width = 0.5)
plt.show()

#scatterplots 

ypoint = loandata['annual_income']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = 'green')
plt.show()

#writing to csv
loandata.to_csv('Loan_Cleaned.csv', index = True)