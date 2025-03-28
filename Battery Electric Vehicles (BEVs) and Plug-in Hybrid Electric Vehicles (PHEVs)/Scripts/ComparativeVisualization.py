
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:\Project\cleaned_electric_vehicle_population_data.csv')

location_columns = [col for col in df.columns if col.startswith('City_') or col.startswith('County_')]
df['Total EVs'] = df[location_columns].sum(axis=1)

# Get the top 5 locations with the most EVs
top_locations = df[location_columns].sum().nlargest(5).index

# Creating a dataframe for the top locations and EV types
data_for_plotting = df.groupby('Electric Vehicle Type')[top_locations].sum().T

# Colors you specified
colors = ['#A5B68D', '#E7CCCC']  # Adjust the number of colors if you have more EV types

# Plotting
plt.figure(figsize=(14, 10))
data_for_plotting.plot(kind='bar', stacked=True, color=colors)
plt.title('Comparative Distribution of EVs Across Top 5 Locations', fontsize=16)
plt.xlabel('Locations', fontsize=14)
plt.ylabel('Number of EVs', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='EV Type', title_fontsize='13', fontsize='11')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()