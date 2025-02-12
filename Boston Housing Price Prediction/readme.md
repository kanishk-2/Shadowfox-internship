# Boston Housing Price Prediction:


## Overview:

This project aims to predict house prices using various regression models, including Linear Regression, Ridge Regression, and Lasso Regression. The dataset used is HousingData.csv, which contains various features related to houses.

## Data Preprocessing:
    * Handling missing values using SimpleImputer with the median strategy.
    * Feature scaling using StandardScaler.
    * Handling outliers and visualizing data distributions.
    
## Machine Learning Models:
    * Linear Regression: A simple baseline model for predictions.
    * Ridge Regression: Implements L2 regularization to avoid overfitting.
    * Lasso Regression: Implements L1 regularization for feature selection.
    
## Model Evaluation:
    * Metrics used: Mean Squared Error (MSE) and R-Squared (R²) score.
    * Visualization of predictions vs actual values using matplotlib.

    
## Installation and Requirements
Ensure you have Python installed along with the required libraries.
* pandas
* numpy
* matplotlib
* seaborn
* sklearn

## Detailed Summary:

The Housing Price Prediction project focuses on analyzing housing data to develop an accurate predictive model for house prices. The dataset consists of multiple features, such as location, number of rooms, crime rate, and other structural attributes. The project involves data preprocessing, including handling missing values, feature scaling, and outlier treatment to ensure data quality. Multiple regression models, such as Linear Regression, Ridge Regression, and Lasso Regression, are implemented and compared based on performance metrics like Mean Squared Error (MSE) and R-Squared (R²) score. Additionally, data visualization techniques are used to better understand the distribution of house prices and the relationship between features. The project aims to provide insights into the key factors affecting house prices and create a reliable prediction model that can assist stakeholders in making informed decisions.
