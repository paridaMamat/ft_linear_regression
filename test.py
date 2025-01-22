import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib
matplotlib.use('TkAgg')  # Use the TkAgg backend
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')
print(df.head())
x = df.iloc[:, 0].values.reshape(-1, 1)
y = df.iloc[:, 1].values.reshape(-1, 1)

reg = LinearRegression()
reg.fit(x, y)


# Access and print the intercept and slope (coefficient)
print(f"Intercept (b) = {reg.intercept_[0]}")
print(f"Slope (m) = {reg.coef_[0][0]}")

y_pred = reg.predict(x)
df['y_pred'] = y_pred


plt.scatter(x, y)
plt.plot(x, y_pred, color='red')
plt.show()

# promp_user = input('Do you want to predict a value? (y/n): ')
# while promp_user == 'y':
#     value = float(input('Enter a value: '))
#     value = np.array(value).reshape(-1, 1)
#     prediction = reg.predict(value)
#     print(f'The prediction is: {prediction}')
#     promp_user = input('Do you want to predict a value? (y/n): ')
# print('Goodbye!')