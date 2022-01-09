%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from google.colab import drive 
drive.mount('/content/gdrive')


PC=pd.read_csv('gdrive/My Drive/PhillipsCurve.csv')
PC=PC[~PC.isin([np.nan, np.inf, -np.inf]).any(1)]

PC.head(20)

x = PC['CPI']
y = PC['Unemployment']

model = LinearRegression(fit_intercept=True)

model.fit(x[:, np.newaxis], y)

xfit = np.linspace(0, 10, 1000)
yfit = model.predict(xfit[:, np.newaxis])

plt.xlabel('Unemployment')
plt.ylabel('Inflation')

plt.scatter(x, y)
plt.plot(xfit, yfit);
