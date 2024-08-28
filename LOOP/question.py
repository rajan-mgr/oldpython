#2.WAP to take a number 'n' as input, find and display the factorial of 'n'.

# n=int(input("Enter a number:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i

# print(f"factorial of {n} is {fact}")

#3.WAP to display multiplication of a number in reverse order (i.e. 5*10=50 first and 5*1 =5 in last)

# n=int(input("Enter a digit:"))
# print("Multiplication in reverse:")
# for i in range(10,0,-1):
#     print(f"{n}*{i}={n*i}")

#4.WAP to display  and count the numbers of vowels in a string entered by the user

# n=input("Enter any string:")
# a=['a','e','i','o','u','A','E','I','O','U']
# count=0
# for i in n:
#     if i in a:
#         count=count+1

# print(f"Total nnumber of vowel is {count}")

    
#5.Suppose you have a list of marks obtained by ten students as [60,67,45,87,90,78,84,38,13,56]. 
#A) Find the number of students who scored 60 or more than 60, what will be the total sum of marks obtained by only these students? .
#B) is there any student who scored exactly 13 ? (just yes or no question, no need to count the number of students who scored exactly 13)

#A:
# list_of_marks=[60,67,45,87,90,78,84,38,13,56]
# sum=0
# student=0
# for i in list_of_marks:
#     if i>=60:
#         student=student+1
#         sum=sum+i
# print(f"The student that obtain greater then 60 is {student} and sum of marks is {sum}")

# #B:
# for i in list_of_marks:
#     if i==13:
#         print("YES there is student who scored 13 marks")

#6.WAP to find the sum of all the digits of a number enter by the user (23189 ==> 2+3+1+8+9 ==> 23)
# n=int(input("Enter the digits:"))
# str=str(n)
# sum=0
# for i in str:
#     sum=sum+int(i)
# print(f"sum of digits is {sum}")

#7.WAP to check whether a number enter by the user is Prime or Not

#WAP to check whether a number enter by the user is Prime or Not
# a=int(input("Enter a number: "))
# count=0
# for i in range(1,a+1):
#     if a%i==0:
#         count+=1

# if count==2:
#     print("It is prime")
# else:
#     print("It is not prime")

#8.WAP to generate Fibonacci series up to n terms

# n=int(input("Enter a digit:"))
# a,b=0,1
# for i in range(1,n+1):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c

#9.WAP to check whether a number enter by the user is Armstrong or not.

# n=input("Enter a num:")
# l=len(str(n))
# sum=0
# for i in n:
#     x=int(i)
#     sum=sum+x**l

# if sum==int(n):
#     print("Armstrong")
# else:
#     print("Not Armstrong")

#10.WAP to print the following pa[erns without using nested loop (just a single loop) as follows.

# for i in range(1,6):
#     print('*'*i)

# for i in range(5,0,-1):
#     print('*'*i)

# for i in range(1,6):
#     a=str(i)
#     print(a*i)

# for i in range(1,6):
#     print(' '*(5-i),'*'*i)

# for i in range(5,0,-1):
#     print(' '*(5-i),'*'*i)

# n="GOBLIN"                             
# for i in range(1,7):
#     print(n[:i])       

# n="GOBLIN"
# for i in range(1,len(n)+1):
#     print(n[:i])  

# n="GOBLIN"
# for i in range(6,0,-1):
#     print(n[:i])

# n="GOBLIN"
# for i in range(1,7):
#     print(' '*(6-i),n[:i])

# n="GOBLIN"
# for i in range(6,0,-1):
#     print(' '*(6-i),n[:i])    


    