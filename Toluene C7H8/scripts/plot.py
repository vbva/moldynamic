import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('dense.xvg', sep='\s+', header=None, names=['time','dencity'], usecols=[0, 1])


# Convert 'step' and 'energy' columns to numpy arrays
step = df['time'].values
energy = df['dencity'].values

plt.plot(step, energy)
plt.xlabel('time')
plt.ylabel('p')
plt.title('dencity')
plt.grid(True)
plt.show()
