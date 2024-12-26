import math

class Dual:
    """
    A class representing a dual number a + bε, where ε² = 0.

    Parameters
    ----------
    real : float
        The real part of the dual number.
    dual : float
        The dual part (ε) of the dual number.
    """

    __slots__ = ['real', 'dual']

    def __init__(self, real: float, dual: float):
        if not isinstance(real, (int, float)):
            raise TypeError(f"Real part must be a numeric type, got {type(real).__name__}")
        if not isinstance(dual, (int, float)):
            raise TypeError(f"Dual part must be a numeric type, got {type(dual).__name__}")
        self.real = real
        self.dual = dual

    def __repr__(self):
        return f"Dual(real={self.real}, dual={self.dual})"

    def __eq__(self, other):
        if isinstance(other, Dual):
            return self.real == other.real and self.dual == other.dual
        return False  # Dual is not equal to non-Dual types

    def __add__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real + other.real, self.dual + other.dual)
        elif isinstance(other, (int, float)):
            return Dual(self.real + other, self.dual)
        else:
            raise TypeError(f"Unsupported type for addition: {type(other).__name__}")

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real - other.real, self.dual - other.dual)
        elif isinstance(other, (int, float)):
            return Dual(self.real - other, self.dual)
        else:
            raise TypeError(f"Unsupported type for subtraction: {type(other).__name__}")

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Dual(other - self.real, -self.dual)
        else:
            raise TypeError(f"Unsupported type for subtraction: {type(other).__name__}")

    def __mul__(self, other):
        if isinstance(other, Dual):
            # (a + bε)(c + dε) = ac + (ad + bc)ε
            return Dual(
                self.real * other.real,
                self.real * other.dual + self.dual * other.real
            )
        elif isinstance(other, (int, float)):
            return Dual(self.real * other, self.dual * other)
        else:
            raise TypeError(f"Unsupported type for multiplication: {type(other).__name__}")

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, Dual):
            # (a + bε)/(c + dε) = (a/c) + ((b*c - a*d)/(c^2))ε
            if other.real == 0:
                raise ZeroDivisionError("Division by Dual with zero real part is undefined.")
            new_real = self.real / other.real
            new_dual = (self.dual * other.real - self.real * other.dual) / (other.real ** 2)
            return Dual(new_real, new_dual)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is undefined.")
            return Dual(self.real / other, self.dual / other)
        else:
            raise TypeError(f"Unsupported type for division: {type(other).__name__}")

    def __rtruediv__(self, other):
        if self.real == 0:
            raise ZeroDivisionError("Division by Dual with zero real part is undefined.")
        if isinstance(other, (int, float)):
            # (c) / (a + bε) = (c/a) + (-c*b)/(a^2) ε
            new_real = other / self.real
            new_dual = (-other * self.dual) / (self.real ** 2)
            return Dual(new_real, new_dual)
        else:
            raise TypeError(f"Unsupported type for division: {type(other).__name__}")

    # Trigonometric operations

    def sin(self):
        # sin(a + bε) = sin(a) + b*cos(a)*ε
        return Dual(math.sin(self.real), self.dual * math.cos(self.real))

    def cos(self):
        # cos(a + bε) = cos(a) - b*sin(a)*ε
        return Dual(math.cos(self.real), -self.dual * math.sin(self.real))

    def tan(self):
        # Check if cosine is zero (tan is undefined when cos(real) = 0)
        if math.isclose(math.cos(self.real), 0, abs_tol=1e-9):
            raise ValueError("Tangent is undefined for cos(real) = 0.")
        
        sec_squared = 1 / (math.cos(self.real) ** 2)
        return Dual(math.tan(self.real), self.dual * sec_squared)
    
    def exp(self):
        # exp(a + bε) = exp(a) + b*exp(a)*ε
        e = math.exp(self.real)
        return Dual(e, self.dual * e)

    def log(self):
        # log(a + bε) = log(a) + (b/a)*ε
        if self.real <= 0:
            raise ValueError("Logarithm not defined for non-positive real parts.")
        return Dual(math.log(self.real), self.dual / self.real)

    def sinh(self):
        return Dual(math.sinh(self.real), self.dual * math.cosh(self.real))
    
    def cosh(self):
        return Dual(math.cosh(self.real), self.dual * math.sinh(self.real))

    def tanh(self):
        sech = 1 / (math.cosh(self.real) ** 2)
        return Dual(math.tanh(self.real), self.dual * sech)

    #inverse trigonometric functions
    def arcsin(self):
        return Dual(math.asin(self.real), self.dual / math.sqrt(1 - self.real**2))

    def arccos(self):
        return Dual(math.acos(self.real), -self.dual / math.sqrt(1 - self.real**2))

    def arctan(self):
        return Dual(math.atan(self.real), self.dual / (1 + self.real**2))

    #logarithm with arbitrary base

    def log(self, base = math.e):
        if self.real <= 0:
            raise ValueError("Log undefined for non-positive.")
        return Dual(math.log(self.real, base), self.dual / (self.real * math.log(base)))

    # power and roots
    def power(self, exp):
        value = self.real ** exp
        derivative = exp * self.real ** (exp - 1)
        return Dual(value, self.dual * derivative)
    
    def root(self, degree):
    # Ensure degree is treated as an integer for even/odd check
        if self.real < 0 and int(degree) % 2 == 0:
            raise ValueError("Root of a negative number is not defined for even degrees.")
    
    # Root is equivalent to raising to the power of 1/degree
        reciprocal_degree = 1 / degree
        return self.power(reciprocal_degree)
