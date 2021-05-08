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
rename= population.rename(columns={"B01001_001E": "Population", "county": "County"})
population=rename
population.index=population["county"]
population.to_csv("population.csv")

#pop density= number of ppl/land area

#%%
#merging population onto the fires_by_county dataframe


join on fips codes 