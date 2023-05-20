
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

crypto_prices_df = pd.read_csv('crypto_daily_prices.csv') 
print(crypto_prices_df)

crypto_prices_df.plot(x = 'Date', y = ['BTC-USD Price', 'ETH-USD Price', 'LTC-USD Price'], label = ['Bitcoin', 'Ethereum', 'LiteCoin'],  linewidth = 3, figsize = (14, 6));
plt.title('Crypto Prices')
plt.ylabel("Prices[$]")
plt.legend(loc = "upper left")
plt.grid()  
plt.show()

crypto_prices_df.plot(x = 'Date', title = 'Crypto Prices', subplots = True, grid = True, figsize = (15, 25))
plt.show() 

crypto_returns_df = pd.read_csv('crypto_daily_returns.csv')
print(crypto_returns_df)

X = crypto_returns_df['BTC']
Y = crypto_returns_df['ETH']
plt.figure(figsize = (7,7))
plt.scatter(X, Y)
plt.grid()
plt.show()

plt.figure(figsize = (7,7))
sns.scatterplot(x = 'BTC', y = 'ETH', data = crypto_returns_df)
plt.grid()
plt.show()

values = [60, 10, 5, 5, 10]
colors = ['r', 'g', 'y', 'b', 'm']
labels = ['XRP', 'BTC', 'LTC', 'ADA', 'ETH']
explode = [0, 0.2, 0, 0, 0]

plt.figure(figsize = (7, 7))
plt.pie(values, colors = colors, labels = labels, explode = explode)
plt.title('Allocation of Crypto')
plt.show()

mu = crypto_returns_df['ETH'].mean()
sigma = crypto_returns_df['ETH'].std()
num_bins = 30
plt.figure(figsize = (14,7))
plt.hist(crypto_returns_df['ETH'], num_bins, facecolor = 'red')
plt.title('Histogram: mu = ' + str(mu) + ' sigma = ' + str(sigma))
plt.grid()
plt.show()


plt.figure(figsize = (12, 10))
sns.heatmap(crypto_returns_df.corr(), annot = True)
plt.show()






