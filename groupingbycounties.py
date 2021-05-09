#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 00:05:31 2021

@author: beyzagurler
"""
import pandas as pd

#opening fire, county, and population data
huge_fire_data= pd.read_csv("Fire_Data.csv")

#please=huge_fire_data.groupby(["COUNTY"])

#please["Num_fires"]=please.count()

#groupby_county=pd.DataFrame(please)

#%%
#for county in groupby_county:
 #   print(groupby_county.sum())

#huge_fire_data["county_bins"]= huge_fire_data.groupby("COUNTY", axis=0)

#groupby_county=huge_fire_data["county_bins"].value_counts().sort_index()

#groupby_county=pd.DataFrame(groupby_county)

#LA_county= huge_fire_data.query(["COUNTY"])


LA=huge_fire_data.query("COUNTY=='001'")
print(LA)