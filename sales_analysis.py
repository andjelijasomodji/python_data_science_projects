import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

meseci = ['Jan', 'Feb', 'Mar', 'Apr', 'Maj', 'Jun']
prodaja = [150, 200, 180, 220, 310, 275]
cena = [10, 12, 11, 13, 15, 14]

df=pd.DataFrame({'meseci': meseci,'prodaja': prodaja,'cena': cena})
df['prihod']=df['prodaja']*df['cena']
najveci_prihod_mesec=df.loc[df['prihod'].idxmax(), 'meseci']
print(df)
print('Mesec sa najvecim prihodom:', najveci_prihod_mesec)

df=df.set_index('meseci')
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(12,5))
ax1.plot(df['prodaja'],'orange')
ax1.set_title('Prodaja')
ax2.plot(df['prihod'],'purple')
ax2.set_title('Prihod')
ax1.set_xlabel('Mesec')
ax1.set_ylabel('Prodaja')

ax2.set_xlabel('Mesec')
ax2.set_ylabel('Prihod')
plt.show()


