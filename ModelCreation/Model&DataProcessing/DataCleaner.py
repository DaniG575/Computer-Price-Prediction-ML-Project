import pandas as pd
from sklearn import linear_model as lm
from matplotlib import pyplot as plt
import seaborn as snsfrom
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from scipy.stats import norm
import re


def extract_ghz(cpu_string):
    match = re.search(r'(\d+(\.\d+)?)\s*GHz', cpu_string)
    if match:
        return float(match.group(1))
    return None

def extract_ssd(storage_string):
    match = re.search(r'(\d+)(GB|TB) SSD', storage_string)
    if match:
        value = int(match.group(1))
        unit = match.group(2)
        return value * 1024 if unit == 'TB' else value
    return None

def extract_hdd(storage_string):
    match = re.search(r'(\d+)(GB|TB) HDD', storage_string)
    if match:
        value = int(match.group(1))
        unit = match.group(2)
        return value * 1024 if unit == 'TB' else value
    return None

def classify_gpu(gpu_string):
    if 'Nvidia GeForce' in gpu_string:
        return 'Nvidia Geforce'
    elif 'Nvidia' in gpu_string:
        return 'Nvidia non-Geforce'
    elif 'Intel Iris' in gpu_string:
        return 'Intel Iris'
    elif 'Intel HD Graphics' in gpu_string or 'Intel UHD Graphics' in gpu_string or 'Intel Graphics' in gpu_string:
        return 'Intel Graphics'
    elif 'AMD' in gpu_string:
        return 'AMD'
    else:
        return 'Other'


df = pd.read_csv("ModelCreation/Model&DataProcessing/laptop_price.csv", encoding='ISO-8859-1')
df1 = df.drop(["laptop_ID","Company","Product","TypeName"], axis="columns")
print(df1.info())
print(df1.ScreenResolution.unique())
df1["HR"] = df1.ScreenResolution.apply(lambda x: float(x.split("x")[0][-4:]))
df1["VR"] = df1.ScreenResolution.apply(lambda x: float(x.split("x")[1][0:4]))
print(df1.HR.unique())
print(df1.VR.unique())
df1 = df1.drop("ScreenResolution", axis="columns")
print(df1.head())
df1["Cpu"] = df1.Cpu.apply(extract_ghz)
print(df1.Cpu.unique())
print(df1.info())
df1["Ram"] = df1.Ram.apply(lambda x: float(x.split("GB")[0]))
df1["SSD"] = df1.Memory.apply(extract_ssd)
df1["HDD"] = df1.Memory.apply(extract_hdd)
df1 = df1.drop("Memory", axis="columns")
print(df1.SSD.unique())
print(df1.HDD.unique())
print(df1.info())
print(df1[df1.HDD == 0])
print(df1.Gpu.unique())
df1["Gpu"] = df1.Gpu.apply(classify_gpu)
dummies = pd.get_dummies(df1.Gpu, drop_first=True).astype(int)
df1= pd.concat([df1, dummies], axis="columns")
df1=df1.drop("Gpu", axis="columns")
print(df1.OpSys.unique())
dummies = pd.get_dummies(df1.OpSys, drop_first=True).astype(int)
df1= pd.concat([df1, dummies], axis="columns")
df1=df1.drop("OpSys", axis="columns")
df1["Weight"] = df1.Weight.apply(lambda x: float(x.split("kg")[0]))
df1 = df1.fillna(0)
print(df1.info())
print(df1[["Inches","Cpu","Ram","Weight","Price_euros","HR", "VR", "SSD", "HDD"]].describe())
print(df1[df1.Price_euros > 4000])
df1["TopForGen"] = df1.Price_euros.apply(lambda x: 1 if x>4000 else 0)
print(df1.head())
print(df1[df1.Price_euros > 4000])
df1.to_csv("clean_prices.csv", index=False)
