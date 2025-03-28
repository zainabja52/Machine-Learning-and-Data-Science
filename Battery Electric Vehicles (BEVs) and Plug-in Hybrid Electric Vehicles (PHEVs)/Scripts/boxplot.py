import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\twitter\OneDrive\Desktop\ML\cleaned_electric_vehicle_population_data.csv")
df.columns = df.columns.str.strip()

make_columns = [col for col in df.columns if col.startswith('Make_')]
df['Make'] = df[make_columns].idxmax(axis=1).str.replace('Make_', '')

# Select specific categorical and numerical features for 6 plots
categorical_features = ['Make', 'Electric Vehicle Type']
numerical_features = ['Electric Range', 'Base MSRP', 'Model Year']

# Set up the figure with 6 subplots
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.flatten()

# Loop through selected categorical and numerical features to create boxplots
plot_index = 0
for cat_feature in categorical_features:
    for num_feature in numerical_features:
        if cat_feature in df.columns and num_feature in df.columns:
            if df[cat_feature].nunique() > 20:
                df_sampled = df[df[cat_feature].isin(df[cat_feature].value_counts().index[:20])]
            else:
                df_sampled = df

            sns.boxplot(data=df_sampled, x=cat_feature, y=num_feature, ax=axes[plot_index], hue=None)
            axes[plot_index].set_xlabel(cat_feature)
            axes[plot_index].set_ylabel(num_feature)
            axes[plot_index].set_title(f'{num_feature} by {cat_feature}')
            axes[plot_index].tick_params(axis='x', rotation=90)
            plot_index += 1
        else:
            # Hide any remaining empty subplots if any
            axes[plot_index].axis('off')
            plot_index += 1

plt.tight_layout()
plt.show()
