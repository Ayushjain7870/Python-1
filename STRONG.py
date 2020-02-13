n=int(input("Enter number: "))
sf=0
x=n
print("Given number",n)
while n>0:
    d=n%10
    f=1
    while d>0:
        f=f*d
        d=d-1
    sf=sf+f
    n=n//10
if x==sf:
    print("Strong")
else:
    print("Not strong")
