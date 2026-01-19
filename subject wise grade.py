sub1=float(input("Enter the marks of subject 1:"))
sub2=float(input("Enter the marks of subject 2:"))
sub3=float(input("Enter the marks of subject 3:"))

total=sub1+sub2+sub3
average=total/3

print("Total Marks:", total)
print("Average Marks:", average)

if sub1<40 or sub2<40 or sub3<40:
    print("You have failed in the exam.")
else:
    print("You have passed the exam.")

# for subject 1

if sub1<45:
    print("grade in sub 1: P")
elif sub1<50:
    print("grade in sub 1: C")
elif sub1<55:
    print("grade in sub 1: B")
elif sub1<60:
    print("grade in sub 1: B+")
elif sub1<70:
    print("grade in sub 1: A")
elif sub1<80:
    print("grade in sub 1: A+")
else:
    print("grade in sub 1: O")


# for subject 2

if sub2<45:
    print("grade in sub 2: P")
elif sub2<50:
    print("grade in sub 2: C")
elif sub2<55:
    print("grade in sub 2: B")
elif sub2<60:
    print("grade in sub 2: B+")
elif sub2<70:
    print("grade in sub 2: A")
elif sub2<80:
    print("grade in sub 2: A+")
else:
    print("grade in sub 2: O")

# for subject 3

if sub3<45:
    print("grade in sub 3: P")
elif sub3<50:
    print("grade in sub 3: C")
elif sub3<55:
    print("grade in sub 3: B")
elif sub3<60:
    print("grade in sub 3: B+")
elif sub3<70:
    print("grade in sub 3: A")
elif sub3<80:
    print("grade in sub 3: A+")
else:
    print("grade in sub 3: O")