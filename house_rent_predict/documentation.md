# house_rent_predict Documentation

## Overview
The `house_rent_predict` project is designed to predict house rental prices based on the area of the property. It leverages a linear regression model from the `scikit-learn` library to estimate rental prices using a provided dataset.

## Requirements
- Python 3.x
- Pandas
- scikit-learn

## Installation
To get started, ensure you have the required libraries installed. If not, you can install them using pip:

```bash
pip install pandas scikit-learn
```

## Dataset
The model uses a simple dataset to train the linear regression model:

```python
data = {
    'Area': [1000, 1500, 2000, 2500, 3000],
    'price': [20000, 30000, 40000, 50000, 60000]
}
```

This dataset contains two features:
- `Area`: The area of the property in square feet.
- `price`: The corresponding rental price in Tk.

## Data Preparation
The dataset is loaded into a Pandas DataFrame for easy manipulation and preview:
```python
df = pd.DataFrame(data)
print('Data Preview:')
print(df.head())
```

## Model Training
The `LinearRegression` model from `scikit-learn` is used:
1. Features (`X`) are extracted: Areas.
2. Targets (`Y`) are extracted: Prices.

```python
X = df[['Area']]
Y = df['price']

model = LinearRegression()
model.fit(X, Y)
```

## User Input
The program requires user input for the area of the property:
```python
Area = float(input('Enter Area:'))
```

## Prediction
The model predicts the rental price based on the input area:
```python
predicted_price = model.predict([[Area]])
```

## Output
The predicted rental price is displayed in the following format:
```python
print(f'Predicted Price: TK {predicted_price[0]:,.2f}')
```

This will output the predicted price with a Tk prefix and formatted to two decimal places.

## Usage
1. Run the script.
2. Enter the area of the property when prompted.
3. View the predicted rental price.

This project provides a basic introduction to using linear regression for predictive analytics in housing prices. Adjust the sample data to fit real-world scenarios for more accurate predictions.