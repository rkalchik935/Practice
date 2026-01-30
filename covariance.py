import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


stock = yf.download("KHC", period="10y", interval="1d")
index = yf.download("DX-Y.NYB", period="10y", interval="1d")

stock = stock["Close"]
index = index["Close"]

df = pd.concat([stock, index], keys=["Stock", "Index"], axis=1).dropna()
df.columns = ["Stock", "Index"]

x = df["Stock"].to_numpy().reshape(-1,1)
y = df["Index"].to_numpy().reshape(-1,1)

xy_matrix = np.hstack([x, y])

covar_matrix = np.cov(xy_matrix, rowvar=False)

print(covar_matrix)
print(df.corr())

# --- SIMPLE PLOT ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Time Series (Both on same plot with dual y-axis)
ax1.plot(df.index, df["Stock"], 'b-', label='KHC Stock', linewidth=1)
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Price ($)', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Create second y-axis for Index
ax1_twin = ax1.twinx()
ax1_twin.plot(df.index, df["Index"], 'r-', label='Dollar Index', linewidth=1, alpha=0.7)
ax1_twin.set_ylabel('Dollar Index', color='r')
ax1_twin.tick_params(axis='y', labelcolor='r')

ax1.set_title('Time Series: Stock vs Dollar Index')
ax1.grid(True, alpha=0.3)

# Add legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax1_twin.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# Plot 2: Scatter Plot with correlation
ax2.scatter(df["Stock"], df["Index"], alpha=0.5, s=10, color='green')
ax2.set_xlabel('Stock Price ($)')
ax2.set_ylabel('Dollar Index')
ax2.set_title('Scatter: Stock vs Index')

# Add correlation line if correlation is meaningful
correlation = df.corr().iloc[0, 1]
if abs(correlation) > 0.1:  # Only plot line if there's some correlation
    z = np.polyfit(df["Stock"], df["Index"], 1)
    p = np.poly1d(z)
    ax2.plot(df["Stock"], p(df["Stock"]), "r--", alpha=0.8, linewidth=2)

# Add correlation value as text
ax2.text(0.05, 0.95, f'Correlation: {correlation:.3f}', 
         transform=ax2.transAxes, fontsize=12,
         verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# Add covariance values
ax2.text(0.05, 0.85, f'Covariance: {covar_matrix[0,1]:.2f}', 
         transform=ax2.transAxes, fontsize=10,
         verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.6))

ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print summary statistics
print(f"\n=== Summary Statistics ===")
print(f"Correlation coefficient: {correlation:.4f}")
print(f"Covariance: {covar_matrix[0,1]:.4f}")
print(f"Stock variance: {covar_matrix[0,0]:.4f}")
print(f"Index variance: {covar_matrix[1,1]:.4f}")
print(f"Data points: {len(df)}")
print(f"Date range: {df.index[0].date()} to {df.index[-1].date()}")