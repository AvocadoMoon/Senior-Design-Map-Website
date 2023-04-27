
import os
import pyarrow.parquet as pq
import pandas as pd

cwd = os.getcwd()
sep = os.sep

output_directory = f"{cwd}{sep}stats{sep}"
measure_stats = pd.DataFrame(columns=["location", "Number of Visits", "Average Dwelling Time"])
temporal_time_series = pd.DataFrame(columns=["Anual", "Monthly", "April Weekly", "Daily Week 3 April"])
spatial_stats = pd.DataFrame()

def add_average_and_visits(row):
    measure_stats[row["location_name"]]["Average Dwelling Time"] += row["minimum_dwell"]
    measure_stats[row["location_name"]]["Number of Visits"] += 1

#For each month
for i in range (1, 4):
    # Set the directory path
    directory = f"{cwd}{sep}{i:02d}"

    # Set the output directory path

    # Loop over all Parquet files in the directory
    print(f"Month {i}\n---------------\n")
    for day in os.listdir(directory):
        print(f"Day {day}")
        os.makedirs(output_directory)
        for filename in os.listdir(f"{directory}{sep}{day}"):
            if filename.endswith('.parquet'):
                # Load Parquet file into Pandas DataFrame
                filepath = os.path.join(f"{directory}{sep}{day}", filename)
                df = pd.read_parquet(filepath)

            # Filter for data from Connecticut
                df = df[(df['state'] == 'ct') | (df['state'] == 'connecticut')]

                # df.replace(r'^\s+$', None, regex=True) #Replaces empty values with None value so that its easier to transfer to PostgreSQL
                
                #For every new location, concat it to new dictionary
                df["location"]
                measure_stats["location"] 
                measure_stats.append(
                    #if the location is not in measure stats, add the location, visit of 1, and minimum dwell time; else add 1 to visits and add to average
                    other= [[row["location_name"], 1, row["minimum_dwell"]]  if not measure_stats["location"].astype(str).str.contains(df[row]["location"]) else add_average_and_visits(row) for row in df]
                )

                csv_filename = os.path.splitext(filename)[0] + '.csv'
                csv_filepath = os.path.join(output_directory, csv_filename)
                df.to_csv(csv_filepath, index=False)
				
                