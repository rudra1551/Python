a=int(input("Enter the length of rectangle: "))
b=int(input("Enter the breadth of rectangle: "))

area=a*b
perimeter=2*(a+b)

if area>perimeter:
    print("The area of rectangle is greather than its perimeter")
elif area==perimeter:
    print("The area of rectangle is equal to its perimeter")
else:
    print("The area of rectangle is NOT greather than its perimeter")
