import pickle
import pandas as pd
import numpy as np
import json

__features = None
__RF = None
__RG = None

def Predict(Inches, Cpu, Ram, Weight, HR, VR, SSD, HDD, graphics, OS, gentop):
	load()
	try:
		loc_gpu = __features.index(graphics)
	except:
		loc_gpu = -1
	try:
		loc_os = __features.index(OS)
	except:
		loc_os = -1
	final = np.zeros(len(__features))
	final[0] = Inches
	final[1] = Cpu
	final[2] = Ram
	final[3] = Weight
	final[4] = HR
	final[5] = VR
	final[6] = SSD
	final[7] = HDD
	if loc_gpu >= 0:
		final[loc_gpu] = 1
	if loc_os >= 0:
		final[loc_os] = 1
	final[-1] = gentop
	final = pd.DataFrame([final], columns=__features)
	bestPredict = __RF.predict(final)
	avgPredict = __RG.predict(final)
	return bestPredict[0], avgPredict[0]

def load():
	global __RF
	global __RG
	global __features
	with open("App/Server/Required/features.json","r") as j:
		__features = json.load(j)

	with open("App/Server/Required/RFModel","rb") as j:
		__RF = pickle.load(j)
	with open("App/Server/Required/RGModel","rb") as j:
		__RG = pickle.load(j)
		
if __name__ == "__main__":
	load()
 