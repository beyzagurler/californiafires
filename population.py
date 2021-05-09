#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:45:31 2021

@author: beyzagurler
"""

#trying to overlay the population density on top of all this good stuff!!! probs should be run second
import pandas as pd
import requests 


api= "https://api.census.gov/data/2018/acs/acs5"

for_clause= "county:*"
in_clause="state:06"
key_value="4e12f01c58fe188d86f91f29ee9fdfbf92bfe34c"

payload={"get":["B01001_001E"], "for": for_clause, "in":in_clause, "key": key_value}
response= requests.get(api, payload)
row_list=response.json()
colnames= row_list[0]
datarows= row_list[1:]

population= pd.DataFrame(columns= colnames, data=datarows)
rename= population.rename(columns={"B01001_001E": "Population", "county": "COUNTY"})
population=rename
population['COUNTY']=population['COUNTY'].astype(str)
population.to_csv("population.csv")


#%%
#merging population onto the fires_by_county dataframe but first, lets open our friend fire_by_county
fires_by_county= pd.read_csv("fires_by_counties.csv")

huge_fire_data=fires_by_county.merge(population, on='COUNTY', how='left', validate='m:1', indicator=True)

print( huge_fire_data['_merge'].value_counts() )

#dropping extra columns
huge_fire_data = huge_fire_data.drop(['_merge',"state","Unnamed: 0"], axis='columns')
#%%
#saving our mega data file to csv juuuust in case
huge_fire_data.to_csv("Fire_Data.csv")
