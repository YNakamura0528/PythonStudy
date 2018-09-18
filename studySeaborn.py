import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

arr = np.random.randn(10000).reshape((5000,2))
df = pd.DataFrame(arr, columns = ["a", "b"])

sns.kdeplot(df["a"], df["b"])
plt.show()
