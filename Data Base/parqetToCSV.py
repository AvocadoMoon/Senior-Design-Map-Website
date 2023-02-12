import pandas as pd
import os
import time

sep = os.sep
parq_file = r"D:\Home\School\CS\3 Concentration and High Level Courses\CS Senior Design\Senior-Design-Map-Website\Data Base\data\part-00000-tid-5103165951321984738-28cc9dfd-ac51-40ee-8b75-a80dd27932e3-18665-1-c000.snappy.parquet"


print("Starting read")
def listRows(parq_directory):
    dir = os.listdir(parq_directory)
    nRows = 0
    startTime = time.time()
    for fil in dir:
        dataFrame = pd.read_parquet(parq_file + "\\" +fil)
        nRows += len(dataFrame)
        print("The current number of rows is " + str(nRows))

    print("Ended read")

    print("It has taken the script " + str(time.time() - startTime) + " seconds to run")

dataFrame = pd.read_parquet(parq_file)
dataFrame.info()
shortDF = dataFrame.head(1000)
dataFrame = dataFrame.dropna()
pd.concat([shortDF, dataFrame.head(100)]).to_csv("testCSV.csv")