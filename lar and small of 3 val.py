a=int(input("Enter a value:"))
b=int(input("Enter a value:"))
c=int(input("Enter a value:"))


if a==b==c:
    print("all three are equal")
elif a>b>c:
    print(a,"is larget and",c,"is smallest")
elif a>c>b:
    print(a,"is larget and",b,"is smallest")
elif b>a>c:
    print(b,"is larget and",c,"is smallest")
elif b>c>a:
    print(b,"is larget and",a,"is smallest")
elif c>b>a:
    print(c,"is larget and",a,"is smallest")
elif c>a>b:
    print(c,"is larget and",b,"is smallest")

