from polynomial import Polynomial
import numpy as np


H1 = Polynomial(np.array([0,0,2,0,1]))
print(H1.to_string())

H2 = Polynomial(np.array([-1,3,-1,0]))
print(H2.to_string())

H3 = Polynomial(np.array([9,-2]))
print(H3.to_string())