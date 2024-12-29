import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %matplotlib inline

sales = pd.read_csv(
    'sales_data.csv',
    parse_dates=['Date'])

test = sales['Customer_Age'].mean()
# sales['Customer_Age'].plot(kind='kde', figsize=(14,6))
# sales['Country'].value_counts().plot(kind='bar', figsize=(14,6))
sales['Year'].value_counts().plot(kind='pie', figsize=(6,6))
plt.savefig('foo.png', bbox_inches='tight')

print(test)