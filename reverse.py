def reverse(n):
    rev=0
    while(n!=0):
        digit=n%10
        rev=rev*10+digit
        n=n//10
    print(rev)
        


x=int(input("Enter the no."))
reverse(x)
