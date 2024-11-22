import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Load the cleaned CSV file (replace 'cleaned_street_trees.csv' with your actual CSV file path)
df = pd.read_csv('cleaned_street_trees.csv')

# Convert Latitude and Longitude to numeric values
df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')
df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')
df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

# Create a GeoDataFrame for the tree data
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['Longitude'], df['Latitude']))

# Set the coordinate reference system to WGS84 (EPSG:4326)
gdf.set_crs(epsg=4326, inplace=True)

# Export the GeoDataFrame to a GeoJSON file for use with Mapbox
gdf.to_file("street_trees.geojson", driver="GeoJSON")

print("GeoJSON file 'street_trees.geojson' has been successfully created.")
