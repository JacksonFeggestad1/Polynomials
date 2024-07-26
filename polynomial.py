#import numpy as np 
from numpy import concatenate, zeros, convolve, array

class Polynomial:
    def __init__(self, _coeffs):
        while(_coeffs[0] == 0):
            _coeffs = _coeffs[1:]
        self.coeffs = _coeffs       #self.coeffs is a numpy array
        self.deg = len(self.coeffs)-1

    def __add__(self, unself):
        return Polynomial(Polynomial.add(self.coeffs, unself.coeffs))
    
    def __sub__(self, unself):
        return Polynomial(Polynomial.add(self.coeffs, -1*unself.coeffs))
    
    def __mul__(self, unself):
        return Polynomial(Polynomial.mult(self.coeffs, unself.coeffs))
    
    def __call__(self, x):
        result = 0
        for i in range(self.deg+1):
            result += x**(self.deg-i)*self.coeffs[i]
        return result
    
    def __eq__(self, unself):
        if len(self.coeffs) == len(unself.coeffs):
            comp = self.coeffs == unself.coeffs
            if False in comp:
                return False
            else:
                return True
        else:
            return False
        
    def __ne__(self, unself):
        return not self==unself
    
    def derivative(self):
        new_coeffs = array(self.coeffs[:-1:])
        for i in range(self.deg + 1):
            new_coeffs[i] *= (self.deg + 1-i)
        return Polynomial(new_coeffs)
    
    #x_0 is what f(0) should be
    def integral(self, x_0=0):
        new_coeffs = concatenate((self.coeffs, array([x_0])),dtype=float)
        for i in range(self.deg+1):
            new_coeffs[i] /= (self.deg + 1 - i)
        return Polynomial(new_coeffs)
    
    def to_string(self):
        result = ""
        if self.coeffs[0] != 1 and self.coeffs[0] != -1:
            if self.deg > 1:
                result += f'{self.coeffs[0]}x^{self.deg}'
            elif self.deg == 1:
                result += f'{self.coeffs[0]}x'
            else:
                result += f'{self.coeffs[0]}'
        elif self.coeffs[0] == 1:
            if self.deg > 1:
                result += f'x^{self.deg}'
            elif self.deg == 1:
                result += f'x'
            else:
                result += f'1'
        else:
            if self.deg > 1:
                result += f'-x^{self.deg}'
            elif self.deg == 1:
                result += f'-x'
            else:
                result += f'-1'

        for i in range(1,self.deg):
            if self.deg-i > 1:
                if self.coeffs[i] > 0:
                    if self.coeffs[i] == 1:
                        result += f' + x^{self.deg-i}'
                    else:
                        result += f' + {self.coeffs[i]}x^{self.deg-i}'
                elif self.coeffs[i] < 0:
                    if self.coeffs[i] == -1:
                        result += f' - x^{self.deg-i}'
                    else:
                        result += f' - {abs(self.coeffs[i])}x^{self.deg-i}'
            else:
                if self.coeffs[i] > 0:
                    if self.coeffs[i] == 1:
                        result += f' + x'
                    else:
                        result += f' + {self.coeffs[i]}x'
                elif self.coeffs[i] < 0:
                    if self.coeffs[i] == -1:
                        result += f' - x'
                    else:
                        result += f' - {abs(self.coeffs[i])}x'

            
        if self.coeffs[-1] != 0 :
            if self.coeffs[-1] < 0:
                return result + f' - {abs(self.coeffs[-1])}'
            else:
                return result + f' + {self.coeffs[-1]}'
        
        return result
    
    # p and q are polynomial objects
    def add(p, q):
        if len(q) > len(p):
            p, q = q, p
        if len(p) != len(q):
            q = concatenate((zeros(len(p)-len(q),dtype=int), q))
        return p+q

    def mult(p, q):
        return convolve(p,q, mode='full')