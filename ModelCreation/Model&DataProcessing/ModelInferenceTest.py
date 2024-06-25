import pickle
import pandas as pd
import numpy as np
import json

df = pd.read_csv("./ModelCreation/InfData/clean_prices.csv")
df1 = df.drop("Price_euros", axis="columns")
features = df1.columns.tolist()
with open('RFModel','rb') as file:
    RF = pickle.load(file)
with open('RGModel','rb') as file:
    RG = pickle.load(file)
def Predict(Inches, Cpu, Ram, Weight, HR, VR, SSD, HDD, graphics, OS, gentop):
    loc_gpu = np.where(df1.columns==graphics)[0]
    loc_os = np.where(df1.columns==OS)[0]
    final = np.zeros(len(df1.columns))
    final[0] = Inches
    final[1] = Cpu
    final[2] = Ram
    final[3] = Weight
    final[4] = HR
    final[5] = VR
    final[6] = SSD
    final[7] = HDD
    if loc_gpu.size > 0:
        final[loc_gpu] = 1
    if loc_os.size > 0:
        final[loc_os] = 1
    final[-1] = gentop
    final = pd.DataFrame([final], columns=features)
    bestPredict = RF.predict(final)
    avgPredict = RG.predict(final)
    return bestPredict[0], avgPredict[0]

print(Predict(13.3,2.3,32.0,1.37,2560.0,1600.0,128.0,0,"Intel Iris","macOS", 0))
with open("./ModelCreation/InfData/features.json","w") as j:
    j.write(json.dumps(features))