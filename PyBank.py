import pandas as pd

df=pd.read_csv(r'C:\Users\1000204905\Desktop\PythonHome\PyBank.csv',encoding='latin-1')
print("Financial analysis")
print("................................................................................")
 
total_months = df.shape[0]
tot_su = df['Profit/Losses'].sum()

#Greatest increase change
difference_change = pd.Series(df['Profit/Losses'])
difference =difference_change.diff()
df['Difference']=difference
df =  df.drop('Unnamed: 2', 1)
df =  df.drop('Unnamed: 3', 1)

print('Total months :',total_months)
print('Total: $',tot_su)
print('Average Change:',df.Difference.mean())
print('Greatest Increase in Profits:',df.Difference.max())
print('Greatest Decrease in Profits:',df.Difference.min())