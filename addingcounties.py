#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:30:55 2021

@author: beyzagurler
"""

#Cleaning up the data from Fire Perimeters and merging counties 

import pandas as pd

#opening California Fire Perimeters as a dataframe

fires= pd.read_csv("California_Fire_Perimeters.csv")

#renaming the missing values under containment date from 1970/01/01 to MISSING

fires["CONT_DATE"]= fires["CONT_DATE"].replace(["1970/01/01 00:00:00+00"],"MISSING")

#getting rid of the timestamps

fires["CONT_DATE"]= fires["CONT_DATE"].str.rstrip(" 00:00:00+00")  

fires["ALARM_DATE"]= fires["ALARM_DATE"].str.rstrip(" 00:00:00+00")



#adding counties 


#saving the dataframe "fires" as a csv file for other scripts to use
fires.to_csv("fires.csv")