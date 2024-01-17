import math
# Request the user to enter three length for a triangle
side1 = int(input("Please enter the first sides length: "))
side2 = int(input("Please enter the second sides length: "))
side3 = int(input("Please enter the first sides length: "))

# Calculate the area of a triangle
s = (side1 + side2 + side3)/2
print(s)
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
print(area)
