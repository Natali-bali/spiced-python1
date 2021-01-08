import os
import pandas as pd
import matplotlib.pyplot as plt
if os.path.exists("datapoints.csv"):
    data = pd.read_csv("datapoints.csv")
else:
    print("File does not exist")

dataY = data['y'].copy()
dataX = data['x'].copy()

def sum1(x):
    sum = 0
    for i in x:
        sum = sum + i
    return sum/len(x)
def sum2(x,y):
    sum = 0
    for i in range(len(x)):
            sum = sum + x[i]*y[i]
    return sum/len(x)
sumx = sum1(dataX)
sumy = sum1(dataY)
sumxy = sum2(dataX, dataY)
sumxx = sum2(dataX, dataX)

resultA = (sumxy-sumx*sumy)/(sumxx - sumx**2)
resultB = sumy - resultA*sumx
print(resultA, resultB)
