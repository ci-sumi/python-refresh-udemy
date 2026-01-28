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
# num=[3,7,2,9,5]
# def fun(num):
#     maximum=num[0]
#     for n in num:
#         print(n)
#         if n>maximum:
#             print(n,maximum)
#             maximum=n
#         print("Updated max to:", maximum)
    
#     return maximum

# result =fun(num)
# print(result)        
    
# a = [1,2,3]
# b=a
# b.append(4)
# print(a)
# Swap the values of two variables without using a temporary variable.
# a =2
# b =5
# a =a+b
# print(a)
# b =a-b
# print(b)
# a =a-b
# print(a)

# print(a,b)
# Write a program to print all numbers from 1 to 50 that are divisible by 3 but not by 5.

# for i in range(1,51):
#     if i%3==0:
#         if i%5!=0:
#             print(i)

# def numbers(r,s):
#     b=[]
#     for i in range(r,s):
#         if i%3==0 and i%5!=0:
#             b.append(i)
#     return[b]
    
# n=numbers(1,51)
# print(n)
# Check if a number entered by the user is a prime number.
# import math
# def prime(n):
#     if n<=1:
#         print("its not a prime number")
#         return
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i ==0:
#             print("its not a prime number")
#             return
#         print("its a prime number")


# prime(11)
# Python pyramid

# def pyramid(n):
#     for i in range(1,n+1):
#         spaces = n-i
#         stars = 2*i-1
#     print(" " *spaces+"*"*stars)

        
# pyramid(7)      

# text = input("enter a word").lower()
# count=0
# for char in text:
#     if char in "aeiou":
#         count+=1
# print("Number of vowels",count)
# text = input("enter the word? ").lower()
# count=0
# for char in text:
#     if char in 'aeiou':
#         count+=1
# print("The number of vowels",count)
# sentence = input("Enter the sentence: ").lower()
# words = sentence.split()
# word_count = {}

# for word in words:
#     if word in word_count:
#         current_count = word_count[word]
#     else:
#         current_count = 0
#     word_count[word] = current_count + 1  # This line actually adds the word to the dictionary

# print("Repeated words and their counts:")
# for word, count in word_count.items():
#     if count > 1:
#         print(word, ":", count)

# sentence = input("Enter the sentence:").lower()
# words=sentence.split()
# word_count={}
# for word in words:
#     if word in word_count:
#         current_count =word_count[word]
#     else:
#         current_count=0
#     word_count[word]=current_count+1
    
# for word,count in word_count.items():
#     if count>0:
#         print(word,count)
# Write a Python program that:

# Takes a string as input

# Counts how many times each character appears

# Prints only the characters that appear more than once

# Ignore spaces
# text =input("Enter a word: ").lower()
# word_count ={}

    
# for word in text:
#     if word=="":
#         continue
#     if word in word_count:
#         current_count = word_count[word]
#     else:
#         current_count =0
#     word_count[word] = current_count+1
# for word,count in word_count.items():
#     if count>0:
#         print("word : count",word,count)
# Write a function that always returns 5

# Sounds easy right? Just bear in mind that 
# you can't use any of the following characters: 0123456789*+-/
# Unique Pairs with Sum
# Write a Python program that:

# Takes a list of numbers as input from the user (comma-separated).

# Takes a target sum as input.

# Finds and prints all unique pairs of numbers in the list that add up to the target sum.

# Each pair should be printed only once, regardless of order.
# print("print('what to print')")

# numbers = input("Enter the numbrs comma separated:").split(",")
# numbers =[int(num) for num in numbers]
# target=int(input("enter the target sum:"))

# print(numbers)
# print(target)
# numbers = input("Enter the numbrs comma separated:").split(",")
# target =int(input("Enter the target sum:"))
# numbersre =[]
# for num in numbers:
#     numbersre.append(int(num))
# numbers =numbersre
# print(numbers)
# seen =set()
# pairs =[]
# for num in numbers:
#     complement = target-num
#     if complement in numbers and (min(num,complement),max(num,complement)) not in seen:
#         seen.add((min(num,complement),max(num,complement)))
#         pairs.append((min(num,complement),max(num,complement)))

# print(pairs)
Vms =[{"name":"Vm-1","status":"Running"},
      {"name":"Vm-2","status":"Stopped"},
      {"name":"Vm-3","status":"Running"},
      {"name":"Vm-4","status":"Terminated"}]
# Running VMs: 2
# Stopped VMs: 1
# Running VM Names:
# vm-1
# vm-3
# running_vm=0
# stopping_vm=0
# runnin_vms=[]
# for vm in Vms:
#     if vm["status"]=="Running":
#         running_vm+=1
#         runnin_vms.append(vm["name"])
#     elif vm["status"]=="Stopped":
#         stopping_vm+=1
    
# print(f"Running Vms:{running_vm}")
# print(f"Stopping Vms:{stopping_vm}")
# for name in runnin_vms:
#     print(name)
# cpu_utilization =[80,65,70,90,75]
# cpu_total=0
# for cpu in cpu_utilization:
#     cpu_total =cpu_total+cpu
# print(cpu_total)
# average_cpu_total = cpu_total/len(cpu_utilization)
# if average_cpu_total>70:
#     print("Scale up")
# else:
#     print("Scale down")




# 4. Write a program to take a number as input and display its square and cube.

# 1. Write a Python program to print 'Welcome to Python Programming'.
# print("welcome to python progaramming")
# 2. Write a program to take user name as input and print a greeting message.
# name =input("Enter your name:")
# print(f"welcome {name} to python programming")
# 3. Write a program to take two numbers as input and print their sum, difference, product, and
# # division.
# number1 =int(input("Enter te first number:"))
# number2 = int(input("Enter the second number:"))
# sum=number1+number2
# diff = number2-number1
# product = number1* number2
# division = number2/number1
# print(sum)
# print(diff)
# print(product)
# print(diff)
# print(division)
# 4. Write a program to take a number as input and display its square and cube.
# number1 = int(input("Enter a number:"))
# square_root = number1**2
# cube_root = number1**3
# print (f"square_root of a number,cube_root ",square_root,cube_root)

# 5. Write a program to take user age as input and print it.
# age = int(input("Enter your age:"))
# print(f"your age is:{age}")

