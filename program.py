import os
import pandas as pd
import matplotlib.pyplot as plt
if os.path.exists("datapoints.csv"):
    data = pd.read_csv("datapoints.csv")
else:
    print("File does not exist")
dataY = data['y'].copy()
dataX = data['x'].copy()
plt.scatter(dataX, dataY)

a = 10
b = 0
# function to create a slope y = a*x+b returns array of Y
def trY(dataX, a, b):
    trueY=[]
    for x in dataX:
        trueY.append(a*x + b)
    return trueY

# function to calculate MSE returns number
def mse(dataX, dataY, a, b):
    result = 0
    trueY = trY(dataX, a, b)
    n = len(dataX)
    for i in range(n):
        result = result + (dataY[i] - trueY[i])**2
    result = result/n
    return result

# function returns number best value of b in range [0:300] with step 0.01
def findMSEB(dataX, dataY, a, b):
    res = {}
    resMSEB = 0
    bestB = 0
    for i in range(300):
        resMSEB = mse(dataX, dataY, a, b)
        res[resMSEB] = b
        b = b + 0.01
    bestB = res[min(res)]
    return bestB
# function returns dict with key = resultMSE and value of [a,bestB]
def findMSE(dataX, dataY, a, b):
    res = {}
    resMSE = 0
    bestB = 0
    for i in range(100):
        bestB = findMSEB(dataX, dataY, a, b)
        resMSE = mse(dataX, dataY, a, bestB)
        res[resMSE] = [a, bestB]
        a = a - 0.1
    return res
listMSE = findMSE(dataX, dataY, a, b)
result = listMSE[min(listMSE)]
print(result)
plt.scatter(dataX, trY(dataX, result[0], result[1]))
plt.show()

"""
this algorithm is not the best solution,
because we have to set up the
range and step for a and b, iterate through the loop
so many times etc. The results still aproximate
and to get better result we have to decrease the step.
To check my results i used another formula in check.py
which gives us a and b
"""
