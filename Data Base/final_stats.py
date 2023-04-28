
import os

import pyarrow.parquet as pq
import pandas as pd


cwd = os.getcwd()
sep = os.sep


output_directory = f"{cwd}{sep}stats{sep}"

measure_stats = pd.DataFrame(columns=["location", "Number of Visits", "Average Dwelling Time"])
number_of_visits_series = pd.DataFrame(columns=["Time Series", "Date", "# of Visits"])
spatial_stats = pd.DataFrame()
business_per_cat = pd.DataFrame(columns=["Category", "Number of Buisnesses", "List of Businesses in Category"])

#Number of business per category

def measure_stats_function(row):
    if (row[6] not in measure_stats.values):
        measure_stats.loc[len(measure_stats)] = {"location": row[6], "Number of Visits": 1, "Average Dwelling Time":row[15]}

    else:
        measure_stats.loc[measure_stats['location'] == row[6], "Average Dwelling Time"] += row[15]
        measure_stats.loc[measure_stats['location'] == row[6], "Number of Visits"] += 1

def number_of_businesses_per_category(row):
    if (row[7] not in business_per_cat.values):
        business_per_cat.loc[len(business_per_cat)] = {"Category": row[7], "Number of Buisnesses": 1, "List of Businesses in Category": [row[8]]}
    else:
        #buisness not in list, add it
        if (row[8] not in business_per_cat.values):
            business_per_cat.loc[business_per_cat["Category"] == row[7], "List of Businesses in Category"].append(row[8])

        #add # of buisnesses
        else:
            business_per_cat.loc[business_per_cat["Category"] == row[7], "Number of Buisnesses"] += 1


#For each month

anual_visits = 0
monthly_visits = 0
weekly_visits = 0
daily_visits = 0

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
                    number_of_businesses_per_category(row)
                    anual_visits += 1
                    monthly_visits += 1

                    #Its April
                    if (i == 3):
                        weekly_visits += 1
                        if (day in range(1, 22)):
                            daily_visits += 1
        
        if (day % 7 and i == 3):
            number_of_visits_series.loc[len(number_of_visits_series)] = {"Time Series": "Weekly", "Date": f"Week {day % 7}", "# of Visits": weekly_visits}
            daily_visits = 0
        if (i == 3 and day in range(1, 22)):
            number_of_visits_series.loc[len(number_of_visits_series)] = {"Time Series": "Daily", "Date": f"Day {day}", "# of Visits": daily_visits}

    number_of_visits_series.loc[len(number_of_visits_series)] = {"Time Series": "Month", "Date": f"Month {i}", "# of Visits": monthly_visits}
    monthly_visits = 0

number_of_visits_series.loc[len(number_of_visits_series)] = {"Time Series": "Anual", "Date": "2023", "# of Visits": anual_visits}



# csv_filename = os.path.splitext(filename)[0] + '.csv'
# csv_filepath = os.path.join(output_directory, csv_filename)
# df.to_csv(csv_filepath, index=False)
        

measure_stats.to_csv(os.path.join(output_directory, "Measure stats.csv"), index=False)
number_of_visits_series.to_csv(os.path.join(output_directory, "Number of visits.csv"), index=False)
business_per_cat.to_csv(os.path.join(output_directory, "Buisness visits.csv"), index=False)


				
                