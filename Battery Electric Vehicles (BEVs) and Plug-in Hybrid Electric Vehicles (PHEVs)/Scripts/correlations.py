import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors

df = pd.read_csv(r"C:\Users\twitter\OneDrive\Desktop\ML\cleaned_electric_vehicle_population_data.csv")

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
numeric_df = df[numeric_cols]

# Compute the correlation matrix
corr_matrix = numeric_df.corr()

# Create a custom colormap
colors = ["#E7CCCC", "#EDE8DC", "#A5B68D", "#C1CFA1"]
cmap = mcolors.LinearSegmentedColormap.from_list("custom_cmap", colors)

# Visualize the correlation matrix using a heatmap with the custom colormap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap=cmap, cbar=True)
plt.title('Correlation Matrix of Numeric Features')
plt.show()