#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 10:20:02 2018

@author: AntoineP
"""

import pandas as pd

data = pd.read_csv('couples.csv', sep = ',',na_values = '.', decimal = '.', encoding =  'utf-8')
