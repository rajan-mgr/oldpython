1.Write a Python program that checks if a given number is positive, negative, or zero.

a=int(input("enter a number:"))
if a>0:
    print("positive")
elif a<0:
    print("negetive")
else:
    print("neutral")

2.Write a Python program that determines whether a given year is a leap year or not, without using nested if-else.

year=int(input("Enter a year:"))
if year%400==0:
    print("It is leap year")
elif year%100==0:
    print("It is not leap year")
elif year%4==0:
    print("is is leap year")
else:
    print("is is not leap year")

3.Write a Python program that finds the maximum of three numbers. (without nested if-else)

a,b,c=map(int,input("enter 3 intergers:").split())

if a>b and a>c:
    print(a," is greater.")
elif b>c and b>a:
    print(b," is greater.")
else:
    print(c," is greater.")

4.Write a Python program that checks if a given character is a vowel or a consonant.

a=input("Enter a character:")
if a=='a' or a=='i' or a=='o' or a=='e' or a=='u':
    print("vowel")
else:
    print("consonant")

5.Write a Python program that determines whether a given string is a palindrome or not.

ch=input("Enter a string:")
rev=ch[::-1]
if ch==rev:
    print("Palindrome")
else:
    print("Not palindrome") 

6.Write a Python program that calculates the grade based on a given percentage. (80-100: A, 60-80:B and so on). Take percentage of user as input.

n=float(input("Enter your percentage:"))
if n<=100 and n>=80:
    print("A")
elif n>=60:
    print("B")
elif n>=40:
    print("C")
else:
    print("FAILED") 

7. Write a Python program that determines the largest among three numbers using nested if-else statements.

a,b,c=map(int,input("Enter 3 intergers:").split())   

if a>b:
    if a>c:
        print(a,"is greater")
    else:
        print(c,"is greater")
else:
    if b>c:
        print(b,"us greater")
    else:
        print(c,"is greater")
    
8.Write a Python program that determines the type of a triangle based on the given side lengths.(equilateral, isosceles , scalene) without nested if-else

a,b,c=map(int,input("Enter 3 length:").split())
if a==b and b==c and c==a:
    print("it is a equilateral triangle")
elif a==b and a!=c or b==c and b!=a or c==a and c!=b:
    print("it is isoceles")
else:
    print("it is scalene")


9.Write a Python program that determines the smallest among three numbers using nested if-else statements.

a,b,c=map(int,input("Enter 3 integers:").split())

if a<b:
    if a<c:
        print(f"{a} is small among three number.")
    else :
        print(f"{c} is small among three number.")
else :
    if b<c:
        print(f"{b} is small among three number.")
    else :
     print(f"{c} is small among three number.")

10.Write a Python program that checks if a given character is an alphabet, digit, or special character. (special characters are other characters than alphabets and digits)

n=input("enter any thing: ")
if n.isalpha():
    print("this is alphabet.")
elif n.isdigit():
    print("this is digit.")
else:
    print("this is special charecter.")

11.Write a Python program that calculates the area of different shapes (circle, rectangle, and square) based on user input. ( take the name of shapes as input: i.e. “circle”, “rectangle” etc.)

shape=input("enter the shape:")

if shape=='circle':
    r=float(input("Enter the radius:"))
    pi=3.1415
    A=pi*r*r
    print(A,"is the area of circle")

elif shape=='rectangle':
    l=int(input("Enter the length:"))
    b=int(input("Enter the breadth:"))
    A=l*b
    print(A,"is the area of rectangle")

elif shape=='square':
    l=int(input("Enter the length:"))
    A=l*l
    print(A,"is the area of sqaure")

else:
    print("Invalid syntax")

12.Write a Python program that checks if a given year is a leap year or not, using nested if-else statements.
year=int(input("Enter a year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap year")
        else:
            print("Not leap year")
        
    else:
         print("Leap year")
else:
    print("Not leap year")           


13. Write a Python program that checks if a given number is divisible by  5 and 7 using nested if-else statements. 
display message like :"divisible by both", "divisible by 5 but not with 7" and so on...(related messages)

a=int(input("Enter a number:"))
if a%5==0:
    if a%7==0:
        print("divisible by both")

else:
    print("not divisible")

14. Write a Python program that determines the season (spring, summer, autumn, or winter) based on a given month
. (take month as input, like : "jan", "feb",.. )

n=input("Enter the month: ")
m=n.capitalize()
if m=="December" or m=="Feburary" or m=="January":
    print("There is winter in ",m)
elif m=="March" or m=="May" or m=="April":
    print("There is spring season in ",m)
elif m=="June" or m=="August" or m=="July":
    print("There is summer season in ",m)
elif m=="September" or m=="October" or m=="November":
    print("There is autumn season in ",m)
else:
    print("Invalid data / spelling error")

15. Write a Python program that converts a given temperature from Celsius to Fahrenheit or vice versa based on user input.
( you can say, "enter 1 to convert celsius to fahrenheit , enter  2 for vice versa)

n=int(input("Enter 1 for C to F and 2 for F to C :"))

if n==1:
    c=int(input("Enter celsius value:"))
    F=(9/5)*c + 32
    print("Temperature in farenheit is",F)
elif n==2:
    f=int(input("Enter temperature in farenheit:"))
    C=(f-32)*(5/9)
    print("Temperature in celsius is",C)

else:
    print("Invalid user input")

16.Write a Python program that determines the winner of a rock-paper-scissors game based on user input and displays the result using if-else statements.
(Google the rule of this game. Write program to take inputs from two users , user1 and user2 and determine who wins the game based on their choice)   

print("1 for rock 2 for paper 3 for scissor:")
user1=int(input("Player 1 enter your choice:"))
user2=int(input("player2 enter your choice:"))

if(user1==user2):
    print("Draw")
elif(user1==2 and user2==1) or (user1==3 and user2==2) or (user1==1 and user2==3):
    print("Player1 Won")
else:
    # print("Player2 won")    

17.Write a Python program that determines the winner of a lottery game based on randomly generated numbers and user input using nested if-else statements.
Suppose the lottery numberlies between 1 and 99. Import random module, random.randint(1,99) gives random numberbetween 1 and 99.

import random
lucky_num=random.randint(1,99)
user_no=int(input("Enter your ticket no:"))
if lucky_num==user_no:
    print("Congrats!you won")
else:
    print("Sorry! Btter luck next time")

18.Write a Python program that converts a given number from decimal to binary, octal, or
hexadecimal based on user input using if-else statements. (bin(a), oct(a), hex(a) converts
decimal number “a” into binary, octal and hexadecimal respectively)

n=int(input("Enter a num:"))
print("Enter bin,oct or hex to convert to binary,octal or hexadecimal")
choice=input("Enter your choice:")
if choice=='bin':
    print("Equivalent binary no is",bin(n))
elif choice=='oct':
    print("Equi octal no is",oct(n))
elif choice=='hex':
    print("Equi hexadeci no is",hex(n))
else:
    print("Invalid input")

19.Write a Python program that determines the eligibility of a person for a driving license based on
age, education, and glass power using nested if-else statements. ( eligible criteria: age>18,
education level >10 and glass power <-6).

