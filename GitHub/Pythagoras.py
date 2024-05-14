import math


def pythagorean_theorem(a, b):
    """
    Calculate the length of the hypotenuse using the Pythagorean theorem.

    Args:
    - a (float): Length of one of the legs of the right triangle.
    - b (float): Length of the other leg of the right triangle.

    Returns:
    - float: Length of the hypotenuse.
    """
    return math.sqrt(a ** 2 + b ** 2)


print("Welcome to the Pythagorean Theorem Calculator!")
a = float(input("Enter the length of the first leg (a): "))
b = float(input("Enter the length of the second leg (b): "))

    # Calculate the length of the hypotenuse
    c = pythagorean_theorem(a, b)

    print(f"The length of the hypotenuse (c) is: {c:.2f}")


