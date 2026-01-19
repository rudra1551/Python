a=int(input("enter a value:"))

def digit(a):
    count=0
    while a>0:
        count+=1
        a=int(a/10)
    print("the total no. of digits is",count)

digit(a)




