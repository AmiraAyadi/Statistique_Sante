#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 10:31:56 2018

@author: Amira AYADI
"""

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('couples.csv', sep=',', na_values='.', decimal='.',
                   encoding='utf-8')

df = pd.concat([
        data.select_dtypes([], ['object']),
        data.select_dtypes(['object']).apply(pd.Series.astype, dtype='category')
        ], axis=1).reindex_axis(data.columns, axis=1)

df.select_dtypes(['category']).describe()

data["dconsultation"] = pd.to_datetime(data.dconsultation)
data["dconception"] = pd.to_datetime(data.dconsultation)
data["ddn"] = pd.to_datetime(data.ddn)


# graph bivarié 
import random as rnd
import seaborn as sns
import matplotlib.pyplot as plt

#femmme
#patho
grid = sns.FacetGrid(data, size=5, aspect=1.6)
grid.map(sns.pointplot, 'patho_f', 'enfant', palette='deep')
grid.add_legend()

#ct_f
grid = sns.FacetGrid(data, size=3, aspect=1.6)
grid.map(sns.pointplot, 'ct_f', 'enfant', palette='deep')
grid.add_legend()

#bh_f
grid = sns.FacetGrid(data, size=3, aspect=1.6)
grid.map(sns.pointplot, 'bh_f', 'enfant', palette='deep')
grid.add_legend()

#diplome_f
grid = sns.FacetGrid(data, size=3, aspect=1.6)
grid.map(sns.pointplot, 'diplome_f', 'enfant', palette='deep')
grid.add_legend()

#tranche_age_f
grid = sns.FacetGrid(data, size=3, aspect=1.6)
grid.map(sns.pointplot, 'tranche_age_f', 'enfant', palette='deep')
grid.add_legend()

#homme
#patho
grid = sns.FacetGrid(data, size=5, aspect=1.6)
grid.map(sns.pointplot, 'patho_h', 'enfant', palette='deep')
grid.add_legend()

#cryptorchidie
grid = sns.FacetGrid(data, size=3, aspect=1.6)
grid.map(sns.pointplot, 'cryptorchidie', 'enfant', palette='deep')
grid.add_legend()

#spermo
grid = sns.FacetGrid(data, size=3, aspect=1.6)
grid.map(sns.pointplot, 'spermo', 'enfant', palette='deep')
grid.add_legend()

#diplome_h
grid = sns.FacetGrid(data, size=3, aspect=1.6)
grid.map(sns.pointplot, 'diplome_h', 'enfant', palette='deep')
grid.add_legend()

#tranche_bmi_h
grid = sns.FacetGrid(data, size=3, aspect=1.6)
grid.map(sns.pointplot, 'tranche_bmi_h', 'enfant', palette='deep')
grid.add_legend()

#tranche_age_f
grid = sns.FacetGrid(data, size=3, aspect=1.6)
grid.map(sns.pointplot, 'tranche_age_f', 'enfant', palette='deep')
grid.add_legend()

#les deux

#traitement
grid = sns.FacetGrid(data, size=3, aspect=1.6)
grid.map(sns.pointplot, 'traitement', 'enfant', palette='deep')
grid.add_legend()

#tranche_duree_infertilite
grid = sns.FacetGrid(data, size=3, aspect=1.6)
grid.map(sns.pointplot, 'tranche_duree_infertilite', 'enfant', palette='deep')
grid.add_legend()

#fecondite
grid = sns.FacetGrid(data, size=3, aspect=1.6)
grid.map(sns.pointplot, 'fecondite', 'enfant', palette='deep')
grid.add_legend()

# multi-varié 

# diplome h 

grid = sns.FacetGrid(data, row='traitement', size=2.2, aspect=1.6)
grid.map(sns.pointplot, 'diplome_h', 'enfant', palette='deep')
grid.add_legend()

# diplome f

grid = sns.FacetGrid(data, row='traitement', size=2.2, aspect=1.6)
grid.map(sns.pointplot, 'diplome_f', 'enfant', palette='deep')
grid.add_legend()

# patho 

grid = sns.FacetGrid(data, row='traitement', size=5, aspect=1.6)
grid.map(sns.pointplot, 'patho_f', 'enfant', palette='deep')
grid.add_legend()

# chi 2 - pour chaque variable 
# traitement

from scipy.stats import chi2_contingency

# Table of traitement vs enfant class
col = ["traitement", "fecondite", "patho_f", "ct_f", "bh_f", "diplome_f",
        "cryptorchidie", "spermo"]
for i in col:
    table = pd.crosstab(index=data["enfant"], 
                                columns=data[i])
    res = chi2_contingency(table)
    chi2, p, dof, expected = chi2_contingency(table)
    print(p)
