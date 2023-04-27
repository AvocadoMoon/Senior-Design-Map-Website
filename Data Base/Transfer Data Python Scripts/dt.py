import os
import pandas as pd
from datetime import datetime

for i in range(1, 29):
    # Set the directory path
    directory = f"/home/jcm20007/sdp/data/{i:02d}"

    # Set the output directory path
    output_directory = os.path.expanduser(f"/home/jcm20007/sdp/data/dateTime/{i:02d}")

    # Loop over all CSV files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            # Load CSV file into Pandas DataFrame
            filepath = os.path.join(directory, filename)
            df = pd.read_csv(filepath)

            # Convert the "utc_timestamp" column to datetime format
            df['dateTime'] = pd.to_datetime(df['utc_timestamp'], unit='s')

            # Write updated DataFrame to a new CSV file
            updated_filename = os.path.splitext(filename)[0] + '_DT.csv'
            updated_filepath = os.path.join(output_directory, updated_filename)
            df.to_csv(updated_filepath, index=False)
