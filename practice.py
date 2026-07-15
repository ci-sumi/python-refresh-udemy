# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#             print(j,end="")
#     print()
# Write a program to check if a number is an Armstrong number. 
# n=input("Enter Your number:")
# total=0
# p=len(n)
# arm=0
# for i in str(n):
#     total+=int(i)**p
# print(total)
# if total==int(n):
#     print("Its an Arm strong number:")
# else:
#     print("Its not a Arm strong number")
# n=int(input("Enter a number:"))
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("")
#  Print the decreasing pattern
# for i in range(6,1,-1):
#     for j in range(1,i):
#         print(j,end=" ")
#     print("")
# Write a program to print a pattern of alternate numbers from 1 to 20
# for i in range(1,21):
#     if i%2!=0:
#         print(i)
# rows=5
# ascii_value=65
# for i in range(rows):
#     letter=chr(ascii_value+i)
#     for j in range(i+1):
#         print(letter,end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# rows=5
# for i in range(0,rows):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()
# for i in range(5,1,-1):
#     for j in range(1,i):
#         print("*",end=" ")
#     print()
# Write a program to print the full multiplication table 
# from 1 to 10 in a grid format.
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end=" ")
#     print("")
# List Cumulative Sum: Each element is the sum of all previous
# input=[1,2,3,4]
# new_list=[]
# current_sum=0
# for i in input:
#     current_sum+=i
#     new_list.append(current_sum)
# print(new_list)
# scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60}
# passing_students={}
# for key,values in scores.items():
#     if values>75:
#         passing_students[key]=values

# print(passing_students)
#common _elements
# list_a=[1,2,3,4,5]
# list_b=[1,2,3]
# common_list=[]
# for item in list_a:
#     if item in list_b:
#         common_list.append(item)
# print(common_list)
# Remove duplicates from list
# Given_input =[1, 2, 2, 3, 4, 4, 4, 5]
# new_list=[]
# for i in Given_input:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)
# Given_input=[1,2,3,4,5,6]
# odd_=[]
# even=[]
# for item in Given_input:
#     if item%2==0:
#         even.append(item)
#     else:
#         odd_.append(item) 

# print(odd_)
# print(even)
# result_list=even+odd_
# print(result_list)
# Given_nums=[1,2,3,4,5]
# k=2
# for _ in range(k):
#     first_element=Given_nums.pop(0)

#     Given_nums.append(first_element)
# print(Given_nums)
# Word frequency counter
text = "apple banana apple orange banana apple"
# words=text.split()
# new_list=[]
# # count=1
# for word in words:
#     if word not in new_list:
#         new_list.append(word)
#         count=words.count(word)

#         print(f"{word}:{count}")
# words=text.split()
# new_dict={}
# for word in words:
#     if word in new_dict:
#         new_dict[word]+=1
#     else:
#         new_dict[word]=1
# print(new_dict)
    
# Display fibonacci series
# num1=0
# num2=1
# for i in range(10):
#     result=num1+num2
#     print(num1)
#     num1=num2
#     num2=result
# number=28
# divisor_sum=0
# for i in range(1,(number//2)+1):
#     if number%i==0:
#         divisor_sum+=i

# if number==divisor_sum:
#     print("its a perfect number")
# else:
#     print("its not a perfect number")
# Print numbers from 1 to 5
# for i in range(1,6):
#     print(f"# {i}")
# Print even numbers
# Print all even numbers from 1 to 10.
# for i in range(1,11):
#     if i%2==0:
#         print(i)
# Count vowels in a word
# word="apple"
# wowels="aeiou"
# count=0
# found=[]
# for w in word:
#     if w in wowels:
#         found.append(w)
#         count=count+1
# result=",".join(found)
# print(f"{result} are vowels and count is {count}")
# Sum of numbers
# sum=0
# for i in range(1,6):
#     sum+=i
# print(sum)
# Print a pattern
# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()
# Reverse a string using loop
# text="hello"
# size=len(text)-1
# for i in range(size,-1,-1):
#     print(text[i])
# Count words in a sentence
text = "apple banana apple"
words=text.split()
# new_dict={}
# for word in words:
#     if word in new_dict:
#         new_dict[word]=new_dict[word]+1
#     else:        new_dict[word]=1
# print(new_dict)
# new_word=[]
# count=0
# print(words)
# for word in words:
#     if word in new_word:
#         count=count+1
#     else:
#         count=1
#         new_word.append(word)
#     print(f"{word}:{count}")
# binary_string="1101"
# decimal_value=0
# reversed=binary_string[::-1]
# for i in range(0,len(binary_string)):
#     if reversed[i]=="1":
#         decimal_value=decimal_value+2**i
#     # print(binary_string[i])
#     print(reversed[i])
# print(decimal_value)
# num=7
# is_prime=True
# for i in range(2,num):
#     if num==0:
#         is_prime=False
#         break
# if is_prime:
#     print("its a prime number")
# else:
#     print("its a not a prime number")
# start=25
# end=50
# for num in range(start,end+1):
#     if num>0:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)
# start=2
# sub_total=0
# n=5
# for i in range(0,n):
#     sub_total=sub_total+start
#     start=start*10+2

# print(sub_total)
# nested_list = [[10, 20], [30, 40], [50, 60]]
# flat=[]
# for item in nested_list:
#     for i in item:
#         flat.append(i)
# print(flat)
# matrix = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]
# target=60
# for r_index,row in enumerate(matrix):
#     for c_index,value in enumerate(row):
#         if value==target:
#             print(f"Target {target} found at row:{r_index},column:{c_index}")
#             break
# print("hello world",'isit good to be out there',sep='***')

        
# for i in range(1,6):
#     print(i,end=" ")
# for i in range(1,6):
#     square=i**2
#     print(f"{square}",end=" ")
# word ="python"
# result=""
# for i in range(len(word)-1,-1,-1):
#     print(word[i],end="")
# decimal=8
# # octal=oct(decimal)
# print(f'{decimal:b}' )
# Giveninput='Emma Jessa Kelly'
# name_list=Giveninput.split()
# for name in name_list:
#     print(name)
# str1,str2,str3=input("Enter the names:").split()
# print(f'n(ame1:{str1}')
# print(f'name2:{str2}')
# print(f'name3:{str3}')
# Decimal_number=255
# print(f'hexa_decimal:{Decimal_number:x}')
# number=458.541315
# print(f"The actual number is:{number:.3f}")
# word=input("Enter the word:")
# version=input("Enter the version:")
# print(f"{word:>20} {version}")
# title = "REPORT SUMMARY"
# print(f"{title:-^50}")
# word="education"
# vowels="aeiou"
# count=0
# for w in word:
#     if w in vowels:
#         count+=1
# print(f"Total number of vowels:{count}")
num1=1
num0=0
# print(num0, num1, end=" ")
# for _ in range(10):
#     result=num0+num1
#     print(result,end=" ")
#     num0,num1=num1,result
# fact=1
# number=8
# for i in range(number,1,-1):
#     fact=fact*i
# print(fact)
    
# num=22
# deno=29
# result=(num/deno)*100
# print(f'{result:.2f}%')
# Given_input='78.6,78.6,85.3,1.2,3.5'
# result=Given_input.split(",")
# print(result)
    
# Given_input=input("eenter the vales with comma:")
# numbers=[float(x)for x in Given_input.split(",")]
# print(numbers)
# numbers=[]
# for i in range(0,5):
#     item=float(input("Enter the numbers:"))
#     numbers.append(item)
# print(numbers)
# names=['Alice','Bob','Charlie']
# scores=[85,92,78]
# print(f"{'Name':<12} {'Score'}")
# print("-"*20)

# for name,score in zip(names,scores):
#     print(f"{name:<15}{score}")
#Prime number or  not
# number=7
# for num in (2,number+1):
#     if number%num==0:
#         print("Its not a prime number")
#         break
# else:
#     print("Its a prime number")
# num=25
# is_prime=True
# for i in range(2,int(num**.5)+1):
#     if num%i==0:
#         is_prime=False
#         break
# if is_prime==True and num>1:
#         print(f"{num} is a prime number")
# else:
#         print(f"{num} is  not a prime number")

# word="programming"
# wor_dic={}
# for w in word:
#     if w in wor_dic:
#         wor_dic[w]=wor_dic[w]+1
#     else:
#         wor_dic[w]=1
# for key,values in wor_dic.items():
#     print(f"{key}:{values}")

# while True:
#     print("1.Say Hello\n2.Calculate the square\n3.Exit")
#     accept=int(input("Enter choice(1-3):"))
#     if accept==1:
#         print("Hello Good morning:")
#     elif accept==2:
#         n=int(input("Enter the value you want to square:"))
#         if n>0:
#             square=n**2
#             print(f"Square of {n}is {square}")
#         else:
#             print("Enter a valid number")
#     elif accept==3:
#         print("Exit")
#         break
#     else:
#         print("Invalid Choice")
    
# import getpass
# user=input("Enter the user_name:")
# # password=input("Enter the password:")
# password=getpass.getpass("password: ")
# if user=="sumi" and password=="hello":
#     print("Login successful")
# else:
#     print("Login unsuccessful")
# num=10
# while(num<=15):
#     print(num)
#     num=num+1
# with open("geek.txt","w") as file:
#     file.write("Hello, this is a sample text file.")
# with open("geek.txt","r") as file:
#     content=file.read()
#     print(content)
# fruit_list=['Apple','Orange','Mango']
# with open("geek.txt","a") as file:
#     for fruit in fruit_list:
#         file.write(fruit+"\n")
# import os
# filename="geek.txt"
# if os.path.exists(filename):
#     file_info=os.stat(filename)
#     if file_info.st_size==0:
#         print(f"Status:{filename}is empty.")
#     else:
#         print(f"{filename} size is {file_info.st_size} bytes")
# number=1
# while(number<=5):
#     result=number**3
#     print(result,end=" ")
#     number+=1
#Prirnt odd numbers between(1-10)
# number=1
# while(number<=10):
#     if number%2!=0:
#         print(number,end=" ")
#     number+=1
# number=1
# product=1
# while(number<=5):
#     product=product*number
#     number+=1
# print(product)
# words="hello world"
# word=words.split()
# print(word)
# for w in word:
#     print(w[::-1],end=" ")
# word="Hello World"
# size_word=len(word)-1
# for i in range(size_word,-1,-1):
#     while(size_word>0):
#         size_word-=1
#     print(word[i],end="")
# words="Hello World"
# word=words.split()
# for w in word:
#     i= len(w)-1
#     while(i>=0):        
#         print(w[i],end=" ")
#         i-=1
# word="learning"
# vowels="aeiou"
# size_word=len(word)
# constants=0
# lis_word=[]
# for w in word:
#     if w not in vowels:
#         lis_word.append(w)
#         constants+=1
# print(f'{lis_word},{constants}')
# word=input("Eneter the word:")
# vowels="aeiou"
# index=0
# count=0
# while index<len(word):
#     if word[index] not in vowels and word[index].isalpha():
#         count=count+1
#     index+=1
# print(count)
# number=1
# while(number<=5):
#     print(number*3,end=" ")
#     number+=1
# b=int(input("Enter the number:"))
# e=int(input("Enter the number:"))
# result=1
# count=1
# while count<=e:
#     result=result*b
#     count+=1
# print(result)
# def demo(name,age):
#     print(name,age,end="")
    
# demo(name="kelly",age=25)
# def fun1(*args):
#     print('printing values:')
#     for a in args:
#         print(a)
# call1 =fun1(20,40,60)
# call2 =fun1(80,100)
# number=int(input("Enter a number:"))
# is_perfect_square=False
# i=1
# while(i*i<=number):
#     if i *i ==number:
#         is_perfect_square=True
#         break
#     i=i+1
# if is_perfect_square:
#     print("Its a perfect square")
# else:
#     print("its not a perfect number:")    
# def calculation(a,b):
#     return a+b,a-b

# result,result1=calculation(40,10)
# print(f'{result},{result1}')

"Occurances of word in a string"

# for w in wd:
#     if w in empty_list:
#         empty_list[w]=empty_list[w]+1
#     else:
#         empty_list[w]=1
# print(empty_list)
# word ="sumi is sucess sucess"
# wd=word.split()
# empty_list=[]
# count=0

# for w in wd:
#     if w in empty_list:
#         count+=1
#     else:
#         empty_list.append(w)
#         count=1
#     print(f"{w}{count}")
# word="success"
# s=len(word)
# ch=input("Enter the character you want to count:")
# index=0
# count=0

# while(index<s):
#     if word[index]==ch:
#         count+=1
#     index+=1
# print(f"{ch}:{count}")

# def show_employee(name,salary=9000):
#     print(f"Name:{name} salary:{salary}")
    

# show_employee("Ben",12000)
# show_employee("Jessa")
#Encapsulation
#Hiding the internal representation of data inside a class
#Binding data_members and method into a single class
# class Employee:
#     def __init__(self,name,age):
#         self.name=name #Public attribute
#         self.__age=age #Private attribute

# emp=Employee("sumi",38)
# print(emp.__age)
# class Employee:
#     def __init__(self,name):#Public attrubute
#         self.name=name
#     def dispaly_name(self):#Public method
#         print(self.name)
# emp=Employee("sumi")
# emp.dispaly_name()
# print(emp.name)
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary
#     def show_salary(self):
#         print("Salary:",self.__salary)
# emp=Employee("john",200)
# # print(emp.__salary)
# emp.show_salary()
# def outer_funtion(a,b):
#     def add(a,b):
#         return a+b
    
    
#     result=add(a,b)
#     return result+5

# result_outer=outer_funtion(7,8)
# print(result_outer)
##Recurcisve function
# def addition(num):
#     if num:
#         return num+addition(num-1)
#     else:
#         return 0
# result=addition(10)
# print(result)
# def display_student(name,age):
#     print(name,age)

# show_student=display_student
# show_student("Emma",26)
# Crete a list of even numbers from 4 to 30 using range function
# def even_numbers():
#     return list(range(4,30,2))
# print(even_numbers())
# class BankAccount:
#     def __init__(self):
#         self.balance=1000
#     def _show_balance(self):#Protected method
#         print(f"Balance:{self.balance}")
#     def __update_balane(self,amout):#private method
#         self.balance+=amout
#     def depposit(self,amount):
#         if amount>0:
#             self.__update_balane(amount)
#             self._show_balance()
#         else:
#             print("Invalid Deposit")
# x = [4, 6, 8, 24, 12, 2]
# min=24
# max=2
# for i in x:
#     if i>max:
#         max=i
# print(max)
# def largest_number(number):
#     largest=number[0]
#     for i in number:
#         if i>largest:
#             largest=i
#     return largest

# number=[4, 6, 8, 24, 12, 2]
# print(largest_number(number))
# def describe_pet(animal_type,pet_name):
#     print(f"i have a {animal_type}.")
#     print(f"my {animal_type}'s name is {pet_name}.")

# # describe_pet("hamster","Harry")

# describe_pet(animal_type="dog",pet_name="Willie")
# Create a Function with Keyword Arguments
# def print_info(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k}:{v}")
        
# print_info(name="Alice", age=30, city="New York")
# class BankAccount:
#     def __init__(self,owner,balane):
#         self.owner=owner
#         self.__balance=balane
#     #Getter method to safely read the private data
#     def get_balance(self):
#         return self.__balance
#     #Setter method to safely modify the private data with validation
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             print(self.__balance)
#         else:
#             print("You cant deposit a negative number")
#     def withdraw(self,amount):
#         if 0<amount<self.__balance:
#             print(self.__balance)
#         else:
#             print("Invalid amount")
# account=BankAccount("Allice",1000)
# print(account.owner)
# account.deposit(500)
# print(account.get_balance())
# Mimicking method overloading with python unlike any other languages like 
# class Multiply:
#     def mul(self,a=1,b=2,*args):
#         result = a*b
#         for r in args:
#             result=result*r
#         return result


# mul1=Multiply()

# print(mul1.mul())
# print(mul1.mul(3))
# print(mul1.mul(3,4,5))
# class Animal:
#     def sound(self):
#         return "It makes some generic sounds"
# class Dog(Animal):
#     def Sound():
#         return "Bark Bark "
# class Cat(Animal):
#     def Sound():
#         return "Meow Meow"

# animals=[Dog(),Cat()]
# for animal in animals:
#     print(animal.sound())

# addition = lambda a,b: a+b
# print(addition(3,4))
# a="GeeksforGeeks"
# upper=lambda x:x.upper()
# print(upper(a))fo
# class Animal:
#    def __init__(self,name):
#       self.name=name
#    def info(self):
#       print(self.name)
      
# class Dog(Animal):
#    def sound(self):
#       print("It barks")

# d=Dog("Buddy")
# d.info()
# d.sound()
# class Animal:
#    def __init__(self,name):
#       self.name=name
#    def info(self):
#       print("Animal name:",self.name)
# class Dog(Animal):
#    def __init__(self,name,breed):
#       super().__init__(name)
#       self.breed=breed
#    def details(self):
#       print(self.name,"is a",self.breed)

# d=Dog("Buddy","Golden")
# d.info()
# d.details()
# Method overriding inheritance
# class Animal:
#    def sound(self):
#       print("Animal sound")
# class Dog(Animal):
#    def sound(self):
#       print("it barks")
      
# d=Dog()
# d.sound()
#Single Inheritance
# class Parent:
#    def fun1(self):
#       print("This function is in parent class")
# class Child(Parent):
#    def fun2(self):
#       print("This function is second function")

# obj=Child()
# obj.fun1()
# obj.fun2()
# class Mother:
#    mothernmae=""
#    def mother(self):
#       print(self.mothernmae)
# class Father:
#    fathername=""
#    def father(self):
#       print(self.fathername)
# class Child(Mother,Father):
#    def parents(self):
#       print("Mother's name:",self.mothernmae)
#       print("Father's name:",self.fathername)
# c=Child()
# c.mothernmae="Alice"
# c.fathername="Bob"
# c.parents()
# class Grandfather:
#    def __init__(self,grandfather_name):
#       self.grandfather_name=grandfather_name
# class Father(Grandfather):
#    def __init__(self,fathersname,grandfather_name):
#       super().__init__(grandfather_name)
#       self.fathersname=fathersname
# class Son(Father):
#    def __init__(self,son_name,fathersname,grandfather_name):
#       super().__init__(fathersname,grandfather_name)
#       self.son_name=son_name
#    def print_name(self):
#       print("Grandfathername",self.grandfather_name)
#       print("Fathername",self.fathersname)
#       print("Son name",self.son_name)

# s1=Son('Prince','Ram','Druva')
# print(s1.son_name)
# s1.print_name()
# for i in range(4,0,-1):
#    print(i)

# input=int(input("Enter the number:"))
# if input<0:
#    for i in range(input,1):
#       print(i)
#       i=i+1
# input=int(input("Enter the number:"))
# if input>0:
#    for i in range(input,-1,-1):
#       print(i)
# num=int(input("Enter the number:"))
# if num<0:
#    for i in range(num,1,1):
#       print(i,end=" ")
# def utility(s):
#    for i, ch in enumerate(s):
#       if i%2==0:
#          print(ch,end=" ")

# utility("Geeks")
# def utility(s):
#    result=[]
#    for i ,ch in enumerate(s):
#       if i %2==0:
#          result.append(ch)
#    return "".join(result)
# print(utility("Geeks"))
# def reverse_string(input):
#    result=input[::-1]
#    print(result)
# reverse_string("Geeks")
# def reverse_string(s):
#    result=""
#    for ch in s:
#       result=ch+result
#    return result
# print(reverse_string("Geeks"))
# def reverse_string(s):
#    return "".join(reversed(s))

# print(reverse_string("Geeks"))
# def reverse_string(s):
#    stack=[]
#    for ch in s:
#       stack.append(ch)
#    result=""
#    while stack:
#       result=result+stack.pop()
#    return result
# print(reverse_string("Geeks"))
# def welcomeAboard(name):
#     print(f"Welcome aboard, {name}!")

# welcomeAboard("sumi")
# Regxis is a way to search,match,validate or extract patterns from the text
# import re
# txt='Geeks forGeeks: A computer science portal for geeks'
# match=re.search(r'portal',txt)
# if match:
#     print(match.group())
#     print("Start:",match.start(),"End",match.end())
# else:
#     print("No match")
# import re


# def numberMatcher(str):
#     pat=r'\d+'
#     match=re.findall(pat,str) ##find all finds all the matched texts and returns a list
#     if(match): 
#         for i in match:
#             print(i, end=" ")
#     else:
#         print(-1,end="")
# str = "asdasd123asmdasdk34234kfdsd34sdfk5"
# numberMatcher(str)
# def boolean(a):
#     return 1 if a=="true" else 0

# print(boolean(a="false"))
# def reverse_string(str):
#     result=""
#     for char in str:
#         result=char+result
#     print(result)
# reverse_string("sumi")
# def reverse_string(str):
#     stack=[]
#     for char in str:
#         stack.append(char)
        
#     result=""
#     while stack:
#         result=result+stack.pop()   
#     return result
# print(reverse_string("sumi"))
#Lambda function
# a="GeeksforGeeks"
# upper=lambda x:x.upper()
# print(upper(a))
# add = lambda a,b:a+b
# print(add(3,4))
# data={"name":"Jake","age":22}
# print(data)
# Create a dictionary
# a={"x":1,"y":2}
# print(a)
# b=dict(name="sumi",age=38)
# print(b["name"])
# print(b.get("age"))
# d={"name":"sam"}
# d["age"]=21
# d["name"]="Alex"
# print(d)
# d={"a":1,"b":2}
# del d['a']
# print(d)
# d.pop("b")
# print(d)
# print(d.popitem())
# d={"a":1,"b":2}
# for key in d:
#     print(key)
# for value in d.values():
#     print(value)
# for key,value in d.items():
#     print(key,value)
# print(d["c"])
# d={"watermelon":4,"banana":2,"apple":3}
# asc={k:v for k,v in sorted(d.items(),key=lambda item:item[1])} 
# print(asc)
# from collections import OrderedDict
# d={'monday':10,'tuesday':9,'wednesday':15}
# res=OrderedDict(sorted(d.items(),key=lambda item:item[1]))
# print(res)
# d={2:56,1:2,3:323}
# for k,v in sorted(d.items(),key=lambda item:item[1]):
#     print((k,v),end="")
# import numpy as np
# d={'alex':10,'ben':9,'clara':15,'diana':2,'eva':32}
# k=list(d.keys())
# v=list(d.values())
# idx=np.argsort(v)
# res={k[i]:v[i] for i in idx}
# print(res)
# Using Defaultdict
# from collections import defaultdict
# dic=defaultdict(lambda:'Key not found')
# dic['a']=1
# dic['b']=2
# print(dic['a'])
# print(dic)
# print(dic['c'])
# dict={'India':'0901','Australia':'0025','Nepal':'0091'}
# print(dict.get('India','Not Found'))
# print(dict.get('Japan','Not Found'))
# dict.setdefault('Japan',"Not found")
# print(dict['India'])
# print(dict['Japan'])
# try:
#     print(dict['India'])
#     print(dict['USA'])
# except KeyError:
#     print("Not Found")
# dict={'a':5,'c':8,'e':2}
# if 'q' in dict:
#     print(dict['q'])
# else:
#     print("Key not found")
# points={}
# points[(1,2)]="A"
# points[(3,4)]="B"
# print(points[(1,2)])
# print(points[(3,4)])
# dict = {}
# dict[(1,2,3,4)]="First"
# dict[(4,5,6)]="Second"
# print(dict)
# print(dict[(1,2,3,4)])
# places={("19.07'53.2","72.54'51.0"):"Mumbai",
#         ("28.33'34.1","77.06'16.6"):"Delhi"}
# print(places)
# print('\n')
# lat,long,plc=[],[],[]
# for i in places:
#     lat.append(i[0])
#     long.append(i[1])
#     plc.append(places[i])

# print(lat)
# print(long)
# print(plc)
# data={(1,"John","Doe"):{"a":"geeks","b":"software","c":7500},
#       (2,"Jane","Smith"):{"e":30,"f":"for","g":9000}}

# print(data[(1,"John","Doe")]["a"])
# data[(1,"John","Doe")]["a"]={"b":"marketting","c":75000}
# print(data[(1,"John","Doe")]["a"])
# Python program to find the sum of all items in a dictionary
# input={'a':100,'b':200,'c':300}
# result=sum(input.values())
# print(result)
# result=sum(input[key] for key in input)
# print(result)
# res=0
# for value in input.values():
#    res+=value
# print(res)
# res=sum(map(lambda key:input[key],input))
# print(res)
# Given a sentence,Create a dictionary that stores how many times each word appears
# text = "apple banana apple orange banana apple"
# my_dictionary={}
# text_result=text.split()
# print(text_result)
# for word in text.split():
#     my_dictionary[word]=my_dictionary.get(word,0)+1
# print(my_dictionary)
# for word in text.split():
#     if word in my_dictionary:
#         my_dictionary[word]+=1
#     else:
#         my_dictionary[word]=1
# print(my_dictionary)
# for word in text.split():
#     my_dictionary[word]=my_dictionary.get(word,0)+1
# print(my_dictionary)
# from collections import Counter
# my_dictionary = Counter(text.split())
# create_dictionary={key: value for key,value in my_dictionary.items()}
# print(create_dictionary)
# Create a dictionary where keys are number from 1 to 5 and values are their squares
# create_dictionary={x:x**2 for x in range(1,6)}
# print(create_dictionary)
# dictionary={}
# for x in range(1,6):
#     dictionary[x]=x**2
# print(dictionary)
# Swap Keys and Values in a Dictionary
# d = {
#     'a': 1,
#     'b': 1,
#     'c': 3
# }
# dictionary={}
# # for key,values in d.items():
# #     dictionary[values]=key
# # print(dictionary)
# dictionary={value:key for key,value in d.items()}
# print(dictionary)
# dictionary={}
# for key,values in d.items():
#     if values not in dictionary:
#         dictionary[values]=[]
        
#     dictionary[values].append(key)
#     print(dictionary)
# scores = {
#     'Alice': 82,
#     'Bob': 91,
#     'Charlie': 78
# }
# result=max(scores,key=scores.get)
# print(scores[result])
# 
# dict3={
#     "a":1,
#     "b":2,
#     "c":3    
# }
# dict4={
#     "x":1,
#     "y":3,
#     "z":6
# }
    
# dict3.update(dict4)
# print(dict3)
# dict=dict3 | dict4
# print(dict)
# Unpacking
# dict = {**dict3, **dict4}
# print(dict)
# words=['cat','dog','apple','banana','car']
# result={}
# for word in words:
#     length=len(word)
#     if length not in result:
#         result[length]=[]
    
#     result[length].append(word)
# print(result)
# Count charcters (ignore spaces)
# text = "hello  world"
# result={}
# for t in text:
#     if t!=" ":
#         if t in result:
#             result[t]+=1
#         else:
#             result[t]=1
# print(result)
# Find the duplicates
# nums=[1,2,3,2,2,4,4,5,1,6]
# result=[]
# frequency={}
# for n in nums:
#     if n not in result:
#         frequency[n]=1
#     else:
#         frequency[n]+=1

# print(frequency)
# result=[]
# dupliacte=[]
# for n in nums:
#     if n not in result:
#         result.append(n)
#     else:
#         dupliacte.append(n)
# print(dupliacte)
# duplicate_dictionary={}
# for n in dupliacte:
#     duplicate_dictionary[n]=duplicate_dictionary.get(n,0)+1
# print(duplicate_dictionary)
# nums = [1,2,3,2,4,5,1,6]
# frequncy={}
# for n in nums:
#     if n not in frequncy:
#         frequncy[n]=frequncy.get(n,0)+1
# print(frequncy)
# Student average marks
# students = {
#  'Alice':[80,85,90],
#  'Bob':[70,75,80],
#  'Charlie':[95,92,98]
# }
# result={}
# # for name,marks in students.items():
# #     result[name]=sum(marks)/len(marks)
# # print(result)
# for name,marks in students.items():
#     print(name,marks)
# nums = [2, 7, 11, 15]
# target=9

# for i in range(len(nums)):#(0,1,2,3)
#     for j in range(i+1,len(nums)):#(1,2,3)
#         if nums[i]+nums[j]!=target:#2
#             print(nums[i],nums[j])
    
# for i , val in enumerate(nums):
#     print(i,val)
# for i in range(len(nums)):
#     print(i,nums[i])
# a=["A","B","C"]
# r=list(enumerate(a))
# print(r)
# 
# a=["Geeks","for", "Geek"]
# # for index,value in enumerate(a,start=10):
# #     print(f"Index{index} value{value}")
# b=enumerate(a)
# print(next(b))
# print(next(b))
# print(next(b))

# nums = [2, 7, 11, 15]
# target=9
# seen={}
# for i ,n in enumerate(nums):
#     need=target-n  
#     if need in seen:
#         print([seen[need],i])
#     seen[n]=i
# data=[{'name':'Alice','city':'Dublin'},
#       {'name':'Bob','city':'London'},
#       {'name':'Charlie','city':'Dublin'},
#       {'name':'David','city':'London'},
#       {'name':'Eve','city':'Paris'}]
# result={}
# for item in data:
#     city=item['city']
#     name=item['name']
#     if city not in result:
#         result[city]=[]
#     result[city].append(name)
# print(result)
# nameDictionary={
#     'firstNmae':'sumi',
#     'secondName':'T.S'
# }
# print(nameDictionary)
# print(type(nameDictionary))
# countryFlags={
#     'China':'a',
#     'India':'b',
#     'Uganda':'c'
# }
# # return Indian flag from the dictionary
# # for key,values in countryFlags.items():
# #     if key=='India':
# #         print(values)
# baseBallteams={
#     'Colorodo':"Ford",
#     'Boston':"Red Sox",
#     'Minnesota':"Twins",
#     'Milwaukee':"Brewers",
#     'Seattle':'mariners'
# }
# # print(list(baseBallteams.values()))
# print(baseBallteams.pop('Minnesota'))
# print(baseBallteams)
# capitals={
#     "Farance":"Paris",
#     "Japan":"Tokyo",
#     "Canada":"Ottawa"
# }
# print(capitals.get("Japan"))
# menu={
#     "espresso":3.00,
#     "drip cofee":2.00,
#     "croissant":3.50,
#     "muffin":2.75
# }
# menu["latte"]=4.50
# print(menu)
# menu.pop('drip cofee')
# print(menu)
# scores={
#     "Alice":92,
#     "Bob":78,
#     "Carol":85,
#     "Dave":61,
#     "Eve":95
# }

# print(list(scores.keys()))
# for names in scores.keys():
#     print(list(names))
# print(scores.keys())
# for keys,values in scores.items():
#     if values>80:
#         print(f"{keys}:{values}")
# recipe={"flour":500,"sugar":200,"butter":250}
# pantry={"flour":1000,"sugar":100}
# shopping_list={}
# for ingredient,needed_amount in recipe.items():
#     have_amount=pantry.get(ingredient,0)

#     if have_amount<needed_amount:
#         shopping_list[ingredient]=needed_amount-have_amount
#     print(shopping_list)
# grades={
#     "Alex":[85,92,90],
#     "Joradan":[78,84,84],
#     "Taylor":[95,100,93]
# }
# ne_dict={}
# for names,marks in grades.items():
#     ne_dict[names]=sum(marks)/len(marks)
# print(ne_dict)
# //Set opertations
# Remove duplicates from a list
# numbers=[1,2,3,4,4,5]
# outpu_list=set(numbers)
# print(outpu_list)
# final_result=list(outpu_list)
# # print(final_result)
# # print(final_result)
# anothe_dictionary=list(dict.fromkeys(nums))
# print(anothe_dictionary)
##Count the unique elements
# names = ["Tom", "Anna", "Tom", "John", "Anna"]
# names_count=len(set(names))
# print(names_count)
# check if an element exits
# a =int(input("Enter a number:"))
# def check_number(numbers,a):
#     if a in numbers:
#         print("Its exists")
#     else:
#         print("Its doens not exists")
# numbers ={10, 20, 30, 40, 50}
# result=check_number(numbers,a)
##Find common elements
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c= a & b
# print(c)
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c=b-a
# print(c)
##Remove Duplicates
# nums = [1, 2, 2, 3, 4, 4, 5]
# unique_numbers=list(set(nums))
# unique_numbers=list(dict.fromkeys(nums))
# print(unique_numbers)
# names=["Tom","Anna","Tom","John","Anna"]
# outputresult=len(set(names))
# print(outputresult)
# Find the duplicates
nums = [1, 2, 2, 3, 4, 4, 5]
# result_set={}
# for n in nums:
#     if n in result_set:
#         result_set[n]+=1
#     else:
#         result_set[n]=1

# print(result_set)
# for key,values in result_set.items():
#     if values>=2:
#         print(set(key))
# seen=set()
# duplicate=set()
# for n in nums:
#     if n in seen:
#         duplicate.add(n)
#     else:
#         seen.add(n)
# print(seen)
# print(duplicate)
# Reverse a list(wihout reverse())
# nums=[1,2,3,4,5]
# size=len(nums)
# result=[]
# # print(size)
# # for n in nums(size):
# #     print(n)
# for n in range(size-1,-1,-1):
#     result.append(nums[n])
# print(result)
# nums = [10, 50, 20, 90, 30]
# max=nums[0]
# for n in nums:
#     print(n)
#     if max<n:
#         max=n
# print(f"Max_number is :{max}")
# for i in range(len(nums)):
#     print(nums[i])
#     if max<nums[i]:
#         max=nums[i]
# print(f"Max_number is :{max}")
# nums = [10, 50, 20, 90, 30]
# max=nums[0]
# second_max=float('-inf')
# for n in nums:
#     if n>max:
#         second_max=max
#         max=n
# print(second_max)
# def welcome():
#     print("Welcome to Python")

# welcome()
##Function with parameter
# def greet(name):
#     print(f"Hello, {name}!")

# greet("john")
# def add(a,b):
#     return a+b
# result=add(2,3)
# print(result)
# def square(num):
#     return num*num

# result=square(2)
# print(result)
# list1=[12,20,30,40,89,56,90,89,78,25]
# print(list1)
# nums = [10, 20, 30, 40, 50]
# print(nums[0])
# print(nums[2])
# print(nums[-1])
# nums = [10, 20, 30, 40, 50, 60, 70]
# print(nums[0:3])
# print(nums[-3:])
# print(nums[2:5])
# print(nums[0::2])
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(nums[0::2])
# print(nums[1::2])
# nums = [5, 10, 15, 20, 25]
# nums.append(30)
# print(nums)
# nums.insert(2,12)
# nums.remove(15)
# print(nums)
# nums = [3, 8, 1, 6, 2]
# size=len(nums)
# for i in range(size):
#     print(i)
#     for j in range(size-i-1):
#         print(j)
#         if nums[j]>nums[j+1]:
#             nums[j],nums[j+1]=nums[j+1],nums[j]
# print(nums)

#Find the maximum number in the list
# max_number=nums[0]
# for n in nums:
#     if n >max_number:
#         max_number=n
# print(max_number)
# min_number=nums[3]
# for n in nums:
#     if n<min_number:
#         min_number=n
# print(min_number)
# nums = [12, 45, 7, 89, 23, 56]
# largest_number=nums[0]
# second_number=nums[0]
# for n in nums:
#     if n>largest_number:
#         second_number=largest_number
#         largest_number=n
#     elif n>second_number and n!=largest_number:
#         second_number=n

# print(second_number)
# nums = [1, 2, 2, 3, 3, 4, 5, 5]
# unique=[]
# for n in nums:
#     if n not in unique:
#         unique.append(n)
# print(unique)
# nums = [1, 2, 2, 3, 3, 3, 4]
# Count Frequency of Elements
# unique={}
# for n in nums:
#     if n in unique:
#         unique[n]+=1
#     else:
#         unique[n]=1

# print(unique)
# nums = [1, 2, 2, 3, 3, 3, 4]
# frequency={}
# for n in nums:
#     frequency[n]=frequency.get(n,0)+1
# print(frequency)
# nums = [10, 20, 30, 40, 50]
# # result=map(lambda x:x+x,nums)
# # print(result)
# size=len(nums)
# total=0
# for n in nums:
#     total=total+n
#     avg=total/size
# print(avg)
# nums = [10, 20, 30, 40, 50]
# size=len(nums)
# reversed_list=[]
# for i in range(size-1,-1,-1):
#     reversed_list.append(nums[i])
# print(reversed_list)
# nums = [0, 1, 0, 3, 12]
# result=[]
# for n in nums:
#     if n!=0:
#         result.append(n)

# for n in nums:
#     if n==0:
#         result.append(n)
# print(result)
# nums = [0, 1, 0, 3, 12]
# result=[]
# zero_ocunt=0
# for n in nums:
#     if n!=0:
#         result.append(n)
#     else:
#         zero_ocunt+=1
# result.extend([0]*zero_ocunt)
# print(result)
# nums = [30,31,33,34,35]
# max=nums[4]
# # size=len(nums)+1
# for i in range(min(nums),max+1):
#     if i not in nums:
#         print(i)
#         break
# Find the First Duplicate Element
# nums = [4, 2, 7, 5, 2, 9, 7]
# result=[]
# du=[]
# for n in nums:
#     if n in result:
#         print(n)
#         break
#     else:
#         result.append(n)
# nums = [4, 2, 7, 2, 4, 9, 7, 8]

# for n in nums:
#     if nums.count(n)==1:
#         print(n)
#         break

# seen=[]
# notseen=[]
# for n in nums:
#     if nums.count(n)==1:
#         seen.append(n)
#     else:
#         notseen.append(n)
# print(seen)
    
    
# numbers= [4, 2, 7, 2, 4, 9, 7, 8]
# act_size=len(numbers)
# size=len(numbers)-1
# reverse_liist=[]
# for n in range(size,-1,-1):
#     reverse_liist.append(numbers[n])
# print(reverse_liist)
# for i in range(act_size):
#     for j in range(i,size):
#         if numbers[i]>numbers[j+1]:
#             numbers[i],numbers[j+1]=numbers[j+1],numbers[i]
# print(numbers)
# nums = [20, 10, 30, 40, 50]
# size=len(nums)-1
# is_sorted=True
# for i in range(size):
#     if nums[i]>nums[i+1]:
#         print(nums[i])
#         is_sorted=False
#         break
# if is_sorted:
#     print("its sorted") 
# else:
#     print("its not sorted")
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# result=[]
# for n in list1:
#     if n in list2:
#         result.append(n)
# print(result)
# Find the Union of Two Lists
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# result=[]
# for n in list1:
#     result.append(n)
# for n in list2:
#     if n not in result:
#         result.append(n)
# print(result)
# Remove Duplicates from a List
# nums = [4, 2, 7, 2, 4, 9, 7, 8]
# # Remove duplicates but keep the original order.
# result=[]
# for n in nums:
#     if n not in result:
#         result.append(n)
# print(result)
# Find the Second Largest Number in a List
# nums = [12, 45, 7, 89, 23, 56]
# large=nums[0]
# second_large=nums[0]
# for n in nums:
#     print(n)
#     if n>large:
#         second_large=large
#         large=n
#     elif n>second_large and n!=large:
#         second_large=n

# print(second_large)
# print(large)
# Access List in Python
#Indexing
#Slicing
#Loop
a = [10, 20, 30, 40, 50]
# print(a[3])
# print(a[-1])
# for item in a:
#     print(item,end=" ")
# print(a[1:4])
# print(a[::-1])
# b=[item for item in a if item>20]
# print(b)
# a[1]=25
# print(a)
# a[1:3]=[21,35]
# print(a)
# List comprehension
# a=[x*2 if x%2==0 else x for x in a]
# print(a)
# for i , x in enumerate(a):
#     if x%2==0:
#         a[i]+=5
# print(a)
# b=list(map(lambda x:x+1,a))
# print(b)
# List compression is creating a new list by applying expression to each item in a existing iterable list
# a=[10,21,30,40]
# b=[val*2 for val in a]
# print(b)
# a = [1, 2, 3, 4, 5]
# b=[val for val in a if val%2==0]
# print(b)
# nums = [1, 2, 3, 4, 5]
# square_numbers=[x**2 for x in nums]
# print(square_numbers)
# nums = list(range(1, 21))
# even_numbers=[n for n in nums if n%2==0]
# print(even_numbers)
# List Comprehension with Conditional Expression
# nums = list(range(1, 21))
# # Create a list containing only the even numbers.
# even_list=[item for item in nums if item%2==0]
# print(even_list)
# words = ["apple", "banana", "cherry"]
# upper_letters=[item.upper() for item in words]
# print(upper_letters)
# words = ["cat", "elephant", "dog", "giraffe"]
# # Create a new list using a list comprehension that contains the length of each word.
# length_word=[len(item)for item in words]
# print(length_word)
# words = ["python", "java", "c++", "ruby"]
# first_word=[item[0] for item in words]
# print(first_word)
# nums = range(1, 21)
# Create a list containing the squares of only the odd numbers.
# new_list=[item**2 for item in nums if item%2!=0]
# print(new_list)
# words = ["hi", "hello", "world", "AI", "python"]
# Create a list containing only words with more than 3 letters.
# three_letters=[item for item in words if len(item)>3]
# print(three_letters)
# 1. basic structure
# new_list=[expression for item in iterable]
# nums=[1,2,3,4]
# squares=[item**2 for item in nums]
# print(squares)
# Filtering with if
# nums = [1, 2, 3, 4]
# even_numbers=["Even" if n%2==0 else "Odd" for n in nums]
# print (even_numbers)
# l1=[x for x in range(11) if x%2==0]
# print(l1)
# l1=[x for x in range(11) if x%2!=0]
# print(l1)
# def smaller(l,x):
#     return [y for y in l if y<x]
    

# l=[1,2,3,4]
# x=2
# result=smaller(l,x)
# print(result)
# def evenodd(l):
#     even=[x for x in l if x%2==0]
#     odd=[x for x in l if x%2!=0]
#     return even,odd

# l=[1,2,3,4,4,5]
# even,odd=evenodd(l)
# print(even)
# print(odd)
# s="geekforgeeks"
# l1=[x for x in s if x in 'aeiou']
# print(l1)
# l2=["geeks","ide","courner","gfg"]
# upper_l2=[x.upper() for x in l2 if x.startswith("g")]
# print(upper_l2)
# l4=[x**2 for x in range(10)]
# print(l4)
# set comprehension
# l1=[10,20,3,4,10,20,7,3]
# s1={x for x in l1 if x%2==0}
# s2={x for x in l1 if x%2!=0}
# print(s1)
# print(s2)
# Dictionary comprehension
# l1=[1,3,4,2,5]
# d1={x:x**2 for x in l1}
# print(d1)
# d2={x:f"ID{x}" for x in range(5)}
# print(d2)
# l2=[101,102,103]
# l3=["gfg","ide","courier"]
# d3={l2[i]:l3[i] for i in range (len(l2))}
# print(d3)
# l1=[101,102,203]
# l2=["neena","Meena","geena"]
# d3=dict(zip(l1,l2))
# print(d3)
# d1={101:"gfg",103:"pharama",102:"ide"}
# d2={v:k for (k,v)in d1.items()}
# print(d2)
# Using a Loop with enumerate
# a=[10,5,20,25]
# #Add 5 to odd numbers
# for i ,x in enumerate(a):
#     if x%2!=0:
#         a[i]+=5
# print(a)
# def double(val):
#     return val*2

# val=[3,4,5]
# print(double(val))

# a=[1,2,3,45]
# b=list(map(lambda x:x**2,a))
# print(b)
# map() with multiple iterables
# a=[1,2,3]
# b=[4,5,6]
# res=list(map(lambda x,y:x+y,a,b))
# print(res)
# Using map() with Tuples
# nums=(1,2,3)
# res=tuple(map(lambda x:x+1,nums))
# print(res)
# fruits=['apple','banana','cherry']
# result=list(map(str.upper,fruits))
# print(result)
# Replace Values in a List in Python
# a = [10, 20, 30, 40, 50]
# a[2]=35
# print(a)
# a = [10, 20, 30, 40, 50]
# for i in range(len(a)):
#     if a[i]==30:
#         a[i]=25
# print(a)
#Using while loop
# a = [10, 20, 30, 40, 50]
# i =0
# while i<len(a):
#     if a[2]==30:
#         a[2]=25
#     i+=1
# print(a)
# a = ["10", "20", "30", "40", "50"]
# result=list(map(lambda x:x.replace("30","25"),a))
# print(result)
# a = ["10", "20", "30", "40", "50"]
# result=a[:2]+["78"]+a[3:]
# # print(a[:2])
# # print(a[3:])
# # print(a)
# print(result)
# Python append list
# a=[2,5,6,7]
# a.append(30)
# print(a)
# a=[1,"python"]
# a.append(3.14)
# a.append("True")
# print(a)
# a=[1,2,3,4]
# a.append([4,5])
# print(a)
# a=[]
# for i in range(5):
#     a.append(i)
# print(a)
##insert() method
# a=["banana","cherry","grape"]
# a.insert(1,"mango")
# print(a)
# a=[1,2,3,45]
# a.insert(2,[2,34])
# print(a)
# a=[10,20,40,50]
# i=a.index(40)
# a.insert(i,89)
# print(a)
#Using extend method
# a=[1,2,3,4]
# n=[4,5,6]
# a.extend(n)
# print(a)
# a=[5,12,3,4]
# b=[4,5,6]
# a+=b
# print(a)
# a=[1,2,3]
# b=[4,5,6]
# a[len(a):]=b
# print(a)
# a=[1,2,3,4]
# a[2:4]=[4,5]
# print(a)
# from itertools import chain 
# a=[1,2,3,4]
# n=[4,5,6]
# a.extend(chain(n))
# print(a)
# Remove items from the list
#Remove,pop,del and clear
# a=[10,20,30,40,50]
# a.remove(30)
# print(a)
# a = [10, 20, 30, 40, 50]
# val=a.pop()
# print(a)
# print(val)
# print(a)
# del a[2:3]
# print(a)
# a.clear()
# print(a)
# Different ways to Clear a List in Python
#Clear method
input=[10,20,30,40,50]
# a.clear()
# print(a)
# del input[:]
# print(input)
#with pop
# a=[1,2,34,6]
# while a:
#     a.pop()
# print(a)
# //Reassigning to []
# a=[1,2,3,4,5]
# a=[]
# print(a)
# List Traversal
# def listtraversal(arr):
#     for i in arr:
#         print(i,end=" ")
#     return arr

# arr=[54,43,2,1,5]
# listtraversal(arr)

# def lengthoflist(arr):
#     return len(arr)


# arr=[1,2,34,9]
# print(lengthoflist(arr))
# Sum The List
# def sum_of_list(arr):
#     total=0
#     for i in arr:
#         print(i)
#         total=i+total
        
#     return total

# arr=[54, 43, 2, 1, 5]
# result=sum_of_list(arr)
# print(result)
# Decrement List Values
# def decrement(arr):
#     result_list=[]
#     for i in arr:
#         i =i-1
#         result_list.append(i)
#     return result_list

# arr = [54, 43, 2, 1, 5]
# result=decrement(arr)
# print(result)
# def appendToList():
#     result_list=[]
#     result_list.append(a)
#     result_list.append(b)
#     result_list.append(c)
#     return result_list
# a,b,c=4,5,0
# print(appendToList(a,b,c))
# def append(*args):
#     result=[]
#     for item in args:
#         result.append(item)
#     return result

# print(append(2,34,5))
# Find the Maximum of two numbers in Python
a=7
b=3
# print(max(a,b))
# ternary operator
# print(a if a>b else b)
# if a>b:
#     print(a)
# else:
#     print(b)
# How To Find the Length of a List in Python
# a = [1, 2, 3, 4, 5]
# print(len(a))
# a=[1,2,3,45]
# c=0
# for i in a:
#     c+=1
# print(c)









    




        
        
        


    
    
    


    
    
    
    
    
    

    

