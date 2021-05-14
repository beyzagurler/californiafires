#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 12:41:42 2021

@author: beyzagurler
"""

Getting the Data:
Perimeters for California fires can be obtained from California's State Geoportal. This data contains both the csv file and the shapefile. The link I utilized is: https://gis.data.ca.gov/datasets/CALFIRE-Forestry::california-fire-perimeters-1/data?geometry=-151.022%2C31.426%2C-87.741%2C43.578&layer=0
California County Boundaries can also be found on California's State Geoportal. This data also contains both the csv file and the shapefile. The link I used is: https://gis.data.ca.gov/datasets/8713ced9b78a4abb97dc130a691a8695_0?geometry=-150.643%2C31.049%2C-87.361%2C43.258
Population Data for each county can be obtained from the Census using the population.py script and would only need an individualized key_value.

Scripts should be run in this order:
1) addingcounties.py
2) population.py
3) bins.py
4) groupingbycounties.py

The addingcounties.py script cleans up some of the data from the California Fire Perimeters dataset. The county dataset and the fire perimeter dataset is joined via a spatial join on QGIS (called join.qgz) and this script opens up the geopackage and saves it as a csv for use in the upcoming scripts.

The population.py script obtains the population data for each county in California from the 2018 Census. It merges the population data onto our larger dataframe called fires_by_county which includes the county and fire perimeters.

The bins.py scrip starts the analysis. It groups the fires by decades and gives an output of all the fires in California for each decade. It also creates a barplot of the amount of fires by decade.

The groupingbycounties.py script continues the analysis. It gives a list of the top 15 fires in California by the amount of acres burned as well as the top 10 counties with the amount amount of fires. These show that the counties with higher populations tend to have higher amounts of fires (with the exception of Siskiyou County ("093") and Tulare County ("107")). The top 15 fires in California are almost all completely in the more recent years (2002-2018) with the exception of one fire in 1987 in Siskiyou County. The top 15 fires were determined by the amount of acres that were burned in a single incident. 