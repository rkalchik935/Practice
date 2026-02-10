import numpy as np
from scipy import stats

# c = option price
# s = stock price
# t = time to expiry
# rf = risk-free rate
# d1 = derived 1
# d2 = derived 2
# x = strike price
# sigma = standard deviaton of log returns


class Black_Scholes_Call():
    def __init__(self, s, t, rf, x, sigma):
        self.s = s
        self.t = t
        self.rf = rf
        self.x = x
        self.sigma = sigma

    def derived(self, s, t, rf, x, sigma):
        d1 = (np.log(s / x) + (rf + (sigma ** 2) / 2) * t) / (sigma * np.sqrt(t))
        d2 = (np.log(s / x) + (rf - (sigma ** 2) / 2) * t) / (sigma * np.sqrt(t))
        mu1 = np.log(s) + (rf + (sigma ** 2) / 2) * t
        mu2 = np.log(s) + (rf - (sigma ** 2) / 2) * t
        
        return d1, d2, mu1, mu2
    
    def lognormal_cdf(self):
        d1, d2, mu1, mu2 = self.derived(self.s, self.t, self.rf, self.x, self.sigma)

        shape = self.sigma * np.sqrt(self.t)
    
        scale1 = np.exp(mu1)
        log_norm1 = stats.lognorm(s=shape, scale=scale1)
        N1 = 1 - log_norm1.cdf(self.x)  # P(S_T > x) under stock measure
    

        scale2 = np.exp(mu2)
        log_norm2 = stats.lognorm(s=shape, scale=scale2)
        N2 = 1 - log_norm2.cdf(self.x) # P(S_T > x) under risk neutral measure
    
        return N1, N2
    
    def calculate_c(self):
        if self.t == 0:
            return max(0, self.s - self.x) # when time = 0 d1, d2 approach inf hence N1, N2 approach 1
        
        N1, N2 = self.lognormal_cdf()
        c = N1 * self.s - N2 * self.x * np.exp(-self.rf * self.t)
        
        return c
    

s, x, t, rf, sigma = 100.0, 100.0, 0.25, 0.05, 0.20

example_price = Black_Scholes_Call(s=s, x=x, t=t, rf=rf, sigma=sigma)

option = example_price.calculate_c()

print(option)