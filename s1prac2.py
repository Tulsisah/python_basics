#program that calculates the area and perimeter of a rectangle.
length=int(input("enter the length: "))
width=int(input("Enter width: "))
area=length*width
print("the area of rectangle is=",area)
width=2*(length+width)
print("the perimeter of rectangle =",width)
