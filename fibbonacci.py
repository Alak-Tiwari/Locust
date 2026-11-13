def fibbo_num(number):
    a=0
    b=1
    print(f"{a} {b}",end=" ")
    
    for i in range(2,number):
        
        c=a+b
        print(f"{c} ",end=" ")
        a=b
        b=c
num=int(input("Enter the numer till which you want to print the fibbonacci series\n"))
fibbo_num(num)