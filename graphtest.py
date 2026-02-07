import numpy as np

x = np.linspace(1e-3, 5, 1000)

def get_argmin(x, coef):
    a = coef[0]
    b = coef[1]
    y = a * x - b * np.log(x)
    
    min_index = np.argmin(y)
    
    min_x = x[min_index]
    
    return min_x
    



get_argmin(x, [13,20])