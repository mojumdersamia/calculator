import pandas as pd
from sklearn.linear_model import LinearRegression

# Step 1: Read data from a CSV file
df = pd.read_csv("D:\New folder\house rent with database\data.csv")

# Step 2: Preview the data
print('Data Preview:')
print(df.head())

# Step 3: Define features (independent variable) and target (dependent variable)
X = df[['sqft_living']]  
Y = df['price']          

# Step 4: Create and train the Linear Regression model
model = LinearRegression()
model.fit(X, Y)

# Step 5: Get user input for square footage
sqft_living = float(input('Enter Square Footage (sqft_living): '))

# Step 6: Predict the price based on user input
predicted_price = model.predict([[sqft_living]])

# Step 7: Output the predicted price
print(f'Predicted Price: TK {predicted_price[0]:,.2f}')