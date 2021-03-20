import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import logistic


x = np.arange(-10, 10.1, 0.1)


logistic_dist = pd.DataFrame({"x": x,
                              "log_cdf": logistic.cdf(x),
                              "log_cdf_man": 1 / (1 + np.exp(-x))})

#sigmoid plotting
sns.lineplot(x='x',
             y='log_cdf',
             data=logistic_dist)


plt.show()
