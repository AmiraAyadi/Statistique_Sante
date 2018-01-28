import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('couples.csv', sep = ',',na_values = '.', decimal = '.', encoding =  'utf-8')
data_cont=data[['age_h','bmi_h','age_f','duree_infertilite']].dropna()

#description des données
data_cont.describe(include='all')

#plt.scatter(data_cont.age_f, data_cont.enfant, c = "blue", marker = "p")
fig, (ax0, ax1, ax2,ax3) = plt.subplots(ncols=4,figsize=(18, 5))
ax0.hist(data_cont.age_h, edgecolor = 'r')
ax0.set_title('age_h')
ax1.hist(data_cont.bmi_h, edgecolor = 'r')
ax1.set_title('bmi_h')
ax2.hist(data_cont.age_f,  edgecolor = 'r')
ax2.set_title('age_f')
ax3.hist(data_cont.duree_infertilite, edgecolor = 'r')
ax3.set_title('duree_infertilite')
plt.show()

plt.boxplot([data_cont.age_h,data_cont.bmi_h,data_cont.age_f,data_cont.duree_infertilite],sym = '')
plt.gca().xaxis.set_ticklabels(['enfant', 'age_h','bmi_h','age_f','duree_infertilite'])
#plt.ylim(0, 14)
plt.title('Boîte à moustaches')
plt.show()
