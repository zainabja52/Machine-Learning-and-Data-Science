import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\twitter\OneDrive\Desktop\ML\cleaned_electric_vehicle_population_data.csv")
fig, axes = plt.subplots(2, 3, figsize=(20, 10))  # 2 rows, 3 columns for a total of 6 plots
axes = axes.flatten()

# Scatter Plot 1: Electric Range vs. Base MSRP
sns.scatterplot(data=df, x='Electric Range', y='Base MSRP', color='#A5B68D', ax=axes[0])
axes[0].set_title('Electric Range vs. Base MSRP', fontsize=14)
axes[0].set_xlabel('Electric Range')
axes[0].set_ylabel('Base MSRP')

# Scatter Plot 2: Model Year vs. Electric Range
sns.scatterplot(data=df, x='Model Year', y='Electric Range', color='#A5B68D', ax=axes[1])
axes[1].set_title('Model Year vs. Electric Range', fontsize=14)
axes[1].set_xlabel('Model Year')
axes[1].set_ylabel('Electric Range')

# Scatter Plot 3: Base MSRP vs. Model Year
sns.scatterplot(data=df, x='Model Year', y='Base MSRP', color='#A5B68D', ax=axes[2])
axes[2].set_title('Base MSRP vs. Model Year', fontsize=14)
axes[2].set_xlabel('Model Year')
axes[2].set_ylabel('Base MSRP')

# Scatter Plot 4: Electric Range vs. Model Year (reversed axes)
sns.scatterplot(data=df, x='Electric Range', y='Model Year', color='#A5B68D', ax=axes[3])
axes[3].set_title('Electric Range vs. Model Year', fontsize=14)
axes[3].set_xlabel('Electric Range')
axes[3].set_ylabel('Model Year')

# Scatter Plot 5: Electric Range vs. Legislative District
if 'Legislative District' in df.columns:
    sns.scatterplot(data=df, x='Legislative District', y='Electric Range', color='#A5B68D', ax=axes[4])
    axes[4].set_title('Electric Range vs. Legislative District', fontsize=14)
    axes[4].set_xlabel('Legislative District')
    axes[4].set_ylabel('Electric Range')

# Scatter Plot 6: Base MSRP vs. Electric Range
sns.scatterplot(data=df, x='Base MSRP', y='Electric Range', color='#A5B68D', ax=axes[5])
axes[5].set_title('Base MSRP vs. Electric Range', fontsize=14)
axes[5].set_xlabel('Base MSRP')
axes[5].set_ylabel('Electric Range')

plt.tight_layout()
plt.show()
