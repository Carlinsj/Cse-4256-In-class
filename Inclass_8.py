# Question 1
class Complex:
    def __init__(self, a, b):
        self.a = a  # real part
        self.b = b  # imaginary part

    def __str__(self):
        # Only real part is nonzero.
        if self.b == 0:
            return str(self.a)
        # Only imaginary part is nonzero.
        if self.a == 0:
            return f"{self.b}i"
        # Both parts are nonzero: determine the sign between them.
        if self.b > 0:
            return f"{self.a} + {self.b}i"
        else:
            return f"{self.a} - {abs(self.b)}i"
        
# Question 2
def add(self, other):
    return Complex(self.a + other.a, self.b + other.b)

# Question 3
def neg(self):
        return self.negate()
# Question 4
def subtract(self, other):
    return self.add(other.negate())

# Question 5
def multiply(self, other):
    new_a = self.a * other.a - self.b * other.b
    new_b = self.a * other.b + self.b * other.a
    return Complex(new_a, new_b)

# Question 6
def multiply(self, other):
    new_a = self.a * other.a - self.b * other.b
    new_b = self.a * other.b + self.b * other.a
    return Complex(new_a, new_b)

# Question 6
def inverse(self):
    denominator = self.a**2 + self.b**2
    if denominator == 0:
        raise ZeroDivisionError("Cannot invert a zero complex number")
    return Complex(self.a / denominator, -self.b / denominator)

# Question 7
def divide(self, other):
    denominator = other.a**2 + other.b**2
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero complex number")
    
    new_a = (self.a * other.a + self.b * other.b) / denominator
    new_b = (self.b * other.a - self.a * other.b) / denominator
    return Complex(new_a, new_b)
# Question 8
def __sub__(self, other):
    return self.subtract(other)

def __mul__(self, other):
    return self.multiply(other)
