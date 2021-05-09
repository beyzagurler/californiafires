#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 00:05:31 2021

@author: beyzagurler
"""
import pandas as pd
import matplotlib as plt
import seaborn as sns

#opening fire, county, and population data
huge_fire_data= pd.read_csv("Fire_Data.csv")
population=pd.read_csv("Population.csv", dtype={"COUNTY": str})

#fires in each county ever
number_by_county = huge_fire_data.groupby("COUNTY").size()

#check why some didn't have counties, islands??-

number_by_county.name="Fires"
number_by_county=number_by_county.to_frame()

number_by_county=number_by_county.reset_index()

number_by_county=number_by_county.merge(population, on="COUNTY", how="outer", indicator=True)

#fires in each county each year
total_acres = huge_fire_data.groupby(["COUNTY","YEAR_"])["GIS_ACRES"].sum()

total_acres=pd.DataFrame(total_acres)

#do acres TOTAL burned per year
acres_burned_yearly=huge_fire_data.groupby("YEAR_")["GIS_ACRES"].sum()

#ammount of acres per county in all of time 
county_tot_acres= total_acres.groupby("COUNTY").sum()


 
#heat map of fires to see if some counties have more fires than others, HISTOGRAM OR MAP
#heat map heat map! counties with a lot of fires might be the big counties 
#are there a lot more fires in some than others, where are located, 

#COUNT FIRES IN LAST TWENTY YEARS--> scatterplot

#high pop plus high fires

#MEASURE OF FIRES BY LAND AREAS maP OF CALI TAKE ALAND VARIABLE SQ METERS  TAKE NUMBER OF FIRES/SQMETERS gives you number of fires per square meters multiple by 1MILLION Number of fires by 1m sq meters
#POP DENSITY AND FIRE DENSITY = SCATTER THAT 
#%%
heatmap_data=number_by_county[['COUNTY', "Fires"]]

fig,ax1= plt.subplots(dpi=300)
fig.suptitle("TITLE")
sns.heatmap(heatmap_data, annot=True, fmt=".0f", ax=ax1)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
fig.tight_layout()

#%%

top15fires=total_acres.sort_values("GIS_ACRES").iloc[-15:]
print(top15fires)
top10counties=number_by_county.sort_values("Fires").iloc[-10:]
print(top10counties)

#%%
#GRAPH THE WORST FIRE BY ACRE AND SEE WHEN IT WAS COMPARED TO THE OTHER ONES

fig, ax1= plt.subplots()
sns.barplot(x="YEAR_", y="GIS_ACRES", data=top15fires.reset_index(), ax=ax1)
plt.ylabel('Acres Burned')
plt.xlabel('Years')
plt.title('Worst Fires by year')
fig.savefig('WORST.png', dpi=300)


#%%

fig, ax1= plt.subplots()
sns.barplot(x="YEAR_", y="GIS_ACRES", data=acres_burned_yearly.reset_index(), ax=ax1)
plt.ylabel('Acres Burned')
plt.xlabel('Years')
plt.xticks(rotation=25)
plt.title('Acres Burned per Year')
fig.savefig('Acres over years.png', dpi=300)

#%%
fig, ax1= plt.subplots(dpi=300)
fig.suptitle("HEATMAAAAAP")
sns.heatmap(grid, annot=True, fmt=".0f", ax=ax1)
ax1.set_xlabel("Years")
ax1.set_ylabel("Acres")
fig.tight_layout()
fig.savefig("heatmap.png")

#%%


fires_by_county=pd.read_csv("fires_by_counties.csv")

#WHAT I AM TRYING T0 DO IS SEE THE FIRES IN EACH COUNTY IN THE LAST TWO DECADES AND SEE THE POPULATION TOO

last20years=huge_fire_data.sort_values("YEAR_").round(-1)
print(last20years)
#number_by_county = huge_fire_data.groupby("COUNTY").size()

#%%

fires_pop=sns.scatterplot(data = number_by_county , x = "Fires", y = "Population")
fires_pop.set_title("Amount of Historical Fires per population in counties")
fires_pop.savefig("population_counties.png",dpi=300)
