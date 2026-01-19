x=float(input("Enter the x coordinate of center: "))
y=float(input("Enter the y coordinate of center: "))

r=float(input("Enter the radius of circle: "))

x1=float(input("Enter the x coordinate of point: "))
y1=float(input("Enter the y coordinate of point: "))

a=x1**2+y1**2

if a==r**2:
    print("The point",(x1,y1),"lies on the circle")
elif a<r**2:
    print("The point",(x1,y1),"lies inside the circle")
else:
    print("The point",(x1,y1),"lies outside the circle")


