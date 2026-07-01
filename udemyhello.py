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
# Factorial using for loop
# Compute n! using a for loop.
# n=int(input("Enter the number for finding factorial:"))
# fact=1
# for i in range(1,n+1):
#       fact=fact*i
# print(fact)
# Reverse a number (using for loop)
# Same as before, but try with a for loop.
# Count digits in a number
# n=int(input("Enter the number:"))
# count=0
# while n>0:
#       n=n//10
#       count=count+1
      
# print(count)
# Reverse a string
# Example: "hello" → "olleh"
# def reverse_string(n):
#       reversed=n[::-1]
#       return reversed
      

# print(reverse_string("hello"))
# input=input("Enter a string:")
# reversed=""
# for char in input:
#       revers=char+reversed
     
#       print(revers)
#God increase me in my knowledge


# print("Hello world")
# Practice Problem: Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

# def product(a,b):
#       if a*b<=1000:
#             return a*b
#       else:
#             return a+b


# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of b:"))  
# print(product(a,b))
#  Cumulative Sum of a Range
# Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.
  
# def cumilative():
#       sum=0
#       previous=0
#       print("Printing current and previous number sum in a range(10)")
#       for i in range(1,10):
#             print(i)
#             sum=previous+i
#             previous=i
#             print(f"Current Number{i} Previous Number {previous} Sum is {sum}")

# cumilative()
# Display only those characters which are present at an even index number in given string.
# Understand how data is stored in memory using zero-based indexing. In most languages, the first character is at position 0, the second at 1, and so on. Mastering indexing is vital for data parsing
# def displayeven(input_data):
#       print(f"Original string is{input_data}")
#       even_char=input_data[0::2]
#       for char in even_char:
#             print(char)
                  


# input_data=input("Enter a Srtring:")
# displayeven(input_data)

# String Slicing and Substring Removal
# Practice Problem: Write a function to remove characters from a string starting from index 0 up to n and return a new string.
     
# def remove_string(word,n):
#       size=len(word)
#       remove=word[n:]
#       return remove



# word=input("Enter the word:")
# n=int(input("Enter the position:"))
# print(remove_string(word,n))
                  
                  
# Write a program to swap the values of two variables, a and b, without using a third temporary variable.
# def swap_numbers(a,b):
#       print(f"Print the numbers before swap:a={a},b={b}")
#       a,b=b,a
#       print(f"Print the numbers after swap:a={a},b={b}")
            
# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of b:"))
# swap_numbers(a,b)      
#  Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.
# def fact_number(n):
#       fact=1
#       for i in range(1,n+1):
#             fact=fact*i
#             print(fact)

# n=int(input("Enter the number:"))      
      
# fact_number(n)
# Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# fruits.append("fig")
# print(fruits)
# fruits.remove("banana")
# print(fruits)
# fruits.pop(2)
# print(fruits)
# Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).
# word="python"
# reverse=word[::-1]
# print(reverse)
# for char in reverse:
#       print(char)
# Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.
# vowels=["a","e","i","o","u"]
# Given_string="Learning Python is fun!"
# count=0
# for i in Given_string:
#       if i.lower() in vowels:
#             count=count+1
# print(f"The number of vowels:{count}")
# Exercise 10. Finding Extremes (Min/Max) in a List
# Given a list of integers, find and print both the largest and the smallest numbers.
# nums = [45, 2, 89, 12, 7]
# i_max=nums[0]
# i_min=nums[0]
# for i in nums:
#       if i>i_max:
#             i_max=i
#       if i<i_min:
#             i_min=i
# print(i_max)
# print(i_min)
# largest=max(nums)
# smallest=min(nums)
# print(largest)
# print(smallest)
# Removing Duplicates from a List
# data = [1, 2, 2, 3, 4, 4, 4, 5]
# unique_numbers=list(set(data))
# print(data)
# print(unique_numbers)
# empt_list=[]
# for i in data:
#       if i not in empt_list:
#             empt_list.append(i)
# print(empt_list)
# values='sumisumi'
# remove_string=""
# for char in values:
#       if char not in remove_string:
#             remove_string+=char

# answer="".join(set(values))
            
# print(answer)
# values = "sumisumi"
# result = "".join(dict.fromkeys(values))
# print(result)
# str_x = "Emma is good developer. Emma is a writer"
# string_count=str_x.count("Emma")
# print(string_count)
# def pattern(a,b):
#       for i in range(a,b+1):
#             for j in range(i):
#                   print(i,end="")
#             print("\n")
# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# pattern(a,b)

# string="hello"
# reversed_string=string[::-1]
# print(reversed_string)
# num=123
# revese_num=str(num)
# revese_num_answer=revese_num[::-1]
# print(revese_num_answer)

# def number(a):
#       revers=0
#       while a>0:
#             digit=a%10
#             revers=revers*10+digit
#             a=a//10
#       return revers
# a=int(input("Enter a number:"))
# print(number(a))
# for i in range(1,11):
#       for j in range(1,10):
#             print(i*j,end="\t")
#       print("")
# for i in range(5,0,-1):
#       for j in range(i):
#             print("*",end=" ")
#       print("")
# def exponent(base,exp):
#       num=exp
#       result=1
#       while num>0:
#             result=result*base
#             num=num-1
#       return result

# print(exponent(2,5))

# def fib(n):
#       num1=0
#       num2=1
#       for i in range(n):
#             print(num1, end=" ")
#             result=num1+num2
#             num1=num2
#             num2=result


# n=int(input("enter the number:"))
# print(fib(n))
# dict1 = {"name": "Alice", "age": 25}
# dict2 = {"city": "New York", "job": "Engineer"}

# dic=dict1 | dict2
# print(dic)
# text = "apple banana apple cherry banana apple"
# # answer=text.count("apple")
# # print(answer)
# word=text.split()
# frequency={}
# for w in  word:
#       if w in frequency:
#             frequency[w]+=1
#       else:
#             frequency[w]=1
# print(f"{w} and frequency{frequency}")
# import math
# def prime(n):
#       if n<=1:
#             return False
#       else:
#             for i in range(2,int(math.sqrt(n))+1):
#                   if n%i==0:
#                         return False
#             return True

# n=int(input("Enter the number:"))
# print(prime(n))
# user_sentence= 'hello sumi'
# answer=user_sentence.replace(" ","_")
# print(answer)
# rows = 6
# # Outer loop for number of rows
# for i in range(rows, 0, -1):
#     # Inner loop for printing numbers in each row
#     for j in range(i, 0, -1):
#         print(j, end=' ')
#     print("") # New line
# text = "hello world from python"
# cap =text.capitalize()
# actual=[]
# print(cap)
# words=text.split()
# for word in words:
#       wxample=word.capitalize()
#       actual.append(wxample)
# print(actual)

# find=" ".join(actual)
# print(find)
# import time
# count=5
# while count>0:
#       print(count)
#       time.sleep(1)
#       count-=1
# print("Blast")
# with open("notes.txt","w") as file:
#       file.write("Hello,this is my first note.\n")
#       file.write("python file handling is simple.\n")
#       file.write("End of file \n")
# print("Reading file contents")
# with open("notes.txt","r") as file:
#       context=file.read()
#       print(context)
# try:
#       with open("sample.txt","r") as file:
#             words=file.read()
#             answer=words.split()
#             word_count=len(answer)
#             print(word_count)
# except FileNotFoundError:
#       print("File not found")

# class Car:
#       def __init__(self,make,model,year):
#             self.make=make
#             self.model=model
#             self.year=year
#       def start_engine(self):
#             print(f"The{self.year} {self.make} {self.model}")
# my_car =Car("Toyota","camry",2022)
# my_car.start_engine()
# words = ["apple", "bat", "cherry", "dog", "elderberry"]
# filtered_words=[w.upper() for w in words if len(w)>=4 ]
# print(filtered_words)
# def merg_dict(d1,d2):
#       result=d1.copy()
#       for key,value in d2.items():
#             result[key]=result.get(key,0)+value
#       return result
# d1 = {'a': 10, 'b': 20}
# d2 = {'b': 5, 'c': 15}

# merged=merg_dict(d1,d2)
# print(merged)

# from collections import Counter
# def get_frequency(input_string):
#       clean_text=input_string.lower().replace(" ","")
      
#       return Counter(clean_text)

# text = "Python Programming"
# freq = get_frequency(text)
# print(freq)
# a=sorted("listen")
# b=sorted("silent")
# print(a)
# print(b)
# print('Name','is','James',sep="***")
# num=8
# print('%o'% num)
# num=45
# binary_value=f"{num:b}"
# print(binary_value)
# str1,str2,str3=input("Enter the three input values").split()
# print('Name:',str1)
# print('Name:',str2)
# print('Name:',str3)

# num=89
# hex=f'{num:x}'
# print(hex)
# num=458.541315
# print('%.2f'%num)
# num=int(input("Enter numerator:"))
# den=int(input("Enter a denominator:"))
# result=(num/den)*100

# print(f'The resultt is:{result:.2f}%')
# Text= 'REPORT SUMMARY'
# formatted_string=f'{Text:-^40}'

# print(formatted_string)
# i=1
# while(i<=10):
#       print(i)
#       i=i+1

# for i in range(-10,0,1):
#       print(i)

def sum_calculate(n):
      sum=0
      for i in range(1,n+1):
            sum=sum+i
      return sum
            
      
      
# n= int(input("Enter the upto which sum has to be calculated:"))
# final=sum_calculate(n)
# print(final)
# list1 = [10, 20, 30, 40, 50]
# # reversed=list1[::-1]
# # print(reversed)
# size=len(list1)-1

# for i in range(size,-1,-1):
#       print(list1[i])
# number= 75869
# largest=0
# smallest=9
# while(number>0):
#       digit=number%10
#       largest=max(largest,digit)
#       smallest=min(smallest,digit)
#       number=number//10
# print(largest)
# print(smallest)
# for i in range(1,6):
#       for j in range(1,i*2):
#             print(j,end=" ")
#       print("")
# for i in range(5,0,-1):
#       for j in range(i,0,-1):
#             print(j,end="")
#       print("")
# Given_Input=[1, 2, 3, 4]
# sum=0
# result_m=[]
# for i in Given_Input:
#       sum=sum+i
#       result_m.append(sum)
# print(result_m)
# nums=[1,2,3,4,5]
# k=2
# for _ in range(k):
#       first_element=nums.pop(0)
#       nums.append(first_element)
# print(nums)
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# sample_dict={}

# for i in sample_list:
#       if i in sample_dict:
#             sample_dict[i]+=1
#       else:
#             sample_dict[i]=1
# print(sample_dict)
# first_list = [2, 3, 4, 5, 6, 7, 8]
# print("First List ", first_list)
# second_list = [4, 9, 16, 25, 36, 49, 64]
# print("Second List ", second_list)
# result = zip(first_list, second_list)
# print(set(result))
# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
#          'july': 54, 'Aug': 44, 'Sept': 54}
# values= speed.values()
# print(values)
# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# answer_list=[]
# for i in sample_list:
#       if i not in answer_list:
#             answer_list.append(i)
# print(tuple(answer_list))
# minimum_value=min(answer_list)
# maximum_value=max(answer_list)
# print(minimum_value)
# print(maximum_value)
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# res=dict.fromkeys(employees,defaults)
# print(res)
# sampleDict = { 
#   "name": "Kelly",
#   "age":25, 
#   "salary": 8000, 
#   "city": "New york" }

# keys = ["name", "salary"]

# newDict = {k: sampleDict[k] for k in keys}
# print(newDict)
# mylist = [64, 34, 25, 12, 22, 11, 90, 5]
# n=len(mylist)
# for i in range(n):
#       for j in range(n-i-1):
#             if mylist[j]>mylist[j+1]:
#                   mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
# print(mylist)
# Input=[1, 2, 2, 3, 4, 4, 5]
# empt_list=[]
# for num in Input:
#       if num not in empt_list:
#             empt_list.append(num)
# print(empt_list)
# Input=[1, 2, 2, 3, 4, 4, 5]
# seen=[]
# duplictaes=[]
# for num in Input:
#       if num in seen:
#             if num not in duplictaes:
#                   duplictaes.append(num)
#       else:
#             seen.append(num)
# print(duplictaes)
# Input="banana"
# Output={'b':1, 'a':3, 'n':2}
# result={}  
# for i in Input:
#       if i in result:
#             result[i]+=1
#       else:
#             result[i]=1
# print(result)
# Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, 
# return their product; otherwise, return their sum.
# def product_sum(a,b):
#       if(a*b<=1000):
#             return a*b
#       else:
#             return a+b
# while True:
#       a=int(input("Enter the first number:"))
#       b=int(input("Enter the second number:"))     
#       if a>0 and b>0:
#             break
#       else:
#             print("Enter the possitive numbers only")    
# print(product_sum(a,b))

# Cumulative Sum of a Range
# Iterate through the first 10 numbers (0–9). In each iteration, 
# print the current number, the previous number, and their sum.
# def cumulative_sum(n):
#       Previous_Number=0
#       print("Printing current and previous number sum in a range(10)")
#       for Current_number in range(n):
#             Sum=Current_number+Previous_Number
#             print(f"Current Number{Current_number} Previous Number{Previous_Number} Sum:{Sum}")
#             Previous_Number=Current_number
                    
# n=int(input("Enter the range 10:"))
# cumulative_sum(n)
# Display only those characters 
# which are present at an even index number in given string.

# def display(a):
#       print(f"Original string is{a}")
#       print(f"Printing only even indexchars:")
#       result=a[::2]
#       for char in result:
#             print(char)
      
# a=input("Enter the String:")

# display(a)
# 
# Write a function to remove characters from a string starting 
# from index 0 up to n and return a new string.

# def remove_char(given_string,n):
#       result=given_string[n:]
#       print(result)
      
      
# # given_string=input("Enter a string")
# # n=int(input("Enter the value upto "))
# remove_char("pynative", 4)

# Write a program to swap the values of two variables, 
# a and b, without using a third temporary variable.
# def swap(a,b):
#       a,b=b,a
#       print(a,b)
      
# a=int(input("Enter your first number:"))
# b=int(input("Enter your second number:"))

# swap(a,b)
# Calculating Factorial with a Loop

# def fact(n):
#       fact=1
#       for i in range(fact,n+1):
#             fact=fact*i
#       return fact

# n=int(input("Enter the number:"))
# print(fact(n))
# List Manipulation: Add and Remove
#  Create a list of 5 fruits. Add a new fruit to the end of the list, 
#  then remove the second fruit (at index 1).
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# ex=("fig")
# fruits.insert(5,"fig")

# fruits.remove("banana")
# print(fruits)
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# fruits.pop(3)

# print(fruits)


# def fruit_add_remove(n):
#       fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#       fruits.append(n)
#       return fruits


# n=input("Enter the fruit to add to your list:")
# print(fruit_add_remove(n))

# def remove(n):
#       fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#       fruits.pop(n)

      
# String Reversal
# Write a program that takes a string and 
# reverses it (e.g., “Python” becomes “nohtyP”).

# def reverse_string(n):
#       result_string=n[::-1]
      
#       for char in result_string:
#             print(char)


# n=input("Enter a string:")
# reverse_string(n)
# def count_vowels(n):
#       vowels=['a','e','i','o','u']
#       count=0

#       for char in n:
#             if char in vowels:
#                   count=count+1
#       return count
      
# n=input("Enter the sentence:").lower()
# print(count_vowels(n))
# Finding Extremes (Min/Max) in a List
nums = [45, 2, 89, 12, 7]
# max=nums[0]
# min=nums[1]
# for i in range(len(nums)):
#       if nums[i]>nums[i+1]:
#             max=nums[i]
#             min=nums[i+1]
#       else:
#             max=nums[i+1]
#             min=nums[i]
# print(f"{max},{min}")
# def max_min(nums):
#       max=nums[0]
#       min=nums[0]
#       for num in nums:
#             if num>max:
#                   max=num
#             if num<min:
#                   min=num
#       print(f"Maximum value:{max} Minimum Value is:{min}")
      
# nums=list(map(int,input("Enter the numbers separted by space:").split(',')))
# max_min(nums)
# Removing Duplicates from a List
# def remove_duplicates(n):
#       newlist=[]
#       for num in n:
#             if num not in newlist:
#                   newlist.append(num)
#       return newlist
      
      
      

# n=list(map(int,input("Enter the numbers seperated by comma:").split(",")))
# print(remove_duplicates(n))
# List Comparison and Boolean Logic

# def comaprison(n1,n2):
#       # n_size=len(n1)
#       # n_size=len(n2)
#       if n1[-1]==n2[-1]:
#             return True
#       else:
#             return False
# n1=list(map(int,input("Enter the number of lists separated by comma:").split(",")))
# n2=list(map(int,input("Enter the number of lists separated by comma:").split(",")))
# print(comaprison(n1,n2))

# def comparison(n1):
#       if n1[0]==n1[-1]:
#             return True
#       else:
#             return False
      


# n1=list(map(int,input("Enter the numbers of a list comma separated:").split(",")))
# print(comparison(n1))
# Filtering Lists with Conditional Logic
# def div_5(n1):
#       new_list=[]
#       for num in n1:
#             if num%5==0:
#                   new_list.append(num)
#       return new_list
            
                  
# n1=list(map(int,input("Enetr the numbers:").split(",")))
# print(div_5(n1))
# def count(n1):
#       result=n1.count("writer")
#       return result


# n1=input("Eneter a string:")
# print(count(n1))
# Nested Loops for Pattern Generation
# for i in range(1,6):
#       for j in range(i):
#             print(i,end="")
#       print(" ")
# Write a program to check 
# if a given number is a palindrome 
# (reads the same forwards and backwards).
# def palindrom(n):
#       reversed=0
#       original=n
#       while n>0:
#             digit =n%10
#             reversed=reversed*10+digit
#             n=n//10
#       if original==reversed:
#             return True
#       else:
#             return False
# n=int(input("Enter the number:"))
# print(palindrom(n))


# def Merging_list(n1,n2):
#       my_new_list=[]
#       for num in n1:
#             if num%2!=0:
#                   my_new_list.append(num)
#       for num in n2:
#             if num%2==0:
#                   my_new_list.append(num)
#       return my_new_list
            
# n1=list(map(int,input("Enter the numbers:").split(",")))
# n2=list(map(int,input("Enter the numbers:").split(",")))
# print(Merging_list(n1,n2))
# Integer Digit Extraction and Reversal
# def extraction(n1):
#       while n1>0:
#             digit=n1%10
#             n1=n1//10
#             print(digit,end=" ")
                  
# n1=int(input("Enter the number:"))
# extraction(n1)
# Practice Problem: Calculate income tax for a given income based on these rules:

# First $10,000: 0% tax
# Next $10,000: 10% tax
# Remaining income: 20% tax


# def tax(amount):
#       tax_amount=0
#       if amount<=10000:
#             tax_amount=0
#       elif amount<=20000:
#             tax_amount=tax_amount+(amount-10000)*10/100
#       else:
#             tax_amount=(10000)*10/100
#             tax_amount=tax_amount+(amount-20000)*20/100
#       return tax_amount

# amount=int(input("Enter the amount:"))
# # tax_per=int(input("Enter the tax per_centage"))

# print(tax(amount))
      
# # Nested Loops for Multiplication Tables
# for i in range(1,11):
#       for j in range (1,11):
#             print(j*i,end=" ")
#       print(" ")
#  Downward Half-Pyramid Pattern
# for i in range(5,0,-1):
#       for j in range(i):
#             print("*",end=" ")
#       print(" ")
# Custom Exponentiation Function
# def expone(base,exp):
#       return base ** exp
      

# base=int(input("Enter the base:"))
# exp=int(input("Enter the exponential:"))

# print(expone(base,exp))
# Generate Fibonacci Series
# def fibonacci(n):
#       num1=0
#       num2=1
#       for i in range(n):
#             print(num1,end=" ")
#             res=num1+num2
#             num1=num2
#             num2=res
# n=int(input("Enter the number:"))
# fibonacci(n)
# def leap_year(year):
#       if (year%4==0 and year%100!=0) or (year%400==0):
#             return "Its a leap year"
#       else:
#             return "Its not a leap year"

# year=int(input("Enter the year:"))
# print(leap_year(year))
# Merging Two Dictionaries
# dict1 = {"name": "Alice", "age": 25}
# dict2 = {"city": "New York", "job": "Engineer"}

# result=dict1|dict2
# print(result)
# list_a = [1, 2, 3, 4, 5]
# list_b = [4, 5, 6, 7, 8]
# set_a=set(list_a)
# set_b=set(list_b)
# common_elements=set_a & set_b
# print(common_elements)

# def splitter(n1):
#       odd_list=[]
#       even_list=[]
#       for n in n1:
#             if n%2!=0:
#                   odd_list.append(n)
#       for n in n1:
#             if n%2==0:
#                   even_list.append(n)
#       return odd_list,even_list
      

# n1=list(map(int,input("Enter the numbers in comma:").split(',')))
# print(splitter(n1))
# Word Length Analysis
# def word_length(n1):
#       for w in n1:
#             length=len(w)
#             print(f"{w}-{length}")
# n1=input("Enter the fruit names:").split(",")
# print(n1)
# word_length(n1)

# text = "apple banana apple cherry banana apple"
# list_text=text.split(" ")
# print(list_text)
# count ={}
# count_s=0
# for w in list_text:
#       if w in count:
#             count[w]=count[w]+1
#       else:
#             count[w]=1
# print(count)
#  Print Alternate Prime Numbers
#  Write a program to find all prime numbers up to 20, but only print every second (alternate) prime number found.
# n=int(input("Enter the number:"))
# result=[]
# if n<=1:
#       print("Its not a prime number:")
# else:
#       for num in range(2,n):
#             for i in range(2,int(num**.5)+1):
#                   if num%i==0:
#                         break
#             else:
#                   result.append(num)
                  
# print(result)
# result_odd=result[::2]
# print(result_odd)
# Dictionary of Squares (Mapping Logic)
# dict={}
# for i in range(1,11):
#       dict[i]=i*i

# print(dict)
# input="I love coding in Python"
# result=input.replace(" ","_")
# print(result)
# Print Reverse Number Pattern
#  Print a downward number pattern where each row starts with a decreasing value.
# for i in range(5,0,-1):
#       for j in range(i,0,-1):
#             print(j,end=" ")
#       print("")

# user_input = "Python3"
# count_digit=0
# for char in user_input:
#       if char.isdigit():
#             count_digit=True
#             break

# print(f"{char}-{count_digit}")
# Capitalize First Letter (Title Case)
# text = "hello world from python"
# cap=[]
# result_text=text.split()
# for re in result_text:
#       cap.append(re.capitalize())

# result=" ".join(cap)
# print(result)
# import time
# count=5

# while count>0:
#       time.sleep(1)
#       print(count)
#       count=count-1
      
# print("blast off")
# with open("notes.txt","w") as file:
#       file.write("Hello this is sumi")
#       file.write("how are you sumi")
#       file.write("\n")

# with open("notes.txt","r") as file:
#       content=file.read()
#       print(content)
# try:
#       with open("sample.txt","r") as file:
#             content=file.read()
#             words=content.split()
#             result=len(words)
#             print(f"The title contains {result}")

# except FileNotFoundError:
#       print("File not found")

# def mul(a,b):
#       return a*b
      
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# print(mul(a,b))
# print('Name','Is','James',sep='****')
# num=255
# print('%o'%num)
# print(f"{num:b}")
# print(f"{num:x}")

# n=input("Enter the name:").split(" ")
# print(n)
# count=1
# for i in n:
#       print(f"Name{count}:{i}")
#       count=count+1
# number=458.541315
# print(f"{'%.3f'%number}")
# Numerator=22
# Denominator=29
# percentage=(Numerator/Denominator)*100
# print(f"The result is {percentage:.2f}%")
# word='Python'
# Number=3.12
# print(f"{word:>20} {Number}")
# title="REPORT SUMMARY"
# formatted_title=f"{title:-^40}"
# print(formatted_title)
# val=input("Enter your number:")
# print(val.zfill(6))


# quantity=3
# totalMoney=450
# price=150
# statement="I have {1}dollars so I can buy{0} football for{2:.2f} dollars"
# print(statement.format(totalMoney,quantity,price))
# Print numbers 1 to 10
# for i in range(1,11):
#       print(i,end=" ")
i =1
# while i<=10:
#       print(i,end=" ")
#       i=i+1

# Print even numbers from 1 to 20
# for i in range(1,21):
#       if i%2==0:
#             print(i,end=" ")
# for i in range(2,21,2):
#       print(i,end=" ")
# Sum of numbers from 1 to n
# def sum_num(n):
#       total=0
#       for i in range(n+1):
#             total=total+i
#       return total
# n=int(input("ENter the number:"))
# print(sum_num(n))
# def sum_number(n):
#       total=0
#       for i in range(1,n+1):
#             total+=i
#       return total
# n=int(input("Enter te number:"))
# print(sum_number(n))
# Multiplication table
# def mul(n):
#       for i in range(1,11):
#                  print(f"{n} x {i}={n*i}")
            
      
# n=int(input("Enter the number:"))
# mul(n)
# def mul(n):
#       for i in range(1,n+1):
#             for j in range(1,11):
#                   print(f"{i}x{j}={i*j}")
#             print()
# n=int(input("Enter the number:"))
# mul(n)
# Reverse a number
# input=1234
# reverse=0
# while input>0:
#       digit=input%10
#       reverse=reverse*10+digit
#       input=input//10

# print(reverse)
# Check palindrome number
# def palindrom(number):
#       original=number
#       reverse=0
#       while number>0:
#             digit=number%10
#             reverse=reverse*10+digit
#             number=number//10
#       return reverse==original
      
# number=int(input("Enter the number:"))
# print(palindrom(number))
# def fact(number):
#       fact=1
#       for i in range(1,number+1):
#             fact=fact*i
#       print(fact)

# number=int(input("Enter the number:"))
# fact(number)
# Display numbers from -10 to -1 using for loop
# for i in range(-10,0,1):
#       print(i,end=" ")
#       # print()
# Display a message “Done” after successful execution of for loop
# for i in range(5):
#       print(i)
# else:
#       print("Done")
# Write a program that accepts a number from the user and calculates the sum of all numbers from 1 up to that number.
# user_input=int(input("Enter the number:"))
# total=0
# for i in range(user_input+1):
#       total+=i
# print(total)
# Print multiplication table of a given number
# user_input=int(input("Enter the number:"))

# for i in range(1,11):
#       print(i*user_input)
# Calculate the cube of all numbers from 1 to a given number
# user_input=int(input("Enter the number:"))
# for i in range(user_input+1):
#       print(f"Current Number is :{i} and the cube is {i**3}")
# numbers = [12, 75, 150, 180, 145, 525, 50]
# new_list=[]
# for i in numbers:
#       if i>500:
#             break
#       elif i>150:
#             continue
#       if i%5==0:
#             new_list.append(i)
# print(new_list)
list1 = [10, 20, 10, 30, 10, 40, 50]
unique_list={}

# for i in list1:
#       if i in unique_list:
#             unique_list[i]=unique_list[i]+1
#       else:
#             unique_list[i]=1
# for key,val in unique_list.items():
#       if val>1:
#             print(f"{key}:{val}")
# Print elements from a list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# evn_position=[]
# for index,value in enumerate(my_list):
#       # print(f"{index}:{value}")
#       if index%2!=0:
#             print(value)
# for i in range(1,len(my_list),2):
#       print(my_list[i])
# list1 = [10, 20, 30, 40, 50]
# reverse_list=[]
# # for i in range(len(list1)-1,-1,-1):
# #       reverse_list.append(list1[i])
# # print(reverse_list)
# reverse_list=list1[::-1]
# print(reverse_list)
# for i in reversed(list1):
#       print(i)
# size=len(list1)-1
# result=[]
# for i in range(size,-1,-1):
#       result.append(list1[i])
# print(list1)
input="Python"
# revers=input[::-1]
# print(revers)
# reversed=" "
# for char in input:
#       reversed=char+reversed
      
# print(reversed)
# Count vowels and consonants in a sentence
# sentence="Loops are Fun!"
# vowels="aeiou"
# v_w=0
# v_c=0
# for char in sentence.lower():
#       if char.isalpha():
#             if char in vowels:
#                   v_w+=1
#             else:
#                   v_c+=1

# print(f"The number of vowels is:{v_w} and characters:{v_c}")
# Given_input=75869
# # count=Given_input
# # print(count)
# count=0

# while Given_input>0:
#       Given_input=Given_input//10
#       count=count+1
# print(count)
# Reverse an integer number
# Given_input=76542
# reverse=0
# while Given_input>0:
#       digit=Given_input%10
#       reverse=reverse*10+digit
#       Given_input=Given_input//10
# print(reverse)
# Find largest and smallest digit in a number
# Given_input=75869
# small=9
# large=0
# while Given_input>0:
#       digit=Given_input%10
#       if digit>large:
#             large=digit
#       if digit<small:
#             small=digit
#       Given_input=Given_input//10

# print(f"{large},{small}")
# Check if a number is a palindrome
# number = 123
# original=number
# reversed=0
# while number>0:
#       digit=number%10
#       reversed=reversed*10+digit
#       number=number//10
# print(reversed)
# if original==reversed:
#       print(True)
# else:
#       print(False)
# Find factorial of a number

# number=5
# fact=1
# for num in range(1,number+1):
#       fact=fact*num
# print(fact)
# n=6
# while n!=1:
#       if n%2==0:
#          n=n//2
#       else:
#             n=(3*n)+1
#       print(f"{n}",end=" ")
# Print right-angled triangle Number Pattern using a Loop
n=int(input("enter the number:"))
for i in range(n+1):
      for j in range(i+1):
            print(f"{i}{i+1}",end=" ")
       

      
      
      
            
      



         
      


            
            
            
               
      
      

      
     
      

            

