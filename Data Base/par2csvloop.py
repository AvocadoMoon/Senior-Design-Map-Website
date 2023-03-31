import os
import pyarrow.parquet as pq
import pandas as pd

cwd = os.getcwd()
sep = os.sep

for i in range (1, 7):
    # Set the directory path
    directory = f"D:{sep}Home\School\CS{sep}3 Concentration and High Level Courses\CS Senior Design\Feb 2023\{i:02d}"

    # Set the output directory path
    output_directory = os.path.expanduser(f"D:\Home\School\CS{sep}3 Concentration and High Level Courses\CS Senior Design\Feb 20230 CSV From CT\{i:02d}")

    # Loop over all Parquet files in the directory
    print(f"Day {i}")
    for filename in os.listdir(directory):
        if filename.endswith('.parquet'):
            # Load Parquet file into Pandas DataFrame
            filepath = os.path.join(directory, filename)
            df = pd.read_parquet(filepath)

            # Filter for data from Connecticut
            df = df[(df['state'] == 'ct') | (df['state'] == 'connecticut')]
            # Filter for data from food places 
            # df = df[(df['top_category'] == 'Restaurants and Other Eating Places')]
            # Write filtered data to CSV file with the same base filename
            df.replace(r'^\s+$', None, regex=True)
            csv_filename = os.path.splitext(filename)[0] + '.csv'
            csv_filepath = os.path.join(output_directory, csv_filename)
            df.to_csv(csv_filepath, index=False)
