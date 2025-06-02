import pandas as pd
from sklearn.linear_model import LinearRegression

# sample data 
data = {
    'Area': [1000,1500,2000,2500,3000],
    'price': [20000,30000,40000,50000,60000]
}

df = pd.DataFrame(data)
print('Data Preview:')
print(df.head())

X= df[['Area']]
Y= df['price']

model = LinearRegression()
model.fit(X,Y)


#user input
Area =  float(input('Enter Area:'))

#predict
predicted_price = model.predict([[Area]]) 

#output
print(f'Predicted Price: TK {predicted_price[0]:,.2f}')
#  
# 