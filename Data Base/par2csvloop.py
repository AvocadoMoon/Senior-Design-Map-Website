import os
import pyarrow.parquet as pq
import pandas as pd

for i in range (1, 29):
    # Set the directory path
    directory = f"/shared/veraset/veraset-s3-data-transfer/2023/01/{i:02d}"

    # Set the output directory path
    output_directory = os.path.expanduser(f"/home/jcm20007/sdp/data/{i:02d}")

    # Loop over all Parquet files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.parquet'):
            # Load Parquet file into Pandas DataFrame
            filepath = os.path.join(directory, filename)
            df = pd.read_parquet(filepath)

            # Filter for data from Connecticut
            df = df[(df['state'] == 'ct') | (df['state'] == 'connecticut')]
            # Filter for data from food places 
            df = df[(df['top_category'] == 'Restaurants and Other Eating Places')]
            # Write filtered data to CSV file with the same base filename
            csv_filename = os.path.splitext(filename)[0] + '.csv'
            csv_filepath = os.path.join(output_directory, csv_filename)
            df.to_csv(csv_filepath, index=False)
