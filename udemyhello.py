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
text =input("Enter a word: ").lower()
word_count ={}

    
for word in text:
    if word=="":
        continue
    if word in word_count:
        current_count = word_count[word]
    else:
        current_count =0
    word_count[word] = current_count+1
for word,count in word_count.items():
    if count>0:
        print("word : count",word,count)
    