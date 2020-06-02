# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 17:13:44 2020

@author: Achyuth
"""

import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')

corona_dataset_csv = pd.read_csv('covid19_Confirmed_dataset.csv')
corona_dataset_csv.drop(['Lat','Long'],axis=1,inplace=True)
corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()

corona_dataset_aggregated.loc['China'].plot()
corona_dataset_aggregated.loc['Italy'].plot()
corona_dataset_aggregated.loc['Spain'].plot()
plt.legend()

countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for country in countries :
    max_infection_rates.append(corona_dataset_aggregated.loc[country].diff().max())
corona_dataset_aggregated['max infection rate'] = max_infection_rates

corona_data = pd.DataFrame(corona_dataset_aggregated['max infection rate'])

world_happiness_report = pd.read_csv("worldwide_happiness_report.csv")

columns_to_dropped = ['Overall rank','Score','Generosity','Perceptions of corruption']
world_happiness_report.drop(columns_to_dropped,axis=1 , inplace=True)

world_happiness_report.set_index(['Country or region'],inplace=True)

data = world_happiness_report.join(corona_data).copy()

data.corr()

x = data['GDP per capita']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))

sns.regplot(x,np.log(y))

x = data['Social support']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))

sns.regplot(x,np.log(y))


x = data['Healthy life expectancy']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))

sns.regplot(x,np.log(y))

x = data['Freedom to make life choices']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))


sns.regplot(x,np.log(y))


