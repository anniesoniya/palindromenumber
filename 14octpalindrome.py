# check  wetherthe number is a plindrome or not
n = int(input("enter number---:"))
rev = 0
num = n
while n>0:

    val=n%10
    rev=rev*10+val
    n=n//10
if num == rev:
    print("it is a palindrome number")
else:
   print("not a palindrome")
