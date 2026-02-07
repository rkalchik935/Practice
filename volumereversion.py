import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = yf.download(tickers="BTC-USD", period='max', interval='1d')

close = data["Close"]
volume = data["Volume"]

returns1 = close.pct_change()
returns2 = close / close.shift(1) - 1
log_returns = np.log(close / close.shift(1) - 1)

volume1 = abs(np.log(volume / volume.shift(1)))

def zscore(stat, window=20):
    rolling_mean = stat.rolling(window).mean()
    rolling_std = stat.rolling(window).std()
    zscore = (stat - rolling_mean) / rolling_std
    return zscore

zlog_returns = zscore(log_returns)
zvolume1 = zscore(volume1)

result = np.sqrt(zvolume1 * zlog_returns)

plt.figure(figsize=(10, 4))
plt.plot(data.index, result)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()