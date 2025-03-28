import pandas as pd
import folium
from folium.plugins import MarkerCluster
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

print("Loading dataset...")
df = pd.read_csv(r'/content/drive/MyDrive/Machine/cleaned_electric_vehicle_population_data.csv')
print("Dataset loaded successfully.")
print("Columns in the dataset:", df.columns)

# Identify city columns
print("Identifying city columns...")
city_columns = [col for col in df.columns if col.startswith('City_')]
print("City columns identified:", city_columns)

# Extract city names and counts
print("Extracting city names and counts...")
city_data = []
for col in city_columns:
    city_name = col.replace('City_', '')
    city_count = df[col].sum()
    if city_count > 0:
        city_data.append((city_name, city_count))
print("City data extracted:", city_data)

# Convert to DataFrame
print("Converting city data to DataFrame...")
city_df = pd.DataFrame(city_data, columns=['City', 'EV_Count'])
print("City DataFrame created:")
print(city_df)

print("Geocoding city names...")
geolocator = Nominatim(user_agent="ev_analysis", timeout=10)

def get_lat_long(city):
    try:
        location = geolocator.geocode(city)
        if location:
            return location.latitude, location.longitude
        else:
            print(f"Geocoding failed for city: {city}")
            return None, None
    except GeocoderTimedOut:
        print(f"Timeout error for city: {city}. Retrying...")
        time.sleep(1)
        return get_lat_long(city)
    except Exception as e:
        print(f"Error geocoding city {city}: {e}")
        return None, None

city_df[['Latitude', 'Longitude']] = city_df['City'].apply(lambda city: get_lat_long(city)).apply(pd.Series)
print("Geocoding completed.")
print(city_df)

city_df = city_df.dropna(subset=['Latitude', 'Longitude'])
print("Filtered DataFrame with valid coordinates:")
print(city_df)

print("Creating base map...")
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)
print("Base map created.")

print("Creating marker cluster...")
marker_cluster = MarkerCluster().add_to(m)

print("Adding markers to the map...")
for index, row in city_df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['City']}\nEV Count: {row['EV_Count']}"
    ).add_to(marker_cluster)
print("Markers added.")

print("Saving the map to an HTML file...")
m.save('ev_spatial_distribution.html')
print("Map saved as 'ev_spatial_distribution.html'.")

