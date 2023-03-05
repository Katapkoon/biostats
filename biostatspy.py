import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('biostats.csv')
print(df.head())

sex_paint = []
for p in df['Sex']:
    if p == 1:
        sex_paint.append('#87CEEB')
    else:
        sex_paint.append('pink')

ax = plt.axes(projection='3d')
ax.scatter(df['Weight(lbs)'], df['Height(in)'], df['Age'],c = sex_paint,s = 20)
ax.set_xlabel('Weight (lb)')
ax.set_ylabel('Height (in)')
ax.set_zlabel('Age')

plt.show(block=True)