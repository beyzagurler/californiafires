#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:30:55 2021

@author: beyzagurler
"""

#Cleaning up the data from Fire Perimeters 

import pandas as pd

#opening California Fire Perimeters as a dataframe

fire= pd.read_csv("California_Fire_Perimeters.csv")

#renaming the missing values under containment date from 1970/01/01 to MISSING

fire["CONT_DATE"]= fire["CONT_DATE"].replace(["1970/01/01 00:00:00+00"],"MISSING")

