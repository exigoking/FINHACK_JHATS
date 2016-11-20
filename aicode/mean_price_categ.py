# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 17:18:44 2016

@author: Hazem
"""
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random

def avg_price_per_categ(user_id = 86246, dept_num = 63):

    filename = "transactions.csv.gz"
    xl_file = pd.read_csv(filename, nrows = 20000 )

    xl_file = xl_file[xl_file['id'] == user_id]
    xl_file = xl_file[xl_file['dept'] == dept_num]
    #xl_file = pd.read_csv("sample.csv")
    
    xl_file_perdept_mean = xl_file[['dept','purchaseamount']].groupby(['dept']).mean().reset_index()
    xl_file_perdept_std = xl_file[['dept','purchaseamount']].groupby(['dept']).std(ddof = 0).reset_index()
    
    return xl_file_perdept_mean.iloc[0][1],xl_file_perdept_std.iloc[0][1]
