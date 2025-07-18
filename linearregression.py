# -*- coding: utf-8 -*-
"""LinearRegression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iLQarz3WPqs5V9vVI0lqhxL-guCkQStN
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

def analyze_regressions():
  try:
    boston = pd.read_csv("/content/sample_data/BostonHousing.csv")
    auto = pd.read_csv("/content/sample_data/auto-mpg.csv")

    X_boston = boston[['rm']]
    y_boston = boston['medv']

    auto = auto.replace('?', np.nan).dropna()
    auto['horsepower'] = auto['horsepower'].astype(float)
    X_auto = auto[['horsepower']]
    y_auto = auto['mpg']

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    X_train_boston, X_test_boston, y_train_boston, y_test_boston = train_test_split(
      X_boston, y_boston, test_size=0.2, random_state=42)

    model_boston = LinearRegression()
    model_boston.fit(X_train_boston, y_train_boston)
    y_pred_boston = model_boston.predict(X_test_boston)

    mse_boston = mean_squared_error(y_test_boston, y_pred_boston)
    r2_boston = r2_score(y_test_boston, y_pred_boston)

    X_test_boston_vals = X_test_boston['rm'].values
    y_test_boston_vals = y_test_boston.values
    y_pred_boston_vals = y_pred_boston

    sorted_indices = np.argsort(X_test_boston_vals)
    X_sorted = X_test_boston_vals[sorted_indices]
    y_pred_sorted = y_pred_boston_vals[sorted_indices]

    plt.scatter(X_test_boston_vals, y_test_boston_vals, color='blue', alpha=0.5, label='Actual Values')
    plt.plot(X_sorted, y_pred_sorted, color='red', label='Regression Line')

    plt.title('Boston Housing: Linear Regression')
    plt.xlabel('Average Number of Rooms')
    plt.ylabel('House Price ($1000s)')
    plt.legend()
    plt.text(0.05, 0.95, f'MSE: {mse_boston:.2f}\nR²: {r2_boston:.2f}',
        transform=plt.gca().transAxes,
        bbox=dict(facecolor='white', alpha=0.8))

    plt.subplot(1, 2, 2)
    poly_features = PolynomialFeatures(degree=2)
    X_poly = poly_features.fit_transform(X_auto)

    X_train_auto, X_test_auto, y_train_auto, y_test_auto = train_test_split(
      X_poly, y_auto, test_size=0.2, random_state=42)

    model_auto = LinearRegression()
    model_auto.fit(X_train_auto, y_train_auto)
    y_pred_auto = model_auto.predict(X_test_auto)

    mse_auto = mean_squared_error(y_test_auto, y_pred_auto)
    r2_auto = r2_score(y_test_auto, y_pred_auto)

    X_sort = np.sort(X_auto.values, axis=0)
    X_sort_df = pd.DataFrame(X_sort, columns=['horsepower']) # FIXED: keep feature name
    X_poly_sort = poly_features.transform(X_sort_df)
    y_smooth = model_auto.predict(X_poly_sort)

    plt.scatter(X_auto.values.flatten(), y_auto.values, color='blue', alpha=0.5, label='Actual Data')
    plt.plot(X_sort.flatten(), y_smooth, color='red', label='Polynomial (degree=2)')

    plt.title('Auto MPG: Polynomial Regression (degree=2)')
    plt.xlabel('Horsepower')
    plt.ylabel('Miles Per Gallon')
    plt.legend()
    plt.text(0.05, 0.95, f'MSE: {mse_auto:.2f}\nR²: {r2_auto:.2f}',
        transform=plt.gca().transAxes,
        bbox=dict(facecolor='white', alpha=0.8))

    plt.tight_layout()
    plt.show()

    print("\nRegression Analysis Results:")
    print("Boston Housing Linear Regression:")
    print(f"Mean Squared Error: {mse_boston:.2f}")
    print(f"R square Score: {r2_boston:.2f}")
    print("\nAuto MPG Polynomial Regression (degree=2):")
    print(f"Mean Squared Error: {mse_auto:.2f}")
    print(f"R square Score: {r2_auto:.2f}")

  except Exception as e:
    print(f"Error in analysis: {str(e)}")

if __name__ == "__main__":
  print("Starting Regression Analysis...")
  analyze_regressions()

