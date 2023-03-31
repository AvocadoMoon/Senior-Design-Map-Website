import csv
import os

months_folder = ""
sep = os.sep

#list days in month directory
for day_folder in os.listdir(months_folder):
    #list csv files in every days folder
    for csv_file in os.listdir(f"{months_folder}{sep}{day_folder}"):

        with open(f"{months_folder}{sep}{day_folder}{sep}{csv_file}", 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                for i in range(len(row)):
                    if row[i] == '':
                        row[i] = None