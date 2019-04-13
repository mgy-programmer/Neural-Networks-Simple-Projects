# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 20:52:31 2019

@author: PC
"""
import numpy as np

inputValue = np.array([[0,0,1], [1,1,1], [1,0,1]])
realValue = np.array([[0,1,1]]).T

weight = np.array([[1.0,1.0,1.0]]).T
i=0
for repeat in range(100000):
    i+=1
    print("Step {0}".format(i))
    cell_weight = np.dot(inputValue,weight)
    print("Cell Weight:",cell_weight)
    predict = 1/(1+np.exp(-cell_weight))
    print("Predict:",predict)
    error = realValue-predict
    weight += np.dot(inputValue.T,(error*predict*(1-predict)))
    print("New Weight:",weight)
    error_mean = str(np.mean(np.abs(error)))
    print("Error Mean:", error_mean)
    
result = 1/(1+np.exp(-(np.dot(np.array([1,0,0]),weight))))
print("Result:",result)
