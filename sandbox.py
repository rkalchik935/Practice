import numpy as np

def get_intersection(x, coef1, coef2):
    a, b = coef1[0], coef1[1]
    c, d = coef2[0], coef2[1]
    
    y1 = a * x - b * np.log(x)
    y2 = c * x - d * np.log(x)
    dif = y1 - y2
    i = 0
    
    prev = dif[0]
    for i in range(1, len(dif)):
        curr = dif[i]
        if prev >= 0 and curr < 0:
            return x[i]
        prev = curr

    return np.nan

x = np.linspace(1e-3, 5, 1000)
print(get_intersection(x, [8, 25], [3, 4]))