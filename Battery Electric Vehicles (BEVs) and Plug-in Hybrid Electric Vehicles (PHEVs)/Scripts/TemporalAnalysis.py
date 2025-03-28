#11. Temporal Analysis (Optional): If the dataset includes data across multiple time points, analyze the temporal trends in EV adoption rates and model popularity.
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r'D:\Project\cleaned_electric_vehicle_population_data.csv')


adoption_rates = df['Model Year'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
adoption_rates.plot(kind='line', marker='o', color='b')
plt.title('EV Adoption Rates Over Time')
plt.xlabel('Year')
plt.ylabel('Number of EV Registrations')
plt.grid(True)
plt.show()


if 'Model' in df.columns:
    top_models = df['Model'].value_counts().nlargest(5).index
    model_popularity = df[df['Model'].isin(top_models)].groupby(['Model Year', 'Model']).size().unstack(fill_value=0)
    model_popularity.plot(kind='bar', stacked=True, figsize=(14, 7))
    plt.title('Model Popularity Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Registrations')
    plt.legend(title='Model')
    plt.xticks(rotation=45)
    plt.show()
else:
    print("Model column not found. Ensure there's a column defining vehicle models.")

