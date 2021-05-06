#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:45:07 2021

@author: beyzagurler
"""
#This script will create bins for the years, decades, and counties for fires in CA

import pandas as pd

#open fires dataframe
fires= pd.read_csv("fires.csv")


#breaking up the dates

pd.to_datetime(fires["ALARM_DATE"])
print(fires["ALARM_DATE"])

#fires["year"]= 

#fires["month"]=

#fires["day"]=

