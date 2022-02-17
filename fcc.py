# first code in python
import numbers
import string
from turtle import color


print("Hello World")

# Drawing in python

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# Variables and Data types

print("There once was a man named George, ")
print("he was 70 years old. ")
print("he really liked the name George, ")
print("but didn't like being 70. ")

# Creating Variables

character_name = "Tom"
character_age = "35"

print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old.")

character_name = "Mike"
character_age = "45"
print("he really liked the name "  + character_name + ",")
print("but didn't like being "  + character_age + ".")

# types of data 

    # string
    # numbers
    # boolean

# Working with strings in python 


print("   Free code camp \nBeginners Tutorial on python")

phrase = "Freecodecamp"
print(phrase + " is cool")    # concantanation with variables

phrase = "Freecodecamp"
print(phrase.upper())    # make or convert strings uppercase

phrase = "Freecodecamp"
print(phrase.isupper())    # check if string is upper case or lower case

         # combination with each other

phrase = "Freecodecamp"
print(phrase.upper().isupper()) 

# check for the length of the string

phrase = "Freecodecamp"
print(len(phrase))       # len is the lenth function

# get individual characters inside string

phrase = "Freecodecamp"
print(phrase[4])  # strings starts with index "zero"


phrase = "Freecodecamp"
print(phrase.index("d")) # we can also get the index from the string

# replace function 

phrase = "Freecodecamp"
print(phrase.replace("Free", "Donation based ")) # we can replace certain words and letters with replace function


# working with numbers in python

print(-2.078) # we can use decimals and also use negative numbers
  
  # basic arithmetic
  
print(25 % 2) # we can use + - * / also modulus 10 % 3

my_num = 5
print(my_num)

# print numbers with strings

my_num = 5
print(str(my_num) + " is my number") # any time we use number string we should use str() function

      # functions related to numbers 

my_num = -25
print(abs(my_num))  # to get absolute value of a number use "abs"

my_num = -25
print(pow(3, 2))  # "pow" funtion to taking and raising its power 

       # max and min function

my_num = -25
print(max(3, 2))

my_num = -25
print(min(3, 2))

      # round function

my_num = -25
print(round(30.7))      

  # import function

from math import *

my_num = -25
print(floor(30.7))  # round the number to lowest
print(ceil(30.7))   # round the number to the highest

# squareroot function

my_num = -5
print(sqrt(25))

# getting input from users

input("Enter your name: ")

# storing input in a variables

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)

# get  input from user to build a basic calculator

num1 = input("Enter a Number: ")
num2 = input("Enter another Number: ")
result = int(num1) + int(num2)  # special python fuction to convert string to numbers
print(result)                   # int fuction only works for round numbers

num1 = input("Enter a Number: ")
num2 = input("Enter another Number: ")
result = float(num1) + float(num2)  # special python fuction to convert string to numbers
print(result)                       # float fuction is used for decimal numbers


# Madlibs game in python

print("Roses are red")
print("Violets are blue")
print("I love you")


color = input("Enter a color: ")
plural_noun = input("Enter a Plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)  

# Lists in python

friends = ["Aravind", "Prince", "Umesh"]
print(friends[0]) # we can also give negative index like -1 it will print the last element 

friends = ["Aravind", "Prince", "Umesh"]
print(friends[1:]) # we can give this to print the index starting from 1 to number of elements in the list

   # we can also update the elements in a list

friends = ["Aravind", "Prince", "Umesh"]
friends[1] = "Ashraf"
print(friends[1])

# List Functions
  
  # add two lists using .extend function


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "jim", "oscar", "Tom"] 
friends.extend(lucky_numbers)
  
  # add two lists using .append function

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "jim", "oscar", "Tom"] 
friends.append(lucky_numbers)
print(friends) 

   # we can also add a elemenst to end of the list

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "jim", "oscar", "Tom"] 
friends.append("mike")
print(friends) 

  # if we want to insert in required index position

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "jim", "oscar", "Tom"] 
friends.insert(1, "kelly")  # we put the index value for the element needed to insert and elemeny
print(friends) 

   # we can also remove elements using remove list function

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "jim", "oscar", "Tom"] 
friends.remove("jim")
print(friends) 

   # we can also clear the list using .clear list function

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "jim", "oscar", "Tom"] 
friends.clear()
print(friends) 

   # pop list fuction removes an element from the list

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "jim", "oscar", "Tom"] 
friends.pop()
print(friends) 

 # check for a element or its index in a list

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "jim", "oscar", "Tom"] 
print(friends.index("kevin")) 


 # check for the number of same values in a list

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "jim", "jim", "oscar", "Tom"] 
print(friends.count("jim")) 

 # .sort list function for sorting elements in list in ascending alphabetical order
 
lucky_numbers = [4, 8, 42, 16, 23, 10]
friends = ["Kevin", "Karen", "jim", "jim", "oscar", "Tom"] 
lucky_numbers.sort()
print(lucky_numbers) 

 # we can also reverse the order of elements in a list

lucky_numbers = [4, 8, 42, 16, 23, 10]
friends = ["Kevin", "Karen", "jim", "jim", "oscar", "Tom"] 
lucky_numbers.reverse()
print(lucky_numbers) 


  # copy a list using .copy

lucky_numbers = [4, 8, 42, 16, 23, 10]
friends = ["Kevin", "Karen", "jim", "jim", "oscar", "Tom"] 
friends2 = friends.copy()
print(friends2)


# Tuples in python (it is a type of data structure or container where we can store some data)
      # Tuple is immutable (cannot change anything in a tuple)

coordinates = (4, 5)
print(coordinates[0])  # accessing elements in a tuble by indexes

   # only store data which cannot be mutated(changed)

# Functions
  
  # Function is a collection of code 
  # create a fuction

def sayhi():
   print("Hello User")

 # the code inside of a fuction only gets executed only when we specify when we want to by calling the fuction name
sayhi()

     # only use lower case
  
  # giving parameters to fuctions

def sayhi(name):
   print("Hello " + name)

sayhi("Mike")

def sayhi(name, age):
   print("Hello " + name + ", you are " + age)

sayhi("Mike", "35")
sayhi("steve", "40")

# Return statements

  # collection of steps for a specific function
  # .return keyword is used to return information from fuction

def cube(num):
  return num*num*num

print(cube(3))  

# def cube(num):
#   return num*num*num

# result = cube(4)
# print(result)
   
# if statements 

is_male = True # setting a variable

if is_male: # if statement for condition is true
  print("You are a male")
else:   # if statement for condtion is false
  print("You are not a male")  


is_male = True # setting a variable
is_tall = True # setting a second variable

if is_male or is_tall:
  print("You are a male or tall or both")
else:   # if statement for condtion is false
  print("You are not a male nor tall")

  # and for a required type of condtion

is_male = True # setting a variable
is_tall = False # setting a second variable

if is_male and is_tall:
  print("You are a male or tall or both")
else:   # if statement for condtion is false
  print("You are not a male nor tall")

  # elif condition

is_male = False # setting a variable
is_tall = True # setting a second variable

if is_male and is_tall:
  print("You are a male")

elif is_male and not(is_tall):
  print("you are a short male")

elif not(is_male) and is_tall:
  print("you are not a male but tall")
else:   # if statement for condtion is false
  print("You are not a male nor tall")

# if statements & comparisions

def max_num(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:  # comparing num1 to num2 and num3
    return num1
  elif num1 >= num3 and num2 >= num3:
    return num2
  else:
    return num3     

print(max_num(300, 40, 500)) 
   

# Building a calculator

num1 = float(input("Enter first number: "))
op = float(input("Enter operator: "))
num1 = float(input("Enter second number: "))

if op == "+":
  print(num1 + num2)
elif op == "-":
  print(num1 - num2)
elif op == "/":
  print(num1 / num2)
elif op == "%":
  print(num1 % num2)    

# Dictionaries

month_Conversions = {
  "jan": "January",
  "Feb": "Febraury",
  "Mar": "March"
}

print(month_Conversions.get("Mar"))

# While Loops

i = 1
while i <= 10:
  print(i)
  i += 1

print("Done with Loop")

# Building a Guessing Game
        # creating required variables
secret_word = "King" 
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
         # creating a loop to check the secret word
while guess != secret_word and not(out_of_guesses):
  if guess_count < guess_limit:
    guess = input("Enter Guess: ")
    guess_count += 1
  else: 
    out_of_guesses = True  

if out_of_guesses:
  print("out of guesses, you lose")
else:  
  print("You Win")

# For loops Examples

for letter in "Free code camp":
  print(letter)

friends = ["jim", "karen", "john"]
for friend in friends:
  print(friend)

friends = ["jim", "karen", "john"]
for index in range(10):
  print(index)

# Exponent Function using loops

def power(base_num, pow_num):
  result = 1
  for index in range(pow_num):
    result = result * base_num
  return result  

print(power(2, 3))

# 2D Lists and Nested Loops

number_grid = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

print(number_grid[1][2]) # accessing elements in array

number_grid = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

for row in number_grid:
  for col in row:
    print(col)

#  Building a translator

def translate(phrase):
  translation = ""
  for letter in phrase:
    if letter.loer() in "aeiou":
      if letter .isupper():
        translation = translation + "G"
    else:
      translation = translation + "g"
  return translation

print(translate(input("Enter a Phrase: ")))

# Comments are ignored by the python when execution

# Try/Except

try:
    number = int(input("Enter a Number: ")) 
    print(number)
except:
  print("Invalid Input")
   
