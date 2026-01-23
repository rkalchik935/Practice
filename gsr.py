import os
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

gold_df = yf.download("GC=F", period="max", interval="1d")
silver_df = yf.download("SI=F", period="max", interval="1d")

gold = gold_df["Close"]
silver = silver_df["Close"]

df = pd.concat([gold, silver], axis=1, keys=["Gold", "Silver"]).dropna()
df.columns = ["Gold", "Silver"]
df["GSR"] = df["Gold"] / df["Silver"]

df.to_csv("gold_silver.csv")

plt.figure(figsize=(10, 4))
plt.plot(df.index, df["GSR"])
plt.axhline(80, color="red", linestyle="--")
plt.axhline(60, color="red", linestyle="--")
plt.title("Gold to Silver Ratio")
plt.ylabel("GSR")
plt.xlabel("Date")
plt.grid(True)

plt.show()