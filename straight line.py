x1=float(input("Enter the x1 coordinate:"))
y1=float(input("Enter the y1 coordinate:"))

x2=float(input("Enter the x2 coordinate:"))
y2=float(input("Enter the y2 Coordinate:"))

x3=float(input("enter the x3 coordinate:"))
y3=float(input("Enter the y3 coordinate:"))

a=((x1-x2)**2+(y1-y2)**2)**0.5
b=((x2-x3)**2+(y2-y3)**2)**0.5
c=((x1-x3)**2+(y1-y3)**2)**0.5

if a+b==c:
    print("All The three points are on straight line")
else:
    print("ALL The three points are not on straight line")