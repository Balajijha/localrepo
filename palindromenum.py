rev=0
n=int(input("enter a number:"))
num1=n
while(n):
    rev=rev*10+n%10
    n=n//10
if rev==num1:
    print(num1,"is palindrome number")
else:
    print(num1,"is not a palindrome number")