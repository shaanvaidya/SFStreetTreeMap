import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as ctx
from shapely.geometry import Point

# Load the cleaned CSV file (replace 'cleaned_street_trees.csv' with your actual CSV file path)
df = pd.read_csv('cleaned_street_trees.csv')

# Count the number of each species and sort the list in descending order
species_count = df['Species'].value_counts().sort_values(ascending=False)

# Optionally, save the species count to a new file
species_count.to_csv('species_count.csv', header=['Count'])

# Count the number of trees by neighborhood
neighborhood_count = df['Analysis Neighborhoods'].value_counts().sort_values(ascending=False)

# Print the sorted list of neighborhood tree counts
print("\nTree counts by neighborhood (sorted):")
for neighborhood, count in neighborhood_count.items():
    print(f"{neighborhood}: {count}")

# Optionally, save the neighborhood tree count to a new file
neighborhood_count.to_csv('neighborhood_tree_count.csv', header=['Count'])
