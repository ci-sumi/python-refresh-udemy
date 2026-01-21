# print("hello world")
# print("python")
# print(10+5)
# name =input("enter your name?")
# print(name)
# Returns length of tuple and list
# print(len("sumi"))
# print(len([1,2,34,9]))
# Returns type
# print(type(10))
# print(type(3.5))
# print(type("hi"))
# Type convertion
# print(int("10"))
# print(float("3.5"))
# a=str(100)
# print(type(100))
# maximum and minimum
# print(max(3,7,5))
# print(min(3,7,5))
# sum
# s = sum((1,2,5))
# print(s)
# sorted
# a = sorted((8,4,5),reverse=True)
# print(a)
# range
# a=list(range(5))
# print(a)
# b =list(range(2,10,2))
# print(b)
# Absolute value
# print(abs(-10))
# print(round(3.6))
# a=any([True,False,True])
# print(a)
# b=all([True,True,True])
# print(b)
# names=["A","B"]
# for i,v in enumerate(names):
#     print(i,v) 
# a =["a","b"]
# b =[1,2]
# c=list(zip(a,b))
# print(c)
# Find the maximum numbers in the list
num=[3,7,2,9,5]
def fun(num):
    maximum=num[0]
    for n in num:
        print(n)
        if n>maximum:
            print(n,maximum)
            maximum=n
        print("Updated max to:", maximum)
    
    return maximum

result =fun(num)
print(result)        
    

 






