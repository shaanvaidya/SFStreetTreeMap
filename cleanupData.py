import pandas as pd

# Load the CSV file (replace 'street_trees.csv' with your actual CSV file path)
df = pd.read_csv('sf_street_trees.csv')

# Rename fields for better readability
rename_mapping = {
    'TreeID': 'Tree ID',
    'qLegalStatus': 'Legal Status',
    'qSpecies': 'Species',
    'qAddress': 'Address',
    'qSiteInfo': 'Site Info',
    'PlantDate': 'Plant Date',
    'Latitude': 'Latitude',
    'Longitude': 'Longitude',
    'Location': 'Location',
    # Keeping 'DBH' as is
}

corrected_values_for_posterity = {
    56697: 30,
    141190: 15,
    133419: 15,
    120977: 15
}

# Apply the renaming
df.rename(columns=rename_mapping, inplace=True)

# Drop the specified fields
drop_fields = ['SiteOrder', 'PlantType', 'qCaretaker', 'qCareAssistant', 'PlotSize', 'PermitNotes', 'XCoord', 'YCoord']
df.drop(columns=drop_fields, inplace=True)

# Print out the column names
print("Column names:", df.columns.tolist())

# Print out Tree ID and Species where the DBH value is null or empty
df['DBH'] = df['DBH'].replace('', pd.NA).astype(float).fillna(10)
null_dbh_cases = df[df['DBH'].isnull() | (df['DBH'] == '')]
print("Tree IDs and Species with null or empty DBH values:")
print(len(null_dbh_cases))
# for _, row in null_dbh_cases.iterrows():
    # print(f"Tree ID: {row['Tree ID']}, Species: {row['Species']}")

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_street_trees.csv', index=False)

print("Data cleaning complete. The cleaned data is saved as 'cleaned_street_trees.csv'.")

# Check for DBH values that are too large and print the Tree ID for those cases
# Assuming a DBH value larger than 300 inches is considered unusually large
# dbh_threshold = 300
# large_dbh_cases = df[df['DBH'].astype(float) > dbh_threshold]
# print("Tree IDs with DBH greater than 60 inches and their DBH values:")
# for _, row in large_dbh_cases.iterrows():
#     print(f"Tree ID: {row['Tree ID']}, DBH: {row['DBH']}")