# main.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima.model import ARIMA
from scipy import stats
import numpy as np

# STEP 1: LOAD & CLEAN DATA
df = pd.read_csv('data.csv', encoding='ISO-8859-1')

# Clean and prep data
df.dropna(subset=['CustomerID'], inplace=True) # Handle missing data by filling or dropping missing values
df = df[df['Quantity'] > 0] # Remove rows where Quantity is <= 0 (no valid sales)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate']) # Convert 'InvoiceDate' to datetime

#STEP 2: FEATURE ENGINEERING

# Create 'Revenue' column
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Extract Month and Year from InvoiceDate
df['Month'] = df['InvoiceDate'].dt.month
df['Year'] = df['InvoiceDate'].dt.year

#STEP 3: DATA EXPLORATION

# Check for outliers in 'UnitPrice' and 'Quantity'
df['UnitPrice'].describe()
df['Quantity'].describe()

# Filter out outliers for both Quantity and UnitPrice
df_filtered = df[df['Quantity'] < df['Quantity'].quantile(0.99)]  # Filter Quantity
df_filtered = df_filtered[df_filtered['Quantity'] > df['Quantity'].quantile(0.01)]  # Filter lower outliers for Quantity

df_filtered = df_filtered[df_filtered['UnitPrice'] < df_filtered['UnitPrice'].quantile(0.99)]  # Filter UnitPrice
df_filtered = df_filtered[df_filtered['UnitPrice'] > df_filtered['UnitPrice'].quantile(0.01)]  # Filter lower outliers for UnitPrice


# Check for outliers in 'UnitPrice' and 'Quantity'
df_filtered['UnitPrice'].describe()
df_filtered['Quantity'].describe()

# Create 'Revenue' column based on filtered data
df_filtered['Revenue'] = df_filtered['Quantity'] * df_filtered['UnitPrice'] 

# Check for outliers in 'Revenue'
df_filtered['Revenue'].describe()

# Plot distribution of UnitPrice and Quantity
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
df_filtered['UnitPrice'].hist(bins=50, color='skyblue', edgecolor='black')
plt.title('Distribution of UnitPrice')

plt.subplot(1, 2, 2)
df_filtered['Quantity'].hist(bins=50, color='lightcoral', edgecolor='black')
plt.title('Distribution of Quantity')
plt.tight_layout()
plt.show()

# Plot revenue trends over time (by month and year)
monthly_revenue = df_filtered.groupby(['Year', 'Month'])['Revenue'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(monthly_revenue['Revenue'], marker='o', linestyle='-', color='b')
plt.title('Monthly Revenue Over Time')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.show()

#STEP 4: PRICING OPTIMIZATION THROUGH REGRESSION

from sklearn.preprocessing import PolynomialFeatures, StandardScaler

# Define Features (UnitPrice) and Target (Quantity sold)
X = df_filtered['UnitPrice'].values.reshape(-1, 1)  # Independent variable
y = df_filtered['Quantity'].values  # Dependent variable (Sales Volume)

# Apply Polynomial Features (Degree 3 for Non-Linear Effects)
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

# Scale Data for Regression
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_poly)

# Train Polynomial Regression Model
model = LinearRegression()
model.fit(X_scaled, y)

# Generate Predictions for Different Prices
price_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
price_range_poly = poly.transform(price_range)
price_range_scaled = scaler.transform(price_range_poly)
predicted_quantity = model.predict(price_range_scaled)

# Plot Results
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='lightblue', label='Actual Sales Data')
plt.plot(price_range, predicted_quantity, color='red', linewidth=2, label='Predicted Sales Volume')
plt.fill_between(price_range.flatten(), confidence_intervals[:, 0], confidence_intervals[:, 1], color='gray', alpha=0.3, label='Confidence Interval') #Confidence Interval Shading
plt.title('Price Optimization: Impact of Price on Sales Volume')
plt.xlabel('Unit Price')
plt.ylabel('Quantity Sold')
plt.legend()
plt.show()

#STEP 5: TIME SERIES FORECASTING

from prophet import Prophet 

# Aggregate revenue by month on filtered data
df_monthly_filtered = df_filtered.groupby(['Year', 'Month'])['Revenue'].sum().reset_index()

# Prepare Prophet-compatible dataset
df_prophet_filtered = df_monthly_filtered[['Year', 'Month', 'Revenue']].copy()
df_prophet_filtered['ds'] = pd.to_datetime(df_prophet_filtered[['Year', 'Month']].assign(day=1))
df_prophet_filtered.rename(columns={'Revenue': 'y'}, inplace=True)  # Prophet expects column 'y' as target

# Initialize and train Prophet model (handles seasonality)
model = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
model.fit(df_prophet_filtered)

# Create future dataframe for 12-month forecasting
future = model.make_future_dataframe(periods=12, freq='M')
future['Year'] = future['ds'].dt.year
future['Month'] = future['ds'].dt.month  # Ensure future dates align with dataset format

# Generate predictions
forecast = model.predict(future)

# Filter forecast to only include future data (exclude historical data)
forecast_future = forecast[forecast['ds'] > df_prophet_filtered['ds'].max()]

# Verify forecast output
print(forecast_future[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())  # Ensure forecast only includes future data

# Enhanced plot with manual visualization (Only forecasted data)
plt.figure(figsize=(10, 6))
plt.plot(forecast_future['ds'], forecast_future['yhat'], label='Forecasted Revenue', color='orange', linewidth=2)
plt.fill_between(forecast_future['ds'], forecast_future['yhat_lower'], forecast_future['yhat_upper'], color='gray', alpha=0.3, label='Confidence Interval')
plt.title('Revenue Forecast for Next Year (Filtered Data)')
plt.xlabel('Month')
plt.ylabel('Projected Revenue')
plt.legend()
plt.show()
