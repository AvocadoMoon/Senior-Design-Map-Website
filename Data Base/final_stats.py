
import os

import pyarrow.parquet as pq
import pandas as pd


cwd = os.getcwd()
sep = os.sep


output_directory = f"{cwd}{sep}stats{sep}"

measure_stats = pd.DataFrame(columns=["location", "Number of Visits", "Average Dwelling Time"])
temporal_time_series = pd.DataFrame(columns=["Anual", "Monthly", "April Weekly", "Daily Week 3 April"])
spatial_stats = pd.DataFrame()


def measure_stats_function(row):
    if (row[6] not in measure_stats.values):
        measure_stats.loc[len(measure_stats)] = {"location": row[6], "Number of Visits": 1, "Average Dwelling Time":row[15]}

    else:
        measure_stats.loc[measure_stats['location'] == row[6], "Average Dwelling Time"] += row[15]
        measure_stats.loc[measure_stats['location'] == row[6], "Number of Visits"] += 1


#For each month

for i in range (1, 4):

    month_directory = f"{cwd}{sep}{i:02d}"
    # Loop over all Parquet files in the directory
    print(f"Month {i}\n---------------\n")

    for day in os.listdir(month_directory):

        print(f"Day {day}")
        os.makedirs(output_directory)

        for filename in os.listdir(f"{month_directory}{sep}{day}"):

            if filename.endswith('.parquet'):
                # Load Parquet file into Pandas DataFrame
                filepath = os.path.join(f"{month_directory}{sep}{day}", filename)
                df = pd.read_parquet(filepath)

                # Filter for data from Connecticut
                df = df[(df['state'] == 'ct') | (df['state'] == 'connecticut')]
                # df.replace(r'^\s+$', None, regex=True) #Replaces empty values with None value so that its easier to transfer to PostgreSQL
                
                ########################################
                ## For loop where stats should happen ##
                ########################################
                for row in df.itertuples():
                    measure_stats_function(row)


csv_filename = os.path.splitext(filename)[0] + '.csv'
csv_filepath = os.path.join(output_directory, csv_filename)
# df.to_csv(csv_filepath, index=False)
        

measure_stats.to_csv(csv_filepath, index=False)

				
                