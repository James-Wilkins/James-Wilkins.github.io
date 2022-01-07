import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from google.colab import drive 
drive.mount('/content/gdrive')


df = pd.read_csv('gdrive/My Drive/FactorsPost.csv')
df=df[~df.isin([np.nan, np.inf, -np.inf]).any(1)]

x = df[['Unemployment', 'Inflation','Interest Rates','Credit Spread','Industrial Production','Consumer Sentiment']]
y = df['SP500']

regr = linear_model.LinearRegression()
regr.fit(x, y)

print(regr.coef_)
