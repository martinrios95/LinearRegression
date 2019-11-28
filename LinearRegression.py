'''
LinearRegression - Python class to use Linear Regression, a supervised Machine-Learning algorithm

Author: Martin Rios (TechD)

Copyright (C) 2019, Martin Rios
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Used for research purposes.

'''

from LinearEquation import LinearEquation

class LinearRegression(LinearEquation):
    # Create set to fit data on this model 
    def __init__(self):
        super().__init__()
        n = 0
        x = []
        y = []

    # Fit data on this model, using Mean
    def fit(self, x, y):
        if (x == None or y == None):
            raise ValueError("X/Y values mustn't be empty.")
        if (type(x) is not list or type(y) is not list):
            raise ValueError("X/Y values must be lists.")

        self.x = x
        self.y = y

        self.n = min(len(x), len(y))

        Sx = 0
        Sy = 0
        Sx2 = 0
        Sxy = 0

        for i in range(0, self.n):
            Sx += x[i]
            Sy += y[i]
            Sx2 += x[i] ** 2
            Sxy += x[i] * y[i]

        self.a = ((self.n * Sxy) - (Sx * Sy)) / ((self.n * Sx2) - (Sx ** 2))
        self.b = ((Sy) - (self.a * Sx)) / (self.n)

    # Size of the dataset which was fitted
    def size(self):
        return self.n
    
    # Predict values after fitting
    def predict(self, values):
        calculated = []
        for i in range(0, len(values)):
            calculated.append(self.get_y(values[i]))
        
        return calculated