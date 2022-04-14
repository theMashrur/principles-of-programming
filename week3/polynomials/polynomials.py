from numbers import Integral, Number

from copy import deepcopy


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            return self + -1*other

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,)
                              + self.coefficients[1:])
        
        else:
            return NotImplemented
    
    def __rsub__(self, other):
        return -1*self+other

    def __mul__(self, other):
        
        if isinstance(other, Polynomial):
            s = self.coefficients
            o = other.coefficients
            prod = [0]*(len(s)+len(o)-1)
            for spower, sco in enumerate(s):
                for opower, oco in enumerate(o):
                    prod[spower+opower] += sco*oco
            return Polynomial(tuple(prod))


        
        elif isinstance(other, Number):
            s = self.coefficients
            return Polynomial(tuple([other*item for item in s]))
        
        else:
            return NotImplemented
    
    def __rmul__(self, other):
        return self*other

    def __pow__(self, num):
        if isinstance(num, Integral):
            c = deepcopy(self)
            for i in range(num-1):
                c = c*self
        return c

    def __call__(self, num):
        s = self.coefficients
        val = 0
        for power, coef in enumerate(s):
            val += coef*(num**power)
        return val

    def dx(self):
        s = self.coefficients
        if len(s)==1:
            return Polynomial((0,))
        deriv = [s[i]*i for i in range(1, len(s))]
        return Polynomial(tuple(deriv))

x = Polynomial((1,))
def derivative(poly):
    return poly.dx()
print(derivative(x))