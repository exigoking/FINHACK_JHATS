# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 14:10:22 2016

@author: Hazem
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 14:03:28 2016

@author: 
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
import random

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel, ConstantKernel as C

from predict_budg import predict_budget
from mean_price_categ import avg_price_per_categ

def moving_avg(l,wind_size):
    mov_avg_list = []
    for i in range(len(l)):
        mov_avg_list.append(np.mean(l[max(0,i-wind_size):i+1]))
    return mov_avg_list
    
np.random.seed(1)

filename = "transactions.csv.gz"
xl_file = pd.read_csv(filename, nrows = 20000 )

list_categs = list(set(xl_file['dept']))

xl_file_perdept_mean = xl_file[['dept','purchaseamount']].groupby(['dept']).mean().reset_index()
xl_file_perdept_std = xl_file[['dept','purchaseamount']].groupby(['dept']).std(ddof = 0).reset_index()

def totalexpenses(uid=86246,bid=0):
    np.random.seed(1)
    categ_dict = {}
    for i in range(100):
        if i <10:
            categ_dict[i] = ['Winter shoes',50]
        elif i < 20:
            categ_dict[i] = ['Shoes',40]  
        elif i < 30:
            categ_dict[i] = ['Jeans',30] 
        elif i < 40:
            categ_dict[i] = ['Shirts',20] 
        elif i < 50:
            categ_dict[i] = ['Kitchen Accessories',1] 
        elif i < 60:
            categ_dict[i] = ['Garden Accessories',20] 
        elif i < 70:
            categ_dict[i] = ['Tools',1] 
        elif i < 80:
            categ_dict[i] = ['Winter Coats',100] 
        elif i < 90:
            categ_dict[i] = ['Sport Equipment',50] 
        else:
            categ_dict[i] = ['Car Accessories',70]
    
    predicted_budget = 0
    for categ in  range(100):
        categ_string = categ_dict[categ][0]
        categ_factor = categ_dict[categ][1]
        try:
            predicted_budget += predict_budget(user_id = uid, dept_num = categ)*categ_factor
        except:
            pass
        #print(savings,disc_value)
    curr_budget = np.random.uniform(0.2*predicted_budget, 1.2*predicted_budget)
    return round(curr_budget)

#generate data set of offers for each category
#Beacon IDs --> list of stores --> list of promotions
def generate_data():
    mall ={}
    np.random.seed(1)
    n_stores = 5
    no_offers = 3
    beaconIDs=['1','2','3','4']
    for j in range(len(beaconIDs)):
        stores=range(n_stores)
        mall[j]={}
        for  i in stores:
            list_categs = np.random.choice(list(xl_file_perdept_std['dept']),no_offers,replace=False)
            discount = round(np.random.uniform(0.2, 0.9),2)
            mall[j][i] = {categ: (round(discount*1.2*xl_file_perdept_mean[xl_file_perdept_mean['dept'] == categ]['purchaseamount'].item(),2),1-discount) for categ in list_categs} # Beacon j and store i list of offers
    return mall

def list_of_categs(uid=86246,bid=0):
    categ_dict = {}
    for i in range(100):
        if i <10:
            categ_dict[i] = ['Winter shoes',50]
        elif i < 20:
            categ_dict[i] = ['Shoes',40]  
        elif i < 30:
            categ_dict[i] = ['Jeans',30] 
        elif i < 40:
            categ_dict[i] = ['Shirts',20] 
        elif i < 50:
            categ_dict[i] = ['Kitchen Accessories',1] 
        elif i < 60:
            categ_dict[i] = ['Garden Accessories',20] 
        elif i < 70:
            categ_dict[i] = ['Tools',1] 
        elif i < 80:
            categ_dict[i] = ['Winter Coats',100] 
        elif i < 90:
            categ_dict[i] = ['Sport Equipment',50] 
        else:
            categ_dict[i] = ['Car Accessories',70]

    return list(set(([x[0] for x in categ_dict.values()])))

def wrapper(command='Hi'):
    categ_dict = {}
    for i in range(100):
        if i <10:
            categ_dict[i] = ['Winter shoes',50]
        elif i < 20:
            categ_dict[i] = ['Shoes',40]  
        elif i < 30:
            categ_dict[i] = ['Jeans',30] 
        elif i < 40:
            categ_dict[i] = ['Shirts',20] 
        elif i < 50:
            categ_dict[i] = ['Kitchen Accessories',1] 
        elif i < 60:
            categ_dict[i] = ['Garden Accessories',20] 
        elif i < 70:
            categ_dict[i] = ['Tools',1] 
        elif i < 80:
            categ_dict[i] = ['Winter Coats',100] 
        elif i < 90:
            categ_dict[i] = ['Sport Equipment',50] 
        else:
            categ_dict[i] = ['Car Accessories',70]
    if(command == 'Hi'): #send all the offers right away
        return ali_func() + '\n These are the other options: \n total expenses (A) \n average price per category (B)  \n budget per category (C) \n list of category (D)'
    elif(command == 'A'):
        return totalexpenses()
    elif(command[0] == 'B'):
        categ = command[1:]
        for i in range(0,100,10):
            if categ in categ_dict[i]:
                categ_factor = categ_dict[i][1]
                try:
                    return avg_price_per_categ(dept_num=i)[0]*categ_factor
                except:
                    continue
        return ("Wrong Category Choice")
    elif(command[0] == 'C'):
        categ = command[1:]
        for i in range(0,100,10):
            if categ in categ_dict[i]:
                categ_factor = categ_dict[i][1]
                try:
                    return predict_budget(dept_num = i)[0]*categ_factor
                except:
                    continue
        return ("Wrong Category Choice")
    elif(command[0] == 'D'):
        return list_of_categs()
    else:
        return 'Unrecognize command!'
    
#input: USer ID + Becon ID
def ali_func(uid=86246,bid=0):
    np.random.seed(1)
    #for loop to go over stores of a sub dictionary of mall
    categ_dict = {}
    for i in range(100):
        if i <10:
            categ_dict[i] = ['Winter shoes',50]
        elif i < 20:
            categ_dict[i] = ['Shoes',40]  
        elif i < 30:
            categ_dict[i] = ['Jeans',30] 
        elif i < 40:
            categ_dict[i] = ['Shirts',20] 
        elif i < 50:
            categ_dict[i] = ['Kitchen Accessories',1] 
        elif i < 60:
            categ_dict[i] = ['Garden Accessories',20] 
        elif i < 70:
            categ_dict[i] = ['Tools',1] 
        elif i < 80:
            categ_dict[i] = ['Winter Coats',100] 
        elif i < 90:
            categ_dict[i] = ['Sport Equipment',50] 
        else:
            categ_dict[i] = ['Car Accessories',70]

    mall = generate_data()
    for stores in mall[bid]:
        for categ in  mall[bid][stores]:
            categ_string = categ_dict[categ][0]
            categ_factor = categ_dict[categ][1]
            disc_price = mall[bid][stores][categ][0]*categ_factor
            disc_value = mall[bid][stores][categ][1]
            #what is the predicted value of user's spending on each category
            predicted_budget = predict_budget(user_id = uid, dept_num = categ)*categ_factor
            #what was the expected value of user's spending on each category
            mean_price, std_price = avg_price_per_categ(user_id = uid, dept_num = categ)
            mean_price = mean_price*categ_factor
            
            savings = (mean_price - disc_price)/mean_price
            #print(savings,disc_value)
            curr_budget = np.random.uniform(0.2*predicted_budget, 1.2*predicted_budget)
            if(predicted_budget  < disc_price + curr_budget):
                final_message = "You are over budget for " + str(categ)
            else:
                if savings >0:
                    final_message = categ_string + " is under " +  str(round(disc_value*100)) + "% discount. This is " + str(round(savings*100)) +"% cheaper that what you normally pay. You are " + str(round(predicted_budget[0] - curr_budget)) + " away from your average budget for this category."
                else:
                    final_message = categ_string + " is under " +  str(round(disc_value*100)) + "% discount. Note that this is " + str(round(savings*100)) +"% more expensive that what you normally pay. You are " + str(round(predicted_budget[0] - curr_budget)) + " dollars away from your average budget for this category."
            print(final_message)
        #break
    return final_message
    #
    
    #output: a dictionary of stores --> each store has list of offers with price+discount+
    #the budget you have for this category
    
    #How mych the costumer would save by buying accepting this offer





    


    