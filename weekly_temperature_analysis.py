import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dani=['Pon','Uto','Sre','Cet','Pet','Sub','Ned']
temperature=[12,15,11,18,20,23,19]

temp_series=pd.Series(temperature, dani)
print(temp_series)

najtopliji_dan=temp_series.idxmax()
najhladniji_dan=temp_series.idxmin()
print('Najtopliji dan:',najtopliji_dan)
print('Najhladniji dan:', najhladniji_dan)

vikend=temp_series[['Sub','Ned']]
fig,(ax1,ax2)=plt.subplots(1,2)
ax1.plot(temp_series,'red')
ax2.plot(vikend,'pink')
ax1.set_title('Temperatura tokom nedelje')
ax2.set_title('Vikend')

ax1.set_xlabel('Dan')
ax1.set_ylabel('Temperatura')
ax2.set_xlabel('Dan')
ax2.set_ylabel('Temperatura')

plt.show()