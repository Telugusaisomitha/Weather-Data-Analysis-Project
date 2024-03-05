# -*- coding: utf-8 -*-
"""weather data analysis.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y2HYQQzwpif3VE8Z8hLNG4RhvLjnOzeM

#Weather Data Analysis

**Importing Libraries**
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

"""**Load the dataset**"""

Weather_data = pd.read_csv("/content/weather[1].csv")
Weather_data

"""**Data Exploration**"""

#Headings
Weather_data.head()

#last rows
Weather_data.tail()

#Shape
Weather_data.shape

#Describe
Weather_data.describe()

#Display
display(Weather_data)

#info
Weather_data.info()

"""**Data Visualization**"""

#Pairplot using Seaborn

sns.pairplot(Weather_data[['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine']])

"""**Feature Engineering**"""

#Analysing hot day

Weather_data['HotDay'] = Weather_data['MaxTemp'] > 30
Weather_data['HotDay']

"""**Data Analysis**"""

#Analyse MinTemp

average_MinTemp = Weather_data['MinTemp'].mean()
MinTemp_std_dev = Weather_data['MinTemp'].std()

print("MinTemp Analysis:")
print("Average MinTemp:", average_MinTemp)
print("MinTemp Standard Deviation:", MinTemp_std_dev)

#Analyse MinTemp

average_MaxTemp = Weather_data['MaxTemp'].mean()
MaxTemp_std_dev = Weather_data['MaxTemp'].std()

print("MaxTemp Analysis:")
print("Average MaxTemp:", average_MaxTemp)
print("MaxTemp Standard Deviation:", MaxTemp_std_dev)

#Analyse MinTemp

average_MaxTemp = Weather_data['MaxTemp'].mean()
MaxTemp_std_dev = Weather_data['MaxTemp'].std()

print("MaxTemp Analysis:")
print("Average MaxTemp:", average_MaxTemp)
print("MaxTemp Standard Deviation:", MaxTemp_std_dev)

#Analyze WindSpeed3pm

average_windspeed3pm = Weather_data['WindSpeed3pm'].mean()
max_windspeed3pm = Weather_data['WindSpeed3pm'].max()
min_windspeed3pm = Weather_data['WindSpeed3pm'].min()
windspeed3pm_std_dev = Weather_data['WindSpeed3pm'].std()

print("\nWindSpeed3pm Analysis:")
print("Average WindSpeed3pm:", average_windspeed3pm)
print("Max WindSpeed3pm:", max_windspeed3pm)
print("Min WindSpeed3pm:", min_windspeed3pm)
print("WindSpeed3pm Standard Deviation:", windspeed3pm_std_dev)

"""**Data Visualization**"""

#Scatter plot

plt.figure(figsize=(10, 6))
plt.scatter(Weather_data['MaxTemp'], Weather_data['Sunshine'], color='hotpink', alpha=0.7)
plt.title('Scatter Plot of MaxTemp vs Sunshine')
plt.xlabel('MaxTemp')
plt.ylabel('Sunshine')
plt.grid(True)
plt.show()

#Bar plot

plt.figure(figsize=(10, 6))
count = Weather_data['WindGustDir'].value_counts()
count.plot(kind='bar')
plt.title('Count of WindGustDir')
plt.xlabel('WindGustDir')
plt.ylabel('Count')
plt.show()

# Line plot

plt.figure(figsize=(9, 6))
plt.plot(Weather_data['MinTemp'], marker='o', linestyle='-', label='MinTemp', alpha=0.5)
plt.plot(Weather_data['MaxTemp'], marker='o', linestyle='-', label='MaxTemp', alpha=0.5)
plt.title('Temperature Over Time')
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.show()

# Histogram

plt.figure(figsize=(8, 6))
plt.hist(Weather_data['Rainfall'], bins=30, color='skyblue', alpha=0.7)
plt.title('Histogram of Rainfall')
plt.xlabel('Rainfall')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

#Heatmap

correlation_matrix = Weather_data[['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

#Distribution plot of MaxTemp

sns.histplot(Weather_data['MaxTemp'], kde=True)

"""**Advanced Analysis or Rainfall Prediction**"""

# Preparing the data for prediction

X = Weather_data[['MinTemp', 'MaxTemp']]
y = Weather_data['Rainfall']

# Splitting the data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions and calculate the Mean Squared Error

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error for Rainfall Prediction: {mse}')

"""**Conclusion and Insights**

1.Mean Squared Error for Rainfall Prediction: 37.0768456005826

2.Average MinTemp: 7.265573770491804

3.Average MaxTemp: 20.550273224043714

4.Mean of Evaporation: 4.521858

5.Max Sunshine: 13.600000

.
"""