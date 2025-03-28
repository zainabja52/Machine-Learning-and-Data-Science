#   1. CLEAN DATA

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
data = pd.read_csv(r"C:\Users\twitter\OneDrive\Desktop\ML\Electric_Vehicle_Population_Data.csv")

#   1.1 Document Missing Values
print("Missing values per column:")
print(data.isnull().sum())

numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
non_numeric_cols = data.select_dtypes(include=['object']).columns
data_cleaned = data.copy()

#   1.2 Missing Value Strategies
# Numerical columns: Apply mean or median imputation based on skewness
for col in numerical_cols:
    if abs(data[col].skew()) > 1:
        data_cleaned[col] = data_cleaned[col].fillna(data_cleaned[col].median())
    else:
        data_cleaned[col] = data_cleaned[col].fillna(data_cleaned[col].mean())


# Non-numerical columns: Use mode for imputation
for col in non_numeric_cols:
    if data_cleaned[col].isnull().sum() > 0:
        most_frequent = data_cleaned[col].mode()[0]
        data_cleaned[col] = data_cleaned[col].fillna(most_frequent)


#   1.3 Feature Encoding: One-hot encoding for categorical features
categorical_cols = ['Make', 'Model', 'County', 'City']
data_encoded = pd.get_dummies(data_cleaned, columns=categorical_cols)


#   1.4 Normalization: Normalize numerical features using MinMaxScaler
scaler = MinMaxScaler()
data_encoded[numerical_cols] = scaler.fit_transform(data_encoded[numerical_cols])

# Save the cleaned and encoded data to a new CSV file
data_encoded.to_csv(r"C:\Users\twitter\OneDrive\Desktop\ML\cleaned_electric_vehicle_population_data.csv", index=False)

print("Data preprocessing completed and saved.")

#  2.Exploratory Data Analysis

# 2.1 Descriptive Statistics
# Calculate summary statistics (mean, median, standard deviation) for numerical features
summary_stats = data_encoded[numerical_cols].describe().T
summary_stats['median'] = data_encoded[numerical_cols].median()
summary_stats = summary_stats[['mean', 'median', 'std']]

print("Summary statistics for numerical features:")
print(summary_stats)
