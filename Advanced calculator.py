name = str(input("Enter your name: "))
print(f"Dear {name}, Welcome to area calculator program")
print("the first program calculate the area of a circle given a radius")

#area of a circle
pi = 3.14
r = float(input("Enter the radius of the circle: "))
AOC = (pi*(r**2))
print(f"the area of the circle is {AOC}")

print("this program calculates the area of a triangle given a base and height")
#area of a triangle
b = float(input("Enter the base of the triangle: "))
h = float(input("Enter the height of the triangle: "))
AOT = ((b*h)/2)
print(f"the area of the triangle is {AOT}")

print("this program calculates the area of a sqaure given the lenght of side")
#Area of a square
s = float(input("Enter the lenghth of the square: "))
AOS = (s**4)
print(f"the area of the square is {AOS}")

#Print statements for the areas of the shapes
#print(f"the area of the circle is {AOC},\n the area of the triangle is {AOT}, \n the area of the square is {AOS}")
