# -*- coding: utf-8 -*-
"""week 10 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PG_8c6EPnZ1qeSpfM-Sf2nvr5AKVN5PO
"""

import pandas as pd
import numpy as np

# Sample data
np.random.seed(0)
data = pd.DataFrame({
    'Game ID': range(1, 31),
    'First Move': np.random.choice(['corner', 'center', 'middle'], 30),
    'First Player Outcome': np.random.choice(['Win', 'Loss', 'Draw'], 30),
    'Total Moves': np.random.randint(3, 10, 30),
    'Game Duration': np.random.randint(30, 180, 30)
})

# Step 2: Descriptive Statistics
print(data.describe())
print(data['First Player Outcome'].value_counts())

# Step 3: Grouping and Aggregation
grouped_data = data.groupby('First Move')['First Player Outcome'].value_counts().unstack()
print(grouped_data)

# Step 4: Data Visualization
grouped_data.plot(kind='bar', stacked=True)
plt.title('Outcomes by First Move')
plt.xlabel('First Move')
plt.ylabel('Count')
plt.show()