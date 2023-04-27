import pandas as pd

# Read the input CSV file into a Pandas DataFrame
df = pd.read_csv('combined_data.csv')

# Group the DataFrame by "location_name", "sub_category", "state", and "geohash_5" and
# count the number of occurrences for each group
grouped = df.groupby(['location_name', 'sub_category', 'state', 'geohash_5']).agg(
    count=pd.NamedAgg(column='dateTime', aggfunc='count'),
    date=pd.NamedAgg(column='dateTime', aggfunc=lambda x: x.str[:10].unique()[0]),
    latitude=pd.NamedAgg(column='latitude', aggfunc='first'),
    longitude=pd.NamedAgg(column='longitude', aggfunc='first')
).reset_index()

# Rename the columns of the DataFrame
grouped.columns = ['location_name', 'sub_category', 'state', 'geohash_5', 'total_count', 'date', 'latitude', 'longitude']

# Write the results to a new CSV file
grouped.to_csv('output.csv', index=False)
