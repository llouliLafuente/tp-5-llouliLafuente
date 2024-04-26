# Replace the "ANSWER HERE" for your answer

import math

def roots(a, b, c):
    if a == 0:
        return "()"
    determinant = b ** 2 - 4 * a * c
    if determinant < 0:
        return "()"
    elif determinant == 0:
        x1 = (-b + math.sqrt(determinant) / 2*a)
        return str(x1)
    else:
        x1 = (-b + math.sqrt(determinant)) / (2 * a)
        x2 = (-b - math.sqrt(determinant)) / (2 * a)
        return str(x1), str(x2)


def value_y(a, b, c, x):
    return a * x ** 2 + b * x + c


def to_string(a, b, c):
    return "Y = " +  str(a) + " * X^2 + " + str(b) + " * X + " + str(c)


def derivation(a, b):
    return "Y' = " + str(2 * a) + "* X + " + str(b)

print(roots(1, -3, 2))
print(value_y(1, -3, 2, 0))
print(to_string(2, -3, 1))
print(derivation(2, -3))
