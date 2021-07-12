import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Qn 1
df_main = pd.read_csv(r'D:\filename.csv', sep='#', index_col=0)
print(df_main)

# Qn 2
df_main.boxplot(column = ['Glucose'],by=['Outcome'])
plt.xlabel('Diabetic Condition')
plt.ylabel('Glucose Level')
plt.show()

# Qn 3
