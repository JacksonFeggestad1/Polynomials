from polynomial import Polynomial
import numpy as np

'''
H = Polynomial(np.array([10, 200,0,-100]))
print(f'deg(H) = {H.deg}, H = {H.to_string()}')
print(f'H = {H.to_string()}, Int^2(H) = {H.integral(x_0=2).integral(x_0=2).to_string()}')
print(f'Roots of H = {H.newtons(eps=0.00001, num_points=5)}')
'''
arr = []
for i in range(1,6):
    arr.append(Polynomial(np.array([1.0,-i])))
    
F = arr[0]*arr[1]*arr[2]*arr[3]*arr[4]
print(F.newtons(num_points = 10, sampling=[1.9,2.1]))
