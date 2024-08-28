#list,tuple:

#list:
# collection of any datatype in square bracker
# mutable
# index starts with 0
# allow repetition  

#string silicing

# name='Rajan'
# print(name[::-2])

# .sort used to sort in ascending order.

# name=[3,4,5,2,6]
# name.sort()
# print(name)

#.append()
# adds data in last of a list

#.insert()
# used to insert data in a list

# name=['oi','oy','oe']
# name.insert(1,"hey")
# print(name)

#.extend used to extend data in list

# name=['rajan','srijal']
# caste=['magar','laude']
# name.extend(caste)
# print(name)

# .remove
# name=["oi","rajan"]
# name.remove("oi")
# print(name)
#if there is similar element in a list it only removes the first one


#.pop()

# name=["jhilke","ram","shyam"]
# name.pop(1)
# print(name)

#default removes the last value

#del

# name=["rajna","rajan","plpl"]
# del name[0]
# print(name)

#.clear 
#it clear all list and give a empty list

#.reverse
# used to reverse a list
# first used sort to ascending and used reverse for desecnding

#.max,.min
#they give maximum and minimum element in a list.

# list joining 
# list1=list 2+list3


#.join 
#used to join a list and make it a string

#.copy()
# a=[5,3,2,3,5]
# b=a.copy()
# print(b)

#overwrite if there is data in b

#.count
#used to count in a list
#.index
#give the index in a list

# name=[4,1,25,6,7,6,6,12,6]
# print(name.count(6))
# i=0
# while i<len(name):
#     if name[i]==6:
#         print("index:",i)
#     i=i+1    

#TUPLE:
#   immutable
#   allow repetition
#   siliicing
#   small bracket]
# b=1,2,3,4,5 #still tuple andy

#single element tuple
# a=(10,)   #comma at last same for strning

#to change convert tuple into list and again to tuple

#unpacking a tuple 