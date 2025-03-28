import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\twitter\OneDrive\Desktop\ML\cleaned_electric_vehicle_population_data.csv")

numerical_features = df.select_dtypes(include=['float64', 'int64']).columns

#--------------------------------------------------------------------------------------
n_rows = (len(numerical_features) + 2) // 3
plt.figure(figsize=(15, 10))


for i, feature in enumerate(numerical_features, 1):
    plt.subplot(n_rows, 3, i)
    sns.histplot(df[feature], bins=30, kde=True, color='#A5B68D', edgecolor='black')
    plt.title(f'Histogram of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
