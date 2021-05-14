#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:45:07 2021

@author: beyzagurler
"""
#Run me third!
#This script will create bins for the decades for fires in CA

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

better_names=sorted_decades.rename(columns={"decade_bins": "Number of Fires"})

better_names=better_names.reset_index()

sorted_by_decades= better_names 


print("\nFire Count for each decade:","\n", sorted_by_decades)


#%%

fig, ax1= plt.subplots()
sns.barplot(x="index", y="Number of Fires", data=sorted_by_decades.reset_index(), ax=ax1)
plt.ylabel('Number of Fires')
plt.xlabel('Decades')
plt.xticks(rotation=25)
plt.title('Fires per Decade')
fig.savefig('Fires_over_decades.png', dpi=300)

