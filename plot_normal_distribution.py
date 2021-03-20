from scipy.stats import norm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

x = np.arange(-4, 4.001, 0.01)

gauss_distr = pd.DataFrame({
    'x': x,
    'y': norm.pdf(x)})

sns.lineplot(x='x',
             y='y',
             data=gauss_distr)

plt.show()
