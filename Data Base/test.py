
import os
import pyarrow.parquet as pq
import pandas as pd

cwd = os.getcwd()
sep = os.sep

output_directory = f"{cwd}{sep}stats{sep}"
measure_stats = pd.DataFrame(columns=["location", "Number of Visits", "Average Dwelling Time"])
# measure_stats.set_index("location", inplace=True)

temporal_time_series = pd.DataFrame(columns=["Anual", "Monthly", "April Weekly", "Daily Week 3 April"])
spatial_stats = pd.DataFrame()


# Load Parquet file into Pandas DataFrame
filepath = r"D:\Home\School\CS\3 Concentration and High Level Courses\CS Senior Design\Senior-Design-Map-Website\testCSV.csv"
df = pd.read_csv(filepath)

# Filter for data from Connecticut
df = df[(df['state'] == 'ct') | (df['state'] == 'connecticut')]

# print(df)
for row in df.itertuples():
    print(row[6])
    print(row[6] not in measure_stats.values)
    if (row[6] not in measure_stats.values):
        # {"location": row[6], "Number of Visits": 1, "Average Dwelling Time":row[15]}
        # new_df = pd.DataFrame([{"location": row[6], "Number of Visits": 1, "Average Dwelling Time":row[15]}])
        measure_stats.loc[len(measure_stats)] = {"location": row[6], "Number of Visits": 1, "Average Dwelling Time":row[15]}
        # new_df.set_index("location", inplace=True)
        # measure_stats = pd.concat([measure_stats, new_df], ignore_index=False)
        # measure_stats.set_index("location", inplace=False)
    else:
        measure_stats.loc[measure_stats['location'] == row[6], "Average Dwelling Time"] += row[15]
        measure_stats.loc[measure_stats['location'] == row[6], "Number of Visits"] += 1

# df.replace(r'^\s+$', None, regex=True) #Replaces empty values with None value so that its easier to transfer to PostgreSQL

print(measure_stats)
#For every new location, concat it to new dictionary
# measure_stats["location"].astype(str).str.contains(row[5])
# [measure_stats.append({"location": row[6], "Number of Visits": 1, "Average Dwelling Time":row[15]}, ignore_index=True) if (not any(measure_stats.columns == row[6])) else add_average_and_visits(row) for row in df.itertuples()]
# measure_stats = measure_stats.append(
    #if the location is not in measure stats, add the location, visit of 1, and minimum dwell time; else add 1 to visits and add to average
    #location_name index is 5, min_dwell is 14
    # other= [[row[6], 1, row[15]]  if (not any(measure_stats.columns == row[6])) else add_average_and_visits(row) for row in df.itertuples()]
# )

# print(measure_stats)

# csv_filename = os.path.splitext(filename)[0] + '.csv'
# csv_filepath = os.path.join(output_directory, csv_filename)
# df.to_csv(csv_filepath, index=False)

# measure_stats.to_csv(csv_filepath, index=False)