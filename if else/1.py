# wap to find positive or negetive

# n=int(input("Enter a number:"))
# if n>0:
#     print("positive")
# else:
#     print("negetive") #indentation

    
#wap to find greatest in three numbers

a,b,c=map(int,input("enter 3 intergers:").split())

if a>b and a>c:
    print(a," is greater.")
elif b>c and b>a:
    print(b," is greater.")
else:
    print(c," is greater.")