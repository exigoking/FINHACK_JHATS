# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 17:11:27 2016

@author: Hazem
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 09:09:36 2016

@author: Hazem
"""
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel, ConstantKernel as C

def moving_avg(l,wind_size):
    mov_avg_list = []
    for i in range(len(l)):
        mov_avg_list.append(np.mean(l[max(0,i-wind_size):i+1]))
    return mov_avg_list
    
def predict_budget(user_id = 86246, dept_num = 63):

    filename = "transactions.csv.gz"
    
    #xl_file = pd.read_csv("sample.csv")
    
    xl_file = pd.read_csv(filename, nrows = 20000 )

    xl_file = xl_file[xl_file['id'] == user_id]
    
    xl_file_perday = xl_file.groupby(['id','chain','date','category','company','brand','productsize','productmeasure','purchasequantity']).sum().reset_index()
    
    xl_file_perday['date'] = pd.to_datetime(xl_file_perday['date'])
    
    #xl_file_perday['day'] = xl_file_perday['date'].apply (lambda x: x.day)
    
    #xl_file_perday['month'] =  xl_file_perday['date'].apply (lambda x: x.month)
    
    xl_file_perday['week'] =  xl_file_perday['date'].apply (lambda x: x.week)
    
    xl_file_perday['year'] =  xl_file_perday['date'].apply(lambda x: x.year)
    
    xl_file_perday = xl_file_perday[xl_file_perday['year'] == 2012]
    
    xl_file_perweek = xl_file_perday[['dept','purchaseamount','week']].groupby(['dept','week']).sum().reset_index()
    
    
    #xl_file_perweek[xl_file_perweek["dept"]==63].plot( kind='bar', x = 'week', y='purchaseamount')
    
    kernel = 0.01*WhiteKernel() + C()*RBF(10, (1e-2, 1e2))
    gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9, normalize_y = True)
    
    X = np.atleast_2d(list(xl_file_perweek[xl_file_perweek["dept"]==dept_num]['week'])).T
    y = np.atleast_2d(list(xl_file_perweek[xl_file_perweek["dept"]==dept_num]['purchaseamount'])).T
    x = np.atleast_2d(np.append(X,max(X)+1)).T
    
    gp.fit(X, y)
    
    y_pred, sigma = gp.predict(x, return_std=True)
    
    list_users = list(set(xl_file_perday["id"]))
    
    fig = plt.figure()
    plt.plot(X, y, 'r.', markersize=10, label=u'Observations')
    plt.plot(x, y_pred, 'b-', label=u'Prediction')
    #plt.fill(np.concatenate([x, x[::-1]]),
    #         np.concatenate([y_pred - 1.9600 * sigma,
    #                        (y_pred + 1.9600 * sigma)[::-1]]),
    #         alpha=.5, fc='b', ec='None', label='95% confidence interval')
    plt.xlabel('Week Index')
    plt.ylabel('Expenses')
    plt.legend(loc='upper left')
    plt.savefig('figures/Categ'+str(dept_num)+'.jpeg')
    return y_pred[-1]
#    for user in list_users:
#        user_dataset = xl_file_perday[xl_file_perday['id']==user]
#        
#        
#        list_catgs = list(set(xl_file_perday["dept"]))
#        for catg in list_catgs:
#            per_user_per_catg_data = user_dataset[user_dataset['dept'] == catg]
#            user_dataset_permonth = per_user_per_catg_data[['purchaseamount','week']].groupby(['week']).sum().reset_index()
#            list_purchase = list(user_dataset_permonth['purchaseamount'])
#            user_dataset_permonth.head()
#            exp_expense = moving_avg(list_purchase,2)
            
    
        
    
    
        