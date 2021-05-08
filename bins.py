#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:45:07 2021

@author: beyzagurler
"""
#This script will create bins for the years, decades, and counties for fires in CA

import pandas as pd
import matplotlib.pyplot as plt
import geopandas

#opening fires_by_county 
fires_by_county= pd.read_csv("fires_by_county.csv")

#Creating a bin for each decade

1900-2019

1900-1910
so we wanna do [1900:1910) and then [1910,1920)
                                     
                                     