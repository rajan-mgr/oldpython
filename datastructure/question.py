#WAP to find sum of common element in two list

a=[2,3,1,5,6,7]
b=[3,5,7,8,10]
sum=0
for i in a:
    if i in b:
        print("Common found",i)
        sum=sum+i
print(sum)