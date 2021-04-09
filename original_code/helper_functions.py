#!/usr/bin/env python
# coding: utf-8

#use this file to write up helper functions
import numpy as np
import pandas as pd


def getDfSummary(input_data):
    "From our 1001 first HW, gets a slightly more robust initial EDA compared to pd.decribe()"
    #start by getting the stats that describe already gives us, then transpose this (gets us mean, max, min, std, 25%, 50%, 75%)
    output_data = input_data.describe()
    output_data = output_data.transpose()
    
    #to get distinct counts, first use the nunique function
    #turn this series into a new data frame and merge it with the one from above
    uniques = input_data.nunique(0)
    ph = uniques.to_frame(name='number_distinct')
    output_data = pd.merge(output_data,ph,left_index=True,right_index=True)
        
    #using the count total, get the total number of rows and take this difference to get number_nan
    numrows = len(input_data.index)
    output_data['number_nan'] = output_data['count'].apply(lambda x: numrows - x) 

    return output_data

