#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:45:07 2021

@author: beyzagurler
"""
#This script will create bins for the years, decades, and counties for fires in CA

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#opening fires_by_county 
fires_by_county= pd.read_csv("fires_by_counties.csv")

#grouping by decades

fires_by_county["decade_bins"]= fires_by_county["YEAR_"].round(-1)

sorted_decades=fires_by_county["decade_bins"].value_counts().sort_index()

sorted_decades=pd.DataFrame(sorted_decades)

#renaming the columns in sorted_decades

better_names.set_index= DO I NEED TO HAVE THE INDEXES DIFFERENT FROM DECADES??

better_names=sorted_decades.rename(columns={"decade_bins": "Number of Fires"})

sorted_by_decades= better_names 


print("\nFire Count for each decade:","\n", sorted_by_decades)

#sorted_by_decades= sns.jointplot(sorted_decades, y="Index", x='Number of Fires', kind='hex')
                                                                       
#%%
#little figure!
(fig, ax1) = plt.subplots(dpi=300)
fig.suptitle("Amount of Wildfires in California by Decade")
sorted_by_decades.plot(ax=ax1)
ax1.set_ylabel("Number of Fires")
ax1.set_xlabel("Decades")
fig.tight_layout()
fig.savefig("Wildfires_By_Decade.png")

#%%

fig, ax1= plt.subplots()
sns.histplot(data=sorted_by_decades, x="Number of Fires", stat="density", ax=ax1)
sns.kdeplot(data=sorted_by_decades, x="Number of Fires", shade=True, ax=ax1)
ax1.set_xlabel("This is the X")
fig.tight_layout()
fig.savefig("histFires_by_decade.png", dpi=300)
#%%

