### Introduction
This is a small project created to learn how to build an ML model and how to deploy it including creating a web application for it. 
This model tries to predict the prices of computers according to just basic characteristics using a random forest regression model (had the best performance with about 80% accuracy)

### Problems
The model can only predict prices with 80% accuracy because many details were left out.
For example, instead of having every type of CPU and GPU possible, it just evaluates based on the brand of the GPU and GHz of the CPU.
Thus it doesn't grab a truly accurate picture of the computer specs, this was done because the dataset is very limited and having 100+ dimensions (one for every type of CPU and GPU) was not practical as the dataset just has 1300 entries.
Additionally, the predictor aims to be simple to use, the cost of these 2 things, is that the accuracy is not perfect but it is decent

### Improval
If the dataset was larger, all of these different cpus and gpus could have been treated as dimensions and the result would be much more accurate.
If the dataset also contained the year of purchase it will also help the dataset as hardware becomes more powerful the more time that passes.
Also, simple algorithms like simple regression or random forest are just basic algorithms and even if they have huge datasets with many dimensions, they could still lack accuracy.

### Try it out
The code is split between a file used to clean the data, train the model and evaluate the model which is not needed to run the application and the app file where all the necessary components to run the application are. 

1- copy the repository or fork the repo 

2- make sure you have Python 3.12 installed and install all the requirements in requirements.txt 

3- run the file ServerApp.py (App --> Server --> ServerApp.py) 

4- open the app.html file (App --> Client --> app.html) 

OR you can try the web version using this link:

