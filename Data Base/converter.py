import pandas as pd
import pygeohash as pgh
import sys
from datetime import datetime



def gh_decode(hash):
    lat, lon = pgh.decode(hash)
    return pd.Series({"latitude":lat, "longitude":lon})

def uts_decode(timestamp):
    utc = datetime.fromtimestamp(timestamp)
    return pd.Series({"utc_datetime":utc})

def lts_decode(timestamp):
    lts = datetime.fromtimestamp(timestamp)
    return pd.Series({"local_datetime":lts})

if len(sys.argv) != 2:
    print("Please input 1 csv file")
    exit()

df = pd.read_csv(sys.argv[1])

if "latitude" not in df:
    df = df.join(df["geohash_5"].apply(gh_decode))

if "utc_time" not in df:
    df = df.join(df["utc_timestamp"].apply(uts_decode))

if "local_datetime" not in df:
    df = df.join(df["local_timestamp"].apply(lts_decode))

df.to_csv(sys.argv[1])