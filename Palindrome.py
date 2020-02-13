n=int(input("Enter number: "))
r=0
x=n
print("Given number",n)
while n>0:
    d=n%10
    r=r*10 +d
    n=n//10
if x==r:
    print("It is a Palindrome number",x)
else:
    print("It is NOT a palindrome number",x)
