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
# Write a Python function that takes a list of integers and returns a new list containing only the numbers that appear more than once, without duplicates in the result.

#Input: [1, 2, 3, 2, 4, 5, 1, 6]
# n=[1, 2, 3, 2, 4, 5, 1, 6]
# s =[]
# for i in n:
#       if n.count(i)>1 and i not in s:
#             s.append(i)
# print(s)
# def find_duplicate(n):
#       s=[]
#       for i in n:
#             if n.count(i)>0 and i not in s:
#                   s.append(i)
#       return s

# numbers=[1,2,3,3]
# print(find_duplicate(numbers))

# Write a Python function that takes a string and returns True if it is a palindrome, and False otherwise. 
# def palindrome_or_not(n):
#       s =(n[::-1])
#       if s==n:
#             return True
#       else:
#             return False
      
            
                    
# word =input("Enter the word:").lower()
# result= palindrome_or_not(word)
# print(result)


#Write a program function that takes a list of numbers and returns the  largest

# def largest(n):
#       max=n[0]
#       for i in n:
#             if i>max:
#                   max=i
#       return max

# print(largest([1,2,3,4]))
#Write a program function that takes a list of numbers and returns the second largest


# def second_largest(n):
#       largest=n[0]
#       second_largest=n[0]
#       for i in n:
#             if i>largest:
#                   second_largest=largest
#                   largest=i
#             elif i>second_largest and i!=largest:
#                   second_largest=i
#       return second_largest

# print(second_largest([1,2,3,4]))
#fstring
# sumi="Helllo sumi"
# print(f"hello{sumi}")
#Strings
# first_name="Bro"
# food="pizza"
# email="hello@gmail.com"
# #Integers
# age=37
# quantity=3
# # print(f"You are {age}old")
# print(f"You are buying {quantity} items")
# print("------")
# print(f"You are buying {quantity} items")
#Float
# price =10.99
# gpa = 3.2
# print(f"The price is ${price}")
# print(f"Your gpa is {gpa}")
#Boolean
# is_student =True
# print(f"Are you a student:{is_student}")
# if is_student:
#       print("You are a student")
# else:
#       print("You are not a student")
#Key ponts about for loops
# for variable in sequences:
#Iterate over a list
# numbers=[1,2,3,4]
# for i in numbers:
#       print(numbers)
# for letter in "python":
#       print(letter)
# for i in range(5):
#       print(i)
# Sum of first N numbers
# Input: N = 5
# Output: 1 + 2 + 3 + 4 + 5 = 15

# sum=0
# for i in range(1,6):
#       sum=sum+i
# print(sum)
      

# Print even numbers from 1 to 20
# for i in range(1,21):
#       if i%2==0:
#             print(i)
#       else:
#             continue

# Find the largest number in a list
# Input: [3, 7, 2, 9, 5] → Output: 9
# n=[3, 7, 2, 9, 5]
# max=n[0] 
# for i in [3,7,2,9,5]:
#       if i>max:
#             max=i

# print(max)
      

# Reverse a string using a loop
# Input: "Python" → Output: "nohtyP"
string ="python"
# revers=(string[::-1])
# print(revers)
# reverse_string=""

# for char in string:
#             reverse_string = char+reverse_string
# print(reverse_string)

      

# Nested loop problem:
# Print a 5x5 multiplication table
# for i in range(1,6):
#       for j in range(1,6):
#             print(i*j,end=" ")
#       print()
      
#Typecasting  is the process of converting a variable from one datatype to another
#str(),int(),float(),bool()
# name=""
# age=37
# gpa=3.2
# is_student =True

# gpa=int(gpa)
# print(type(gpa))
# age=float(age)
# print(age)
# age=str(age)
# print(type(age))
# age=age+"1"
# print(age)
# name=bool(name)
# print(name)
#Write a program that counts vowels in a string
# input ="pythonu"
# vowels=["a","e","i","o","u"]
# count=0
# string=""
# for char in input:
#       if char in vowels:
#             count+=1
#             string=char+string
# print(count,string)
# Find the sum of even numbers from 1 to 50.
# sum=0
# for i in range(1,51):
#       if i%2==0:
#             sum=sum+i
# print(sum)
            
# Count how many numbers are greater than 10.
# numbers = [4, 12, 7, 18, 3, 25]
# count=0
# for i in numbers:
#       if i>10:
#             count=count+1
# print(count)
# Find the Second Smallest Number
# number=[1,2,3]
# largest=number[0]
# second_largest=number[0]
# for i in number:
#       if i>largest:
#             second_largest=largest
#             largest=i
            
#       elif i>second_largest and second_largest!=largest:
#             second_largest=i
# print(second_largest)
# //print pattern
# for i in range(1,6):
#             print(i*"*",end="")
#             print()
# Remove Duplicates From a List
# numbers = [1, 2, 2, 3, 4, 4, 5]
# list=[]
# for i in numbers:
#       if i not in list:
#             list.append(i)
             
            
# print(list)

#input
# name=input("Enetr your name:? ")
# print(f"hello {name}")
# age =int(input("How old are you? "))
# age=age+1
# print(f"you are {age} old")
# print("Happy Birthday")
#Rectange area calculation
# length=int(input("Enter the rectangle length:"))
# width=int(input("Enter the width of the rectangle:"))
# area=length*width
# print(f"Area of Rectangle is {area}cm")
#Exercise 2 shopping cart Program
# item=input("Enter the item you woud like to buy:?")
# price=float(input("Enter the price of item:? "))
# quantity =float(input("Enter the numbers you want:? "))
# total=price*quantity
# print(f"You have bought {item}x {quantity}/s")
# total = print(f"The total is ${total}")
# Find the Most Frequent Character in a String
# input ="programming"
# char_input={}
# for char in input:
#       if char in char_input:
#             char_input[char]+=1
#       else:
#             char_input[char]=1

# max_count=0
# char_fre=""
# for char,count in char_input.items:
#       if count>max_count:
#             max_count=count
#             char_fre=char
# print(f"Most frequent character:{max_count}{char_fre}")
##Madlib game
# adjective1=input("Enter an adjective(description)")
# noun1=input("Enter a noun-person or place or thing")
# adjective2=input("Enter an adjective(description)")
# verb1=input("Enter a verb ending with 'ing'")
# adjective3=input("Enter an adjective (description)")

# print(f"I went to a {adjective1}house")
# print(f"In an exhibit,i saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"i was {adjective3}")
# input="programming"
# char_count={}
# for char in input:
#       if char in char_count:
#             char_count[char]+=1
#       else:
#             char_count[char]=1
# max_count=0
# char_fre=""
# for char,count in char_count.items():
#       if count>=max_count:
#             max_count=count
#             char_fre=char
#       print(f"the frequent letter {char_fre} and count {max_count}")
# friends=9
# friends+=1
# print(friends)
# friends-=2
# print(friends)
# friends*=5
# print(friends)
# friends/=2
# print(friends)
# friends**=3
# print(friends)
# friends%=2
# print(friends)
x=3.14
y=4
z=5
# result=round(x)
# print(result)
# result=abs(y)
# print(result)
# result=pow(y,3)
# print(result)
# result=max(x,y,z)
# print(result)
import math
# print(math.pi)
# print(math.e)
x=81.5
# result=math.sqrt(x)
# print(result)
# result=math.ceil(x)
# print(result)
# result=math.floor(x)
# print(result)
#circumferences of a circle
# import math
# radius=int(input("Enter the radius of the circle?:"))
# circumference=2*math.pi*radius
# print(f"The circumference of a circle is {round(circumference,2)}cm")
#Area of a circle
#2pir
# import math
# radius=float(input("Enter the radius of a circle:?"))
# area=2*math.pi*pow(radius,2)
# print(f"The are of the circle {round(area,2)}")
#hy of a triangle
# import math
# a=float(input("Enter the value of a:?"))
# b=float(input("Enter the value of b:?"))
# c=math.sqrt((pow(a,2)+pow(b,2)))
# print(c)
#Print all the elements in the list
#To do
#1️⃣ Print all elements in a list 
# 2️⃣ Print first and last element 
# 3️⃣ Count even numbers
# 4️⃣ Find sum of elements 
# 5️⃣ Find average 
# 6️⃣ Reverse a list (without reverse())
# 7️⃣ Find maximum number 
# 8️⃣ Find minimum number
# 9️⃣ Check if element exists 
# 🔟 Replace an element at a specific index
# numbers = [10, 25, 4, 8, 15, 3, 20]
# # print(*numbers," ")
# for num in numbers:
#       print(*num,' ')
# cars=['volvo','bmw','alto']
# cars.sort(reverse=True)
# # for i in cars:
# #       print(i)
# print(cars)
# 2️⃣ Print first and last element
# numbers= [10,20,30]
# n1=numbers[0]
# n2=numbers[2]
# print(f"First and lat number number{n1} and{n2}")

#  3️⃣ Count even numbers
# numbers = [1,2,3,4,5,6]
# count=0
# for i in numbers:
#       if i%2==0:
#             count+=1
# print(f"The number of even numbers ",count)
# 4️⃣ Find sum of elements 
# numbers= [1,2,3,45,6]
# sum=0
# for i in numbers:
#       sum=sum+i
# print(f"The sum of the numbers:",sum)

# 5️⃣ Find average 
# numbers= [1,2,3,45,6]
# sum=0
# for i in numbers:
#       sum=sum+i
# avg=sum/len(numbers)
# print(f"The avg of numers is",sum,avg)
# 6️⃣ Reverse a list (without reverse())
# numbers =[1,2,34,5]
# reversed_list=numbers[::-1]
# print("The reverse_list",reversed_list)

# Find maximum number
# numbers = [10, 25, 4, 8, 15, 3, 20]
# max=numbers[0]
# min=numbers[0]
# for i in numbers:
#       if i>max:
#             max=i
#       if i<min:
#             min=i
            
# print(f"The maximum numer in the list is",max,min)

# # 9️⃣ Check if an element exists in a list
# numbers = [10, 25, 4, 8, 15, 3, 20]
# if 14 in numbers:
#       print("The number is found")
# else:
#       print("The number is not found")

# numbers=[]
# for i in input().split():
#       numbers.append(i)
# print("The list",numbers)
# index=int(input("Enter the index value:"))
# value_replace=int(input("Enter a  new value"))
# numbers[index]=value_replace

# print("The new numbers list",numbers)

# numbers = list(map(int,input("Enter the numbers:").split(",")))
# print(numbers)
# index=int(input("Enter the index value:"))
# value=int(input("Enter the value:"))
# if 0<=index and index<=len(numbers):
#       print("condition is true")
#       numbers.insert(index,value)
# print(numbers)
# Take a list of numbers and remove all duplicates.
# numbers=list((map(int,input("Enter the numbers:?").split(","))))
# print(numbers)
# checke_list=[]
# for i in numbers:
#       if i not in checke_list:
#             checke_list.append(i)
# print(checke_list)

# Intermediate Level

# Take a list of numbers and remove all duplicates.

# Find the largest and smallest number in a list without using max() or min().

# Merge two lists entered by the user and sort them in ascending order.

# Take a list of numbers and create a new list with squares of each number.

# Take a list and insert a value at a specific index (like the problem we just fixed).

# Challenging Level

# Find the second largest number in a list.

# Take a list of strings and sort them by length.

# Take a list of numbers and shift all zeros to the end while keeping the order of other numbers.

# Take a list and split it into two halves. If the list has an odd number of elements, the first half should have one more element.

# Implement a simple stack using a list and perform push and pop operations based on user input.
      
# thislist=["apple","banana","cherry"]
# for i in range(len(thislist)):
#       print(thislist[i])
# thislist=["apple","banana","cherry"]
# i=0
# while i<len(thislist):
#       print(thislist[i])
#       i=i+1
# thislist=["appple","banana","cherry"]
# [print(x) for x in thislist]
# List Comprehension
# fruits= ["apple","banana","cherry","mango"]
# newlist=[]
# for x in fruits:
#       if "a" in x:
#             newlist.append(x)
# print(newlist)
# fruits=["apple","banana","cherry","kiwi","mango"]
# new_list=[x for x in fruits if "a" in x]
# print(new_list)
# fruits=["apple","banana","cherry","kiwi","mango"]
# new_list=[x for x in fruits if "apple" !=x]
# print(new_list)
# fruits=["apple","banana","cherry","kiwi","mango"]
# new_list=[x for x in fruits]
# print(new_list)
# new_list=[x for x in range(10) if x<5]
# print(new_list)
# fruits=["apple","banan","cherry","kiwi","mango"]
# new_list=[x.upper() for x in fruits]
# print(new_list)
# fruits=["apple","banana","cherry","kiwi","mango"]
# # new_list=['hello' for x in fruits]
# # print(new_list)
# new_list=[x if x!='banana' else 'orange' for x in fruits]
# print(new_list)
#Calculator program
# operator =input("Enter the option '+ - * / %' ")
# input1 =float(input("Enter the first value:? "))
# input2= float(input("Enter the second value:? "))
# if operator=="+":
#       result=input1+input2
# elif operator=="-":
#       result=input1-input2
# elif operator=="*":
#       result=input1*input2
# elif operator=="/":
#       result=input1/input2
# elif operator=="%":
#       result=input1%input2
# else:
#       print(f"This {operator} is invalid")

# print(f"the result of {input1},{input2} is {result}")
# thislist=["orange","mango","kiwi","people"]
# thislist.sort()
# print(thislist)
# thislist=[100,50,65,82,23]
# thislist.sort()
# print(thislist)
# for i in range(3):
#       print(i)
      
#Bubble sort
# my_list=list(map(int,input("Enter the numbers for sort:").split(",")))
# print(my_list)
# n=len(my_list)
# for i in range(n):
#       swapped=False
#       for j in range(n-i-1):
#             if my_list[j]>my_list[j+1]:
#                   my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
#                   swapped=True
#       if not swapped:
#             break
            
# print(my_list)
# thislist=["orange","mango","kiwi","pineapple","banana"]
# # thislist.sort()
# # print(thislist)
# thislist.sort(reverse=True)
# print(thislist)
# def myfun(n):
#       return abs(n-50)
# thislist=[100,50,65,82,23]
# thislist.sort(key=myfun)
# print(thislist)
# thislist=["Banana","Orange","kiwi","cherry"]
# thislist.sort(key=str.lower)
# print(thislist)
# python converter
# weight= float(input("Enter your weight:"))
# unit=input("Enter the unit:?")
# if unit=="k":
#       weight=weight *2.25
#       unit="Lbs"
#       print(f"Your weight is:{round(weight,1)}{unit}")
# elif unit=="L":
#       weight=weight/2.05
#       unit="kgs."
#       print(f"Your weight is:{round(weight,1)}{unit}")
# else:
#       print(f"{unit} was not valid")
#Copy Lists
# thislist=["apple","banana","cherry"]
# mylist=thislist.copy()
# print(mylist)
# thislist=['appple','banana','cherry']
# my_lst=list(thislist)
# print(my_lst)
# thislist=["appple","banana","cherry"]
# mylist=thislist[:]
# print(mylist)
#Join Lists
# list1=["a","b","c"]
# list2=[1,2,3]
# list3=list1+list2
# print(list3)
# list1=["a","b","c"]
# list2=[1,2,3]
# for x in list1:
#       list2.append(x)
# print(list2)
# extend()
# list1=["a","b","c","d"]
# list2=[1,2,3]
# list1.extend(list2)
# print(list1)
# Create and print a list

# Create a list of your 5 favorite fruits and print it.
fruits=["apple","orange","mango","jackfruit","kiwi"]
# print(fruits)
# //Access elements

# Print the first, last, and middle elements of a list:
# print(fruits[0])
# print(fruits[2])
# print(fruits[4])
# fruits.append('chakka')
# print(fruits)
# fruits.pop(1)
# print(fruits)
# # Find the number of elements in a list.
# print(len(fruits))
# numbers = [2, 4, 6, 8, 10]
# sum=0
# for i in numbers:
#       sum=sum+i
# print(sum)

# def sum(*n):
#       first_value=0
#       for i in n:
#             first_value=i+first_value
#       return first_value

# print(sum(1,2,3,4,5,6,7,8,9))
# def my_sum(a,b,c):
#       s=a+b+c
#       return s

# print("Total is :",my_sum(3,4,5))
# passing of efault arguments
# def student(name,age,grade='five',school="st'Marys"):
#       print('student Details:',name,age,grade,school)
      
# student('sume',37)
# name=input("enter your name:")
# while(name==""):
#       print("You didnt enter a name")
#       name=input("enter your name:")

# print(f"hai {name }")
# Print numbers 1 to 10
# Use a while loop to print numbers from 1 to 10.
# x=1
# while x<11:
#       print(x)
#       x=x+1
# Sum of first n numbers
# # Ask the user for a number n, then calculate the sum from 1 to n using a while loop.
# number = int(input("Enter the numbers:"))
# x=0
# sum=0
# while x<number:
#       x=x+1
#       sum=sum+x
# print(sum)
# Even numbers up to 20
# Print all even numbers from 1 to 20 using a while loop.
# x=0
# while x<=20:
#       if x%2==0:
#             print(x)
#       x=x+1
# Countdown timer
# Print numbers from 10 down to 1, then print "Blast off!".
# x=10
# while x>=1:
#       print(x)
#       x=x-1
# print("Blastoff")
# Multiplication table
# Ask the user for a number and print its multiplication table up to 10.
# n=int(input("Enter the number:"))
# i=1
# while i<=10:
#       print(n,"x",i,"=",n*i)
#       i=i+1
# Reverse a number
# Example: input 1234 → output 4321 (using a while loop).
# number=int(input("Enter the number:"))
# reverse=0
# while number>0:
#       digit=number%10
#       reverse=reverse*10+digit
      
#       number=number//10
# print(reverse)
# Count digits
# Ask for a number and count how many digits it has.
# number=int(input("Enter the number:"))
# count=0
# reverse=0
# while number>0:
#       digit=number%10
#       reverse=reverse*10+digit
#       count=count+1
#       number=number//10
# print(count)
# Sum of digits
# Example: input 123 → output 6.

# number=int(input("Enter the number:"))
# sum=0
# while number>0:
#       digit=number%10
#       sum=sum+digit
#       number=number//10
# print(sum)
# number=int(input("Enter the number:"))
# count=0
# while number>0:
#       digit=number%10
#       count=count+1
#       number=number//10
# print(count)
# Guess the number game
# Generate a secret number (1–100). Keep asking the user to guess until they get it right.
# import random
# random_number=random.randint(1,100)
# print(random_number)
# number=int(input("Enter the guess number:"))
# while number>0:
#       if number!=random_number:
#             number=int(input("Enter the guess number:"))
#       break

# print("The guessed number is correct")
# Check for palindrome number
# Example: 121 → palindrome, 123 → not.
# number=int(input("Enter the number:"))
# reverse=0
# actual=number
# while number>0:
#       digit=number%10
#       reverse=reverse*10+digit
#       number=number//10

# print(number)
# print(reverse)

# if actual==reverse:
#       print("Its a palindrome")
# else:
#       print("Its not a palindrome")
# Factorial using while loop
# Compute n! using a while loop.
# n=int(input("Enter the number:"))
# i=0
# while n>0:
#       fact=n*(n-1)
#       n=n-1
# print(fact)
# fact=0
# n=int(input("Enter the number:"))
# for i in n:
#       fact=n*(n-1)
#       i=i-1
# print(fact)
# Practice Problem: Write a Python function that accepts two integer numbers. 
# If the product of the two numbers is 
# less than or equal to 1000, return their product; otherwise, return their sum.
      
# def two_integers(a,b):
#       if a*b>=1000:
#             return a*b
#       else:
#             return a+b

# print(two_integers(4,30))
#  Iterate through the first 10 numbers (0–9). In each iteration, 
#  print the current number, the previous number, and their sum.

# print("Printing current and previous number sum in a range(10)")
# sum=0
# for i in range(1,10):
#       p=i-1
#       sum=sum+i
#       print(f"current Number{i} previous Number{p} sum is {i+p}")
# print(sum)
# n=int(input("Enter the number:"))
# i=1
# factorial=1
# while i<=n:
#       factorial=factorial*i
#       i+=1
# print("factorial",factorial)
# Keep asking until valid input
# Keep asking the user for a number greater than 0. 
# Only stop when they enter a valid number.
# n=int(input("Enter a value greater than 0:"))
# while n<=0:
#       print("You didn't enter the number greater than 0")
#       n=int(input("Enter a value greater than 0:"))
#       if n>0:
#             break
# Prime number check
# Determine if a number is prime using a while loop. 

# Print numbers 1 to 10
# Use a for loop to print numbers from 1 to 10. 
# for i in range(1,11):
#       print(i)
# Print even numbers
# Print all even numbers from 1 to 20.
# for i in range(1,21):
#       if i%2==0:
#             print(i)
# Sum of first n numbers
# Ask the user for n, then find the sum from 1 to n.
# n=int(input("Enter the n:"))
# sum=0
# for i in range(1,n+1):
#       sum=sum+i
# print(sum)

# Print a multiplication table
# Ask for a number and print its table up to 10.
# n=int(input("Enter a numer:"))
# i=1
# while(i<=10):
#       print(i*n)
#       i=i+1
# n=int(input("Enter a number:"))

# for i in range(1,11):
#       print(i*n)
#       i=i+1
# Display only those characters which are present at an even index number
# in given string.
# input="pynative"
# # output=input[::2]
# # print(output)
# for i in range(0,len(input),2):
#       print(input[i])
# String Slicing and Substring Removal
# Practice Problem: Write a function to remove characters from a string starting
# from index 0 up to n and return a new string.
# def string_slicing(word,n):
#       print(f"{word}")
#       res=word[n:]
#       return res

# print(string_slicing("pynative", 4))
# print(string_slicing("pynative", 2))


      
      




      
      
     

                  
                  

            
            
