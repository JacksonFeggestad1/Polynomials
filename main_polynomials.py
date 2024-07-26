from polynomial import Polynomial
import numpy as np


H = Polynomial(np.array([2,0,1]))
print(f'deg(H) = {H.deg}, H = {H.to_string()}')
print(f'H = {H.to_string()}, Int^2(H) = {H.integral(x_0=2).integral(x_0=2).to_string()}')