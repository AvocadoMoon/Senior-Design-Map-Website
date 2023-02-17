import pandas as pd
import os
import time
from datetime import datetime
import pytz

sep = os.sep
parq_file = r"D:\Home\School\CS\3 Concentration and High Level Courses\CS Senior Design\Senior-Design-Map-Website\Data Base\data\2019\01\01\part-00000-tid-5103165951321984738-28cc9dfd-ac51-40ee-8b75-a80dd27932e3-18665-1-c000.snappy.parquet"


def listRows(parq_directory):
    print("Starting read")
    dir = os.listdir(parq_directory)
    nRows = 0
    startTime = time.time()
    for fil in dir:
        dataFrame = pd.read_parquet(parq_file + "\\" +fil)
        nRows += len(dataFrame)
        print("The current number of rows is " + str(nRows))

    print("Ended read")

    print("It has taken the script " + str(time.time() - startTime) + " seconds to run")


def get_all_POI_data_rows(veraset_directory:str, save_path_directory:str):
    years = os.listdir(veraset_directory)
    for year in years:
        visits_df = pd.DataFrame(columns=["date", "top_category_POI", "number_of_visit_that_day"])
        months = os.listdir(f"{veraset_directory}{sep}{year}")
        for month in months:
            days = os.listdir(f"{veraset_directory}{sep}{year}{sep}{month}")
            for day in days:
                full_path = f"{veraset_directory}{sep}{year}{sep}{month}{sep}{day}"
                list_of_todays_files = os.listdir(full_path)
                todays_df = pd.DataFrame()
                print(f"Day {day}")
                for file in list_of_todays_files:
                    #check if the category row is filled, if not then drop that stuff
                    files_df = pd.read_parquet(f"{full_path}{sep}{file}").dropna(subset=["top_category", "sub_category", "utc_timestamp"])
                    todays_df = pd.concat([todays_df, files_df])


                #adds the number of visits for that day to the total list
                list_of_categories = todays_df["top_category"].unique().tolist()
                print("Categories")
                for category in list_of_categories:
                    rows_of_category = todays_df.loc[todays_df["top_category"].isin([category])]
                    number_of_rows = len(rows_of_category)
                    visits_df.loc[len(visits_df)] = [f"{month}/{day}/{year}", category, number_of_rows]
    
        visits_df.to_csv(f"{save_path_directory}{sep}{year}_poi.csv")



def get_eastern_time():
    est = pytz.timezone('US/Eastern')
    utc = pytz.utc
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'

data_path = r"D:\Home\School\CS\3 Concentration and High Level Courses\CS Senior Design\Senior-Design-Map-Website\Data Base\data"
save_path = r"D:\Home\School\CS\3 Concentration and High Level Courses\CS Senior Design\Senior-Design-Map-Website"
get_all_POI_data_rows(data_path, save_path)
# dataFrame = pd.read_parquet(parq_file)
# dataFrame.info()
# shortDF = dataFrame.head(1000)
# dataFrame = dataFrame.dropna(subset=["top_category", "sub_category"]).info()

# calcualte_visits_percategory(dataFrame)