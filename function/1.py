# def greet(n):
#     print("Hello",n)

# name=input("Enter ur name:")
# greet(name) #ARGUMENT VALUE ASSIGN IN PARAMETER

# def greet():
#     name=input("Enter your name:")
#     return name

# print("Hello",greet())

# def greet():
#     name=input("Enter your name:")
#     return name

# n=greet()
# print("Hello",n)

# def greet():
#     name=input("Enter your name:")
#     print("Hello",name)

# greet()

# def greet(a):
#     print("we r inside function")
#     return "hello" +a

# name=input("Enter ur name:")
# n=greet(name)
# print(n)



#keyword arguments


# def si(p,t,r):

# si(p=1000,t=5.r=0.5)

#default arguments

# def display(a,b=5):   #if argumrnt is assigned while calling it will replace the default value
#     print("a is",a)
#     print('b is',b)

# display(2)   


#RULE:non defalut argument is followed by a default argument

#PASSING MULTIPLE ARGUMENTS
# def display(*argument_name)

# a=b,b=9  (data stored as touple)

#Passing multiple keyword argument

# def display(**keywordargument_name):

# value stored as dictonary


#GLOBAL AND LOCAL VARIBALE

# variable defined outside the function are global

# name='boi'   
# def greet()

#varibale defined inside a specific function is local variable

#global keyword

# def greet():
#     global age  #we use global keyword to make a varibale global  
#     age=18
    

# #we can modify global variable inside from the function
# name='jhike'
# def greet():
#     global name
#     name='ram'

#nested function:

# def first_function():
#     print("oi")
#     def sec_function():
#        print("k xa")
#     sec_function()        #to run second function we need to call from the body of first function()
# first_function()        


#Lamda function(anonymus function)

# function_name=lambda keyword argumentslist:expression #it an have multiple arguments a=but only one expression
# a=lambda b:b+1
# print(a(3))

# def power(n):
#     return lambda x:x**n

# num=int(input("Enter a number:"))
# square=power(2)
# print("sqaure of ",num,"is",square(num))

#recursive function




