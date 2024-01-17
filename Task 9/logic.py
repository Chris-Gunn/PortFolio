import math

def area_of_circle(side_a, side_b):
    '''
    Wrong formula - Deliberately used pythagoras theorem instead of
    using the formula for the area of a circle
    '''
    side_c = math.sqrt(side_a**2 + side_b**2)
    return side_c


# Creates the two known sides to the right hand triangle
a = 20
b = 30

'''
x correctly gives the answer to the missing side of a right
angled triangle but it should have given the area of a circle
'''
x = area_of_circle(a, b)

print(f"The area of the circle is: {x:.2f}")