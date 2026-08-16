# Write a program to find the greatest of four numbers entered by the user.
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if(a > b and a > c and a > d ):
    print("a is the greatest")
elif(b > c and b > d):
    print("b is the greatest")
elif(c > d):
    print("c is the greatest")
else:
    print("d is the greatest")        