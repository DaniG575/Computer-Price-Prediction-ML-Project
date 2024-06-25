import pandas as pd
from sklearn import linear_model as lm
from matplotlib import pyplot as plt
import seaborn as snsfrom
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import pickle

df = pd.read_csv("./ModelCreation/InfData/clean_prices.csv")
x = df.drop("Price_euros", axis="columns")
y = df.Price_euros
xtrain,xeval,ytrain,yeval = train_test_split(x,y,test_size=0.2,random_state=10)
model = lm.LinearRegression()
model.fit(xtrain,ytrain)
print(model.score(xeval,yeval))

# The model performs poorly so I perform hyperparameter tunning to find out
# the best model with the best params

def HyperParameterTune(model, input, target, splits, params):
	clf = GridSearchCV(model, params, cv=splits, return_train_score=False)
	clf.fit(input, target)
	df = pd.DataFrame(clf.cv_results_)
	df = pd.concat([df.filter(regex="^param"), df["mean_test_score"]])
	bp = clf.best_params_
	bs = clf.best_score_
	return bs,bp

def EvalModelsParams(input, target, splits):
	scores = []
	model_params = {
		'linear': {
			'model': lm.LinearRegression(),
			'params' : {
			}  
		},
		'random_forest': {
			'model': RandomForestRegressor(),
			'params' : {
				'n_estimators': [5,10,50,100]
			}
		},
		'lasso': {
			'model': Lasso(max_iter=10000),
			'params' : {
				'selection': ["random", "cyclic"],
				'alpha': [0.1,0.2,0.3,0.5,1,2,3,5]
			}
		}
	}
	for model_name, params in model_params.items():
		best_score, best_params = HyperParameterTune(params["model"], input, target, splits, params["params"] )
		scores.append({
			'model': model_name,
			'best_score': best_score,
			'best_params': best_params
		})
	df = pd.DataFrame(scores,columns=['model','best_score','best_params'])
	return df
print(EvalModelsParams(x,y,5))
scaled = StandardScaler().fit_transform(x)
print(EvalModelsParams(scaled,y,5))

bestModel = RandomForestRegressor(n_estimators=100)
bestModel.fit(x,y)
with open("./ModelCreation/Models/model_pickle",'wb') as RegModel:
    pickle.dump(bestModel,RegModel)

RegressionModel = lm.LinearRegression()
RegressionModel.fit(x,y)
with open("./ModelCreation/Models/model_pickle",'wb') as RegModel:
    pickle.dump(RegressionModel,RegModel)