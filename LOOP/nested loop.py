# for i in range(1,4):
#     print("outer loop",i)
#     for j in range(0,3):
#         print("inner loop:",j)
 
#WEEK9 NO 5
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="\t")
    
#     print()

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end="\t")
    
#     print()

# 1.Suppose u have a list a=[2,4,5,6,7,8,13,15,17,20]. Display all the prime numbers of the above
# list , also display total no of prime numbers

# a=[4,5,6,7]
# c=0
# for n in a:
#     count=0
#     for j in range(1,n+1):
#         if n%j==0:
#             count=count+1
#     if count==2:
#         print(n,"is prime")
#         c=c+1
#     else:
#         print(n,"is not prime")
    

# print("total no of prime",c)

# n=int(input("Enter a number:"))
# while n>9:
#     sum=0
#     while n>0:
#         r=n%10
#         sum=sum+r
#         n=n//10
#     n=sum
# print("sum to single digit is ",n)    

# n=int(input("Enter a number:"))

# for i in range(1,11):
#     for j in range(1,n+1):
#         print(f"{j}*{i}={i*j}",end='\t')
#     print()

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()    

#6.WAP that asks the user to enter a number one at a time until the user hits exactly zero (0).
#Display the sum of all the numbers that were entered by the user before hitting zero.

# sum=0
# while True:
#     n=int(input("Enter a number:"))
#     sum=sum+n
#     if n==0:
#         break    

# print(f"Sum of number is {sum}")


# WAP that asks the user to enter an integer number one at a time until the user hits fifth even
# number, note that the user can hit even or odd numbers randomly. Display the total sum of those
# five even numbers at last.

# sum=0
# count=0
# while True:
#     n=int(input("Enter a number:"))
#     if n%2==0:
#         sum=sum+n
#         count=count+1
#     if count==5:
#         break

# print(f"Sum of even number is {sum}")    

#  Let us consider a user login system whose username is : “jhilke” and password is : “jhilke@1”.
# WAP to ask the user to enter the username and password to login to the system. If both
# username and password is correct, display “login successful !” and end the program. Otherwise,
# display “ incorrect username or password”, and again ask the user to enter the username and
# password. If the user hits incorrect username or password for third time, display “sorry! You
# entered wrong username or password for third time, you cannot login” , and end the program

# usr="jhilke"
# psw="@jhilke123"
# count=0
# while True:
#     user=input("Enter your name:")
#     pasw=input("Enter your password:")

#     if usr==user and psw==pasw:
#         print("Login successful!")    
#         break
#     else:
#         count=count+1
#         print("incorrect input try again")

#     if count==3:
#         print("3 chances finish ") 
#         break
        



#  Suppose you have a string str1=“ram123@baha23dur#”. WAP to copy the alphabet characters
# to another string str2, and numeric characters to another string str3. Finally display the contents
# of str2 and str3

a="ram123@baha23dur"
b=""
c=""
for i in a:
    if i.isalpha():
        b+=i
    elif i.isdigit():
        c+=i
    else:
        pass
print("Alphabet",b)
print("Digit",c)    