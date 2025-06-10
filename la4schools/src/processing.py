from src.data import df
import pandas as pd
import numpy as np

def correct_entries(df): #an alternate, unused approach for handling the abnormal data
    df["TextLevel-01-SOY"] = [abs(x) for x in df["TextLevel-01-SOY"]]
    df["HRSIW-01-SOY"] = [abs(x) for x in df["HRSIW-01-SOY"]]
    df.iloc[:, 1:7] = df.iloc[:, 1:7].map(lambda x: 31 if x > 31 else x)
    df.iloc["NumAbvYear9"] = df["NumAbvYear9"].map(lambda x: 2 if x > 2 else x)
    return df

def remove_entries(df):
    df = df.loc[df["TextLevel-01-SOY"]>=0]
    df = df.loc[df["HRSIW-01-SOY"]>=0]
    df = df.loc[(df.iloc[:, 1:7]<=31).all(axis=1)]
    df = df.loc[df["NumAbvYear9"]!=3]
    return df

df = remove_entries(df)
df.Gender = [0 if x == "Male" else 1 for x in df.Gender]
# df.iloc[:, -1] = [0 if x == False else 1 for x in df.iloc[:, -1]]
X = df.iloc[:, 1:-1]
y = df.iloc[:, -1]
y = [0 if x == False else 1 for x in y]

if __name__ == "__main__":
    print(len(X))
    print(df.describe())