import pandas as pd
import numpy as np


# Data setup
data = {
    'area': [1000, 800, 1200, 1500, 900, 1100],
    'bedrooms': [2, 2, 3, 3, 2, 3],
    'rent': [10000, 12000, 18000, 22000, 13000, 17000]
}
df = pd.DataFrame(data)

# Prepare features and target
X = df[['area', 'bedrooms']].values
y = df['rent'].values

# Standardize features
X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

# Add intercept term
X = np.hstack((np.ones((X.shape[0], 1)), X))

# Initialize parameters for gradient descent
theta = np.zeros(X.shape[1])
alpha = 0.01
iterations = 1000

# Gradient Descent Function
def gradient_descent(X, y, theta, alpha, iterations):
    m = len(y)
    for _ in range(iterations):
        prediction = X @ theta
        error = prediction - y
        theta -= (alpha / m) * (X.T @ error)
    return theta

# Train the model
theta = gradient_descent(X, y, theta, alpha, iterations)
print("Learned coefficients:", theta)

# Prediction function
def predict(X, theta):
    return X @ theta

# Take user input and predict
area = float(input("Enter the area: "))
bedrooms = int(input("Enter the number of bedrooms: "))

# Standardize input using the training data mean and std
area_std = (area - np.mean(df['area'])) / np.std(df['area'])
bedrooms_std = (bedrooms - np.mean(df['bedrooms'])) / np.std(df['bedrooms'])

# Create feature array for prediction
user_input = np.array([1, area_std, bedrooms_std])

# Predict rent
predicted_rent = predict(user_input, theta)
print(f"Predicted Rent: {predicted_rent:.2f}")

