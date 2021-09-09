import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('output/input.csv')

fig, ax1 = plt.subplots(1,1,figsize = (16,6))
sns.distplot(data['age'], ax = ax1)
fig.savefig('output/descriptive.png')
