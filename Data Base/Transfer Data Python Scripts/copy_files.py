import psycopg2
import os

conn_string = "host='127.0.0.1' dbname='sdp' \
    user='db_user' password='mypasswd'"

connector = psycopg2.connect(conn_string)
engine = connector.cursor()

months_folder = ""
sep = os.sep

#list days in month directory
for day_folder in os.listdir(months_folder):
    #list csv files in every days folder
    for csv_file in os.listdir(f"{months_folder}{sep}{day_folder}"):
        sql_command = f"""COPY "map-data"."all-data" \
FROM '{months_folder}{sep}{day_folder}{sep}{csv_file}' \
DELIMITER ',' \
CSV HEADER;"""
        engine.execute(sql_command)

connector.commit()

engine.close()
connector.close()