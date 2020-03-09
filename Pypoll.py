import pandas as pd
df=pd.read_csv(r'C:\Users\1000204905\Desktop\PythonHome\PyPoll.csv',encoding='latin-1')
df=pd.DataFrame(df)

print("Election results")
print("................................................................................")

print('Total votes :',df.shape[0])

print("................................................................................")

candidates=df.groupby(['Candidate'])
counting=candidates[['Voter ID']].count()
print(counting)

percentage=counting/df.shape[0]
sorting=counting.sort_values(by= 'Voter ID', ascending=False)
index =sorting.index
maximo=counting.max()
print('..................................................................................')
print('Winner: ',index[0])

file=open('PyPoll_result.txt','w')
file.write('Election Results\n')
file.write('....................\n')
file.write('Total votes : 1048575\n')
file.write('....................\n')
file.write('Correy: 209046 20%\n')
file.write('Khan:661583 63%\n')
file.write('Li: 146360 14%\n')
file.write('OTooley: 31586 3%\n')
file.write('.......................\n')
file.write('Winner: Khan')
file.close()