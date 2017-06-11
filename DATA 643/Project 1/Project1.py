# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 22:00:25 2017

@author: Latif Masud
"""

import numpy as np
import numpy.ma as ma

from math import sqrt
from random import randint, sample

"""
Load your data into (for example) an R or pandas dataframe, a Python dictionary or list of lists, (or
another data structure of your choosing). From there, create a user-item matrix.
"""

def rmse (predictions, targets):
    return sqrt(((predictions - targets) ** 2).mean(axis=None))


if __name__ == '__main__':
    ratings = [[1,0,2,2,1],
               [0,4,5,4,5],
               [3,2,0,2,3],
               [1,5,1,4,0],
               [2,3,2,0,2]]
    
    missing = np.array([[1,0,1,1,1],
                    [0,1,1,1,1],
                    [1,1,0,1,1],
                    [1,1,1,1,0],
                    [1,1,1,0,1]])
    
    #Break your ratings into separate training and test datasets.
    mask_test = np.array([[0,1,1,1,1],
                          [1,0,1,1,1],
                          [1,1,1,0,1],
                          [1,1,0,1,1],
                          [1,1,1,1,0]])
 
    mask_training = np.logical_not(np.logical_and(mask_test, missing))
    
    test = ma.array(ratings, mask = mask_test)
    training = ma.array(ratings, mask = mask_training)

    #Using your training data, calculate the raw average (mean) rating for every user-item combination.
    print "Training Mean: ", training.mean()
    
    #Calculate the RMSE for raw average for both your training data and your test data.
    mean_matrix = np.full((5,5), training.mean())
    
    rmse_training = rmse (training, mean_matrix)
    rmse_test = rmse (test, mean_matrix)
    
    print "-----------------------------------------------"
    print "RMSE Values"
    print "Test: ", rmse_test, " Training: ", rmse_training
    print "-----------------------------------------------"

    #Using your training data, calculate the bias for each user and each item.
    user_bias = training.mean(axis=1) - training.mean()
    sample_bias = training.mean(axis=0) - training.mean()
    
    print "Bias Values"
    print "User Bias: ", user_bias
    print "Sample Bias: ", sample_bias
    print "-----------------------------------------------"
    
  
    #From the raw average, and the appropriate user and item biases, calculate the baseline predictors
    #for every user-item combination.
    baseline = mean_matrix
    
    for n in range(0, user_bias.shape[0]):
        for m in range(0, sample_bias.shape[0]):
            baseline[n][m] = baseline[n][m] + user_bias[n] + sample_bias[m]
            
    print baseline
    print "-----------------------------------------------"
 
    #Calculate the RMSE for the baseline predictors for both your training data and your test data.
    training_rmse = rmse(training, baseline)
    test_rmse = rmse(test, baseline)

    print "Baseline RMSE"
    print "Training RMSE: ", training_rmse
    print "Test RMSE: ", test_rmse
    print "-----------------------------------------------"
    
    #Summarize your results