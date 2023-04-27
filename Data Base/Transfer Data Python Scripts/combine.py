import os
import pandas as pd
from datetime import datetime

# Set the output directory path
output_directory = os.path.expanduser("/home/jcm20007/sdp/data/combined")

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Create an empty DataFrame to store the combined data
combined_df = pd.DataFrame()

# Loop over all directories
for i in range(1, 29):
    # Set the directory path
    directory = f"/home/jcm20007/sdp/data/{i:02d}"

    # Loop over all CSV files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            # Load CSV file into Pandas DataFrame
            filepath = os.path.join(directory, filename)
            df = pd.read_csv(filepath)

            # Convert the "utc_timestamp" column to datetime format
            df['dateTime'] = pd.to_datetime(df['utc_timestamp'], unit='s')

            # Append the DataFrame to the combined DataFrame
            combined_df = pd.concat([combined_df, df], ignore_index=True)

# Sort the combined DataFrame by the "dateTime" column
combined_df = combined_df.sort_values('dateTime')

# Write the combined DataFrame to a CSV file
output_filepath = os.path.join(output_directory, 'combined_data.csv')
combined_df.to_csv(output_filepath, index=False)
