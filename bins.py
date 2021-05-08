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
import datetime as dt
import seaborn as sns

#opening fires_by_county 
fires_by_county= pd.read_csv("fires_by_counties.csv")

#grouping by decades

fires_by_county["decade_bins"]= fires_by_county["YEAR_"].round(-1)

sorted_decades=fires_by_county["decade_bins"].value_counts().sort_index()

print("\nFire Count for each decade:","\n", sorted_decades)

#fires_by_decade=fires_by_county["decade_bins"].groupby()

#decades= sns.jointplot(sorted_decades, y="index", x='columns', kind='hex')

#decades.savefig('fires_by_decade.png')

#print(fires_by_county["decade_bins"])

#print("\nFires per Year in California State:", len("YEAR_"))
# MAYBE I DONT NEED THIS fires_per_year=fires_by_county.groupby("YEAR_", axis="index")
# MAYBE I DONT NEED THIS print(fires_per_year)

                                     
#make a histogram at the end of this                                     


fig, ax1= plt.subplots(1)
sorted_decades.hist()
plt.ylabel('Amount of Fires')
plt.xlabel("Decades")
plt.title("Amount of Wildfires in California by Decade")


#sorting by counties!

