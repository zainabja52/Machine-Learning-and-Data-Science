import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\twitter\OneDrive\Desktop\ML\cleaned_electric_vehicle_population_data.csv")

make_columns = [col for col in df.columns if col.startswith('Make_')]
df['Make'] = df[make_columns].idxmax(axis=1).str.replace('Make_', '')
make_popularity = df.groupby('Make').size().reset_index(name='Count').sort_values(by='Count', ascending=False)

plt.figure(figsize=(12, 10))

# Plot for 'Make'
plt.subplot(2, 1, 1)
plt.bar(make_popularity['Make'], make_popularity['Count'], color='#E7CCCC')
plt.xlabel('EV Make')
plt.ylabel('Count')
plt.title('Popularity of Different EV Makes')
plt.xticks(rotation=90)

model_columns = [col for col in df.columns if col.startswith('Model_')]
df['Model'] = df[model_columns].idxmax(axis=1).str.replace('Model_', '')
model_popularity = df.groupby('Model').size().reset_index(name='Count').sort_values(by='Count', ascending=False)

# Plot for 'Model'
plt.subplot(2, 1, 2)
plt.bar(model_popularity['Model'], model_popularity['Count'], color='#A5B68D')
plt.xlabel('EV Model')
plt.ylabel('Count')
plt.title('Popularity of Different EV Models')
plt.xticks(rotation=90, fontsize=6)


plt.tight_layout()
plt.show()
