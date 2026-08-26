import numpy as np

def sin_taylor(x0, n):    
    if not isinstance(n, int):
        if not isinstance(n, float):
            raise TypeError
            return
        if not x.is_integer():
            raise TypeError
            return
        n = int(n)

    fac = 1

    for i in range(1, n + 1):
        fac = fac * i
    

    if n % 4 == 1:
        return np.power(x0, n) / fac
    else:
        return -np.power(x0, n) / fac

print(sin_taylor(1.7, 5))