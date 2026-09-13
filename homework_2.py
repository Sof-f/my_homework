import math

shape = input("Enter what shape you want(circle or square): ")
if shape == "circle":
    radius = float(input("Enter a radius of circle: "))
    S = math.pi * (radius**2)
    print(S)

elif shape == "square":
    side = float(input("Enter a side of square: "))
    S = side**2
    print(S)

elif shape != "circle" and shape != "square":
    print("You entered wrong shape. Please enter circle or square.")


























a= float(input("Enter side a: "))
b= float(input("Enter side b: "))
c= float(input("Enter side c: "))

p= (a+b+c)/2
s= math.sqrt(p*(p-a)*(p-b)*(p-c))
print(s)