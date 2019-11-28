'''
LinearEquation - Python class to make "y = ax + b" linear equation.

Author: Martin Rios (TechD)

Copyright (C) 2019, Martin Rios
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Used for research purposes.

'''
class LinearEquation:
    # Create equation with coefficients
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    # Get coefficients
    def coefs(self):
        return [self.a, self.b]

    # Get X-axis from Y-axis
    def get_x(self, y = 0):
        if (self.a == 0):
            raise ZeroDivisionError("Linear coefficient is zero. Cannot calculate X-axis.")
        return (y - self.b) / (self.a)

    # Get Y-axis from X-axis
    def get_y(self, x = 0):
        return (self.a * x) + self.b

    # Get X-root
    def root_x(self):
        return self.get_x()

    # Get Y-root
    def root_y(self):
        return self.b

    # Represent y = ax + b equation
    def __str__(self):
        return "y = " + str(self.a) + "x + " + str(self.b)