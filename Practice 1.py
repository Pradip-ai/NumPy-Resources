#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


2 + 3 +9


# In[ ]:


99-73


# In[ ]:


100/7


# In[ ]:


100//7


# In[ ]:


100 % 7


# In[ ]:


5 **3


# In[ ]:


((2 +5)) * (17-3) / (4 **3)


# In[ ]:


#solving a multi steps problems using variables

cost_of_ice_bag = 1.25
profit_margin = 0.2
profit_per_bag = 1.25 * 0.2
no_of_bag = 500
TP = no_of_bag * profit_per_bag
print(TP)


# In[ ]:





# In[ ]:


profit_margin


# In[ ]:


profit_margin


# In[ ]:


print('The grocessary store makes a profit of', TP)


# In[ ]:


""""Evalulating using conditions variable"""


# In[ ]:





# In[ ]:


a = 1
b =2
print(a!=b)


# In[ ]:


#combining conditions with logical operator

print(a or b)
print(a and b)


# In[ ]:


a < 0 or True


# In[ ]:


get_ipython().system('pip install jovian --upgrade --quiet')


# In[ ]:


import jovian


# In[ ]:


jovian.commit(project= 'First setps with python')


# In[ ]:


#variable and data types
my_favourite_color = 'blue'
print(my_favourite_color)


# In[ ]:


color1 = color2 = color3 = 'red'
print(color1)


# In[ ]:





# In[ ]:


profit_margin


# In[ ]:





# In[ ]:





# In[ ]:


a = 'b'
b = 'c'
print(a != b)


# In[ ]:


profit_margin


# In[ ]:


my_favourite_color = 'blue'
print(my_favourite_color)


# In[ ]:


my_favourite_color = 'red'
print(my_favourite_color)


# In[ ]:


a = 10
a += 4


# In[ ]:


print(a)


# In[ ]:


#Type
a = '0.3333'
print(type(a))


# In[ ]:


current_year = 2022
print(type(current_year))


# In[ ]:


a = 1e-5
print(type(a))


# In[ ]:


float(current_year)


# In[ ]:


pi = 3.1444
print(int(pi))


# In[ ]:


pi = 3.1444
print(int(pi))


# In[ ]:


current_year = 2022
print(type(current_year))


# In[ ]:


current_year = 2022
print(type(current_year))


# In[ ]:





# In[ ]:


nothing = 'none'
type(nothing)


# In[ ]:


today = 'monday'
type(today)


# In[ ]:


a = 'pradip\'s name'
print(a)


# In[ ]:


a = 'pradip'
len(a)


# In[ ]:


list(a)


# In[ ]:


len(helllllllllllllllllo)


# In[ ]:


list(a)


# In[ ]:


'ip' in a


# In[ ]:


full_name = 'Pradip Bhatta'
greeting = 'Hello'
greeting + " " + full_name


# In[ ]:


a = "ram"
a.capitalize()


# In[ ]:


a = "ram"
a.upper()


# In[ ]:


another_day = 'monday'

another_day.replace('monday', 'tuesday')


# In[ ]:


another_day = 'Call'


another_day.strip()


# In[ ]:


name = 'pradip'
last_name = 'bhatta'

print(f' hello {name} {last_name} How are you?')


# In[ ]:


#list 
fruits = ['a', 'b']
type(fruits)


# In[ ]:


len(fruits)


# In[ ]:


fruits[-2]


# In[ ]:


House = ['room', 'kitchen', 'bathroom', 'dinein', fruits, 'toilet']

House


# In[ ]:


House[2:10]


# In[ ]:


list(House[2:10])


# In[ ]:


House[1] = 'Room2'


# In[ ]:


House


# In[ ]:


House = ['room', 'kitchen', 'bathroom', 'dinein', fruits, 'toilet']

House[1] = 'Room2'
House


# In[ ]:


House.append('Car')
House


# In[ ]:


House.insert(1, 'Room3')
list(House)


# In[ ]:





# In[ ]:


person1 ={
    'name': 'Pradip',
    'sex': 'male',
    'age': 32,
    'married': 'single'
}
print(person1)


# In[ ]:


type(person1)


# In[ ]:


person1['name']


# In[ ]:


person1['age']


# In[ ]:


'name' in person1


# In[ ]:


person1['address'] = '1, cassie Street'


# In[ ]:


person1


# In[ ]:


person1['work'] = '1, Part-time'
person1


# In[ ]:


person1.values()


# In[ ]:


#Branching, Loops and function
a_number = 33
if a_number % 2 == 0:
    print('We are in if block')
    print(f'The given number {a_number} is even.')
else:
    print(f'The given number {a_number} is odd.')
    
    

    
    


# In[ ]:


home_1= ('room', 'kitchen,' 'bathroom')
anusha = 'Renting a house'
if anusha in home_1:
    
    
    print(f' Anusha is {anusha} with a (home[1]) in city')
    


# In[ ]:


today = 'monday'
type(today)


# In[ ]:


a_number = 49
if a_number % 2 == 0:
    print(f' {a_number} is divisible by 2')
    


# In[ ]:


a_number = 33
if a_number % 2 == 0:
    print('We are in if block')
    print(f'The given number {a_number} is even.')
else:
    print(f'The given number {a_number} is odd.')


# In[ ]:


a_number = 12.5
if a_number % 2 == 0:
    print(f' {a_number} is divisible by 2')
elif a_number % 3 == 0:
    print(f' {a_number} is divisible by 3')

else:
    print('The check is failed')
    print('The number is not divisible by 2 and 3')
    


# In[ ]:


x = 5
y = 6
if x > y:
    print('The condiotn is true')
else:
    print('Invalid')
    


# In[ ]:


baby = '0-4'
childern = '4-12'
adult = '13-19'
young = '20-30'

if childern:
    print('This level of kids falls in young')
else:
    print('This level falls in young')

    


# In[ ]:


#if statement

test_value = 100
if test_value > 1000:

    print('This is valid')
    

else:
    print('Program continue can not to work')
    


# In[ ]:


n = int(input('Input the number:'))
if n <5:
    print('Baby')
    
elif n < 18:
    print('Children')
elif n < 26:
    print('Young adult')
elif n < 60:
    print('Adult Adult')
else:
    print('old')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


n = int(input('Input the number'))
if n <5:
    print('Baby')
    
elif n < 18:
    print('Children')
elif n < 26:
    print('Young adult')
elif n < 60:
    print('Adult Adult')
else:
    print('old')


# In[ ]:


age = int(input('Enter your age'))
if age > 18:
    print('Eligible for voting')
    
else:
    print('Not eligible for voting')


# In[ ]:


n = int(input('Enter your number'))

if n % 7 == 0:
    print('This is divisble by 7')
else:
    print('This is not divisble by ')
    


# In[ ]:


number= int(input('Enter you number'))
if number %5 == 0:
    print('Hello')
    
else:
    print('Bye')


# In[ ]:


nu = int(input("Enter you total units"))
if nu <= 100:
    print('No charge')
    
elif nu <=200:
    amount = (nu - 100) * 5
    print("Amount to pay :",amt)
    


# In[ ]:


amt=0
nu=int(input( "Enter number of electric unit"))
if nu<=100:
     amt=0
if nu>100 and nu<=200:
     amt=(nu-100)*5
if nu>200:
     amt=500+(nu-200)*10
print("Amount to pay :",amt)


# In[ ]:


amt=0
nu=int(input( "Enter number of electric unit"))
if nu<=100:
     amt=0
if nu>100 and nu<=200:
     amt=(nu-100)*5
if nu>200:
     amt=500+(nu-200)*10
print("Amount to pay :",amt)


# In[ ]:


get_ipython().run_cell_magic('time', '', "re = 1\ni = 1\nwhile i <= 1000:\n    re = re * i\n    i = i+1\n    \nprint(f' The factorial of 100 is: {re} ')")


# In[ ]:


line = '*'
max_lenght = 10
while len(line) <= max_lenght:
    print(line)
    line += "*"
    
while  len(line) > 0:
    print(line)
    line = line[:-1]


# In[ ]:


i = 1
while i < 6:
    print(i)
    i += 1


# In[ ]:


n = 5
while n > 0:
    n -= 1
    print(n)


# In[ ]:


n = 5
while n > 4:
    n = n -1
    print(n)
else: 
    print('Invalid')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


n = 5
while n > 4:
    n = n -1
    print(n)


# In[ ]:


get_ipython().run_cell_magic('time', '', 'n = 1000\nwhile n > 0:\n    print(n)\n    n -=1')


# In[ ]:


line = '*'
max_lenght = 10
while  <= max_lenght:
   print(line)
   line += "*"


# In[ ]:


line = '*'
max_lenght = 10
while len(line) <= max_lenght:
    print(line)
    line += "*"
    
while  len(line) > 0:
    print(line)
    line = line[:-1]


# In[ ]:


line = '*'
max_lenght = 10
while len(line) <= max_lenght:
    print(line)
    line += "*"
    
while  len(line) > 0:
    print(line)
    line = line[:-1]


# In[ ]:


line = '*'
max_lenght = 10
while len(line) <= max_lenght:
    print(line)
    line += "*"


# In[ ]:


n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended.')


# In[ ]:


n = 6
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended a nd dinshhfjisjkn')
    


# In[ ]:


i = 1
re = 1
while i < 20:
    i += 1
    print(i)
    if i % 2 == 0:
        print(f' Skipping {i}')
        continue
    print(f' Multiplying with {i}')
    re = re * i
print('i:' , i)
print('re:', re)


# In[ ]:


a_1= input('What is your name?')
a = input(f' Hi {a}, What is your dream?')
a = input(f' its alright {a_1}, you will get your dream job')



# In[ ]:


a_1= input('What is your name?')
a = input(f' Hi {a_1}, What\'s your dream?')
a = input(f' its alright {a_1}, you will get your dream job')
a= input('Are you in Love?')
print('Your Boyfriend is cute, and he Loves you so much. Pradip is saying No matter what happens, you will be always my girlfriend, my world, and my life. I love you.')


# In[ ]:


a_1= input('What is your name?')
a = input(f' Hi {a_1}, What\'s your dream?')
a = input(f' its alright {a_1}, you will get your dream job')


# In[ ]:


a_1= input('What is your name?')
a = input(f' Hi {a_1}, What\'s your dream job?')
a = input(f' its alright {a_1}, you will get your dream job')
a= input('Are you in Love?')
print('Your Boyfriend is cute, and he Loves you so much. Pradip is saying No matter what happens, you will be always my girlfriend, my world, and my life. I love you.')


# In[ ]:





# In[ ]:


days = ['monday', 'tuesday', 'wednesday']
for day in days:
    print(day)
    


# In[ ]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    break
    x == 'banana'
print(x)


# In[ ]:


for x in "banana":
  print(x)


# In[ ]:


for x in "car":
    print(x)


# In[ ]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


# In[ ]:


fruits = ['a', 'b', 'v', 'd']
for x in fruits:
    print(x)
    if x == 'v':
        break


# In[ ]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


# In[ ]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(f' Here is the fruits details {fruits[0]}: Come and have yourself')
    print(f' Here is the fruits details {fruits[1]}: Come and have yourself')
    print(f' Here is the fruits details {fruits[2]}: Come and have yourself')
    


# In[ ]:


person = {
    'name' :'pradip',
    'age' :24,
    'sex' : 'male',
    'married' :  'single'
}

for key in person:
    print('key:', key, ', ', 'value:', person[key])


# In[ ]:


for i in range(7, 16, 4):
    print(i)


# In[ ]:


fruits = ["apple", "banana", "cherry"]
for fruits in range(len(fruits)):
    print(fruits)


# In[ ]:


# Defining a functions

def say_hello():
    print('Hello There')
    print('How are you')


# In[ ]:


def say_hello():
    print('Hello There')
    print('How are you')
say_hello()


# In[ ]:


say_hello()


# In[ ]:


def say_hello():
    print(f' Hi {say_hello}, How are you?')

    


# In[ ]:


say_hello('Ram')


# In[ ]:


def filter_even(number_list):
    result_list = []
    for number in number_list:
        if number % 2 == 0:
            result_list.append(number)
    return result_list
even_list = filter_even([1, 2, 3, 4, 5])


# In[1]:


#the more function you  wrtie the more experience you will get


def loan_emi(amount):
    emi = amount / 12
    print(f' The emi is {emi}')


# In[3]:


loan_emi(1.26e6)


# In[7]:


def loan_emi(amount, duration, down_payment=0):
    loan_amount = amount - down_payment
    
    emi = loan_amount / duration
    return emi


# In[9]:


emi1 = loan_emi(12000, 8*12, 3e5)
emi1


# In[21]:


def rent_emi(Amount, duration, rate, down_Payemnt=0):
    Loan_amount = Amount- down_Payemnt
    Emi = Loan_amount * rate *((1 + rate)**duration) / (((1+rate)**duration)-1)
    return Emi
         
    


# In[26]:



rent_emi(126000, 8*12, 0.1/12 , 3e5)


# In[17]:


rent_emi(126000, 10*12, 0.08/12)


# In[28]:


def round_up(x):


# In[ ]:




