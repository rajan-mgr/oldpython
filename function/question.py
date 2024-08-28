#  Make a function to find sum of squares of first ‘n’ natural numbers. The function should take ‘n’
# as an argument and should return the final sum value to the calling location
#.(function with argument and with return type)

# def sum_square(n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i*i
#     return sum

# n=int(input("Enter a number:"))
# a=sum_square(n)                 #return value is assign when function is call
# print("sum of square to that no",a)


#  Make a function to check whether a number ‘n’ is prime or not, the function should 
# take ‘n’ as an argument and display appropriate message from inside the function. (function with argument and without return type) 

# def prime(n):
#     count = 0
#     for i in range(1, n+1):
#         if n%i==0:
#             count=count+1

#     if count==2:
#         print("Prime")
#     else:
#         print("Not prime")

# num = int(input("Enter the number: "))
# prime(num)


# Make a user-defined function that generates the Fibonacci series
# upto ‘n’ terms. Make a function without argument and without return type.  

# def fib():
#     n=int(input("Enter a number:"))
#     a=1
#     b=2
#     for i in range(n):
#         print(a,end="\t")
#         c=a+b
#         a=b
#         b=c

# fib()        

# Make a user defined function that takes marks of 10 students as input from the user and returns sum & average marks of 10 students. 
# The function must be of type “without argument and with return type”. i.e. 
# marks should be taken input from within the user defined function. 

# def marks():
#     sum=0
#     for i in range(1,11):
#         m=int(input(f"Enter marks of student{i}:"))
#         sum=sum+m
#     avg=sum/10
#     return sum,avg

# a,b=marks()
# print("Sum of marks is",a)
# print("Avg of marks is ",b)



#wap that has a user defined function "pattern",that takes a string as an argument and print that string in following patteren.
# j
# j h
# j h i
# j h i l k
# j h i l k e

# def pattern(n):
#     for i in range(len(n)):
#         for j in range(i + 1):
#             print(n[j], end=" ")
#         print()


# input = input("Enter a string: ")
# pattern(input)

def pattern(name):
    for i in range(1,len(name)+1):
        print(name[:i])

n=input("Enter a string:")
pattern(n)            