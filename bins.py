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
import seaborn as sns

#opening fires_by_county 
fires_by_county= pd.read_csv("fires_by_counties.csv")

#grouping by decades

fires_by_county["decade_bins"]= fires_by_county["YEAR_"].round(-1)

sorted_decades=fires_by_county["decade_bins"].value_counts().sort_index()

sorted_decades=pd.DataFrame(sorted_decades)

#renaming the columns in sorted_decades
better_names=sorted_decades.rename(index={"index":"Decades"},columns={"decade_bins": "Number of Fires"})


sorted_by_decades= better_names 


print("\nFire Count for each decade:","\n", sorted_by_decades)


#decades= sns.jointplot(sorted_decades, y="index", x='columns', kind='hex')

                                     
#make a histogram at the end of this                                     
#%%
fig, ax1 = plt.subplots()
sorted_by_decades.plot()
ax1.set_ylabel("Number of Fires")
ax1.set_xlabel("Decades")
plt.title("Amount of Wildfires in California by Decade")
fig.savefig("Wildfires_By_Decade.png", dpi=300)

#%%
#sorting by counties!

