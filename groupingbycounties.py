#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 00:05:31 2021

@author: beyzagurler
"""
import pandas as pd

#opening fire, county, and population data
huge_fire_data= pd.read_csv("Fire_Data.csv")

#fires in each county ever
number_by_county = huge_fire_data.groupby("COUNTY").size()



number_by_county=pd.DataFrame(number_by_county)

number_by_county['Fires']=number_by_county

#fires in each county each year
total_acres = huge_fire_data.groupby(["COUNTY","YEAR_"])["GIS_ACRES"].sum()

total_acres=pd.DataFrame(total_acres)

#ammount of acres per county in all of time 
county_tot_acres= total_acres.groupby("COUNTY").sum()
 

#%%
#Trying to get some counties that had the most acres burned

#total_acres and try to find the top ten counties with most fires and what years they were in 


#%%

top10fires=total_acres.sort_values("GIS_ACRES").iloc[-10:]

top10counties=number_by_county.sort_values("Fires").iloc[-10:]

