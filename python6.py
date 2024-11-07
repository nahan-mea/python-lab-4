square_area = lambda side: side * side
rectangle_area = lambda length, width: length * width
triangle_area = lambda base, height: 0.5 * base * height

side = float(input("Enter the side of the square: "))
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

print("Area of square:", square_area(side))
print("Area of rectangle:", rectangle_area(length, width))
print("Area of triangle:", triangle_area(base, height))
