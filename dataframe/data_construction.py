import pandas as pd

d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}

df = pd.DataFrame(data=d)

print(df)

import pandas as pd

health_data = pd.read_csv("D:\VScode\dataframe\data.txt", header=0, sep=",")

print(health_data)

#Data cleaning
health_data.dropna(axis=0,inplace=True)

print(health_data)


#data types
print(health_data.info())

#data head
print(health_data.head())# only head shows 5 data

#describe
print(health_data.describe())


#data_plotting
import matplotlib.pyplot as plt


health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='line', bar= True),


plt.show()

