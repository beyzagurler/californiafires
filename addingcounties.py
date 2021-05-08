#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:30:55 2021

@author: beyzagurler
"""

#Cleaning up the data from Fire Perimeters and merging counties 

import pandas as pd
import geopandas

#opening California Fire Perimeters as a dataframe

fires= pd.read_csv("California_Fire_Perimeters.csv")

#renaming the missing values under containment date from 1970/01/01 to MISSING

fires["CONT_DATE"]= fires["CONT_DATE"].replace(["1970/01/01 00:00:00+00"],"MISSING")

#getting rid of the timestamps

fires["CONT_DATE"]= fires["CONT_DATE"].str.rstrip(" 00:00:00+00")  

fires["ALARM_DATE"]= fires["ALARM_DATE"].str.rstrip(" 00:00:00+00")

#saving the dataframe "fires" as a csv file 
fires.to_csv("fires.csv")

#%%
#open firesbycounty after spatial join in qgis
fires_by_county=geopandas.read_file("firesbycounty.gpkg")

#Drop all the columns that are not needed
fires_by_county= fires_by_county.drop(["OBJECTID","OBJECTID_2","COUNTY_ABB", "COUNTY_NUM","COUNTY_COD","FIRE_NUM","OBJECTIVE","REPORT_AC","INC_NUM","C_METHOD","AGENCY","STATE","UNIT_ID","COMMENTS","GlobalID", "ISLAND"],axis=1)

fires_by_county['COUNTY_FIP'] = fires_by_county['COUNTY_FIP'].str.zfill(1)

fires_by_county.to_csv("fires_by_counties.csv")

#pickling some stuff

#fires_by_county.to_pickle("fires_by_counties.pkl")