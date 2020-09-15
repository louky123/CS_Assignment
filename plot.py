import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df=pd.read_csv('istherecorrelation.csv', sep=';')

years = df.iloc[:, 0]
wo = df.iloc[:,1]
beer = df.iloc[:,2]


plt.figure(dpi=300)
plt.scatter(wo, beer)
plt.xlabel("WO x1000")
plt.ylabel("Beer consumtion x1000 hectoliter")
plt.savefig(r'C:\Users\Gebruiker\source\repos\CS_Assignment\corr1.png', dpi=300)
plt.show()
