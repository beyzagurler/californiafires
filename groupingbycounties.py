#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 00:05:31 2021

@author: beyzagurler
"""

#Run me last!

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#opening fire, county, and population data
huge_fire_data= pd.read_csv("Fire_Data.csv")
population=pd.read_csv("Population.csv", dtype={"COUNTY": str})

#fires in each county ever
number_by_county = huge_fire_data.groupby("COUNTY").size()


number_by_county.name="Fires"

number_by_county=number_by_county.to_frame()

number_by_county=number_by_county.reset_index()

#merging the population by county to the number of fires per county
number_by_county=number_by_county.merge(population, on="COUNTY", how="outer", indicator=True)

#fires in each county each year
total_acres = huge_fire_data.groupby(["COUNTY","YEAR_"])["GIS_ACRES"].sum()

total_acres=pd.DataFrame(total_acres)

#acres TOTAL burned per year
acres_burned_yearly=huge_fire_data.groupby("YEAR_")["GIS_ACRES"].sum()

#ammount of acres per county in all of time 
county_tot_acres= total_acres.groupby("COUNTY").sum()

#cleaning up some columns
number_by_county= number_by_county.drop(["Unnamed: 0", "_merge", "state"], axis=1)


#%%
#Seeing when the top 15 fires occured 
top15fires=total_acres.sort_values("GIS_ACRES").iloc[-15:]
print("\nTop 15 fires in California:","\n",top15fires)

#seeing the counties that have the most amount of fires
top10counties=number_by_county.sort_values("Fires").iloc[-10:]
print("\nTop 10 counties with the most amount of fires:","\n" ,top10counties)

#%%
#plotting the worst fires ever
fig, ax1= plt.subplots()
sns.barplot(x="YEAR_", y="GIS_ACRES", data=top15fires.reset_index(), ax=ax1)
plt.ylabel('Acres Burned')
plt.xlabel('Years')
plt.title('Worst Fires')
fig.savefig('Worst_fires.png', dpi=300)


#%%
#plotting acres burned over all the years
fig, ax1= plt.subplots()
sns.barplot(x="YEAR_", y="GIS_ACRES", data=acres_burned_yearly.reset_index(), ax=ax1)
plt.ylabel('Acres Burned')
plt.xlabel('Years')
plt.xticks(rotation=90, fontsize=3.5)
plt.title('Acres Burned per Year')
fig.savefig('Acres_over_years.png', dpi=300)


#%%
#plotting the amount of historical fires for population in counties 
fires_pop=sns.scatterplot(data = number_by_county , x = "Fires", y = "Population")
fires_pop.set_title("Amount of Historical Fires by population in counties")
plt.savefig("population_counties.png")

