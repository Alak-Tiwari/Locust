def reverse_num(num):
    rev_num=0
    while(num!=0):
        r=num%10
        rev_num=rev_num*10+r
        num=num//10 
    return rev_num


number=231
print(f"reverse number of {number} is:")
num=reverse_num(number)
print(f"{num}")

#reverse of a string In same way we can convert integer to string and find the reverse of num
name="Alka"
reverse_name=name[::-1]
print(f"original string is {name} and reverese string is {name[::-1]}")