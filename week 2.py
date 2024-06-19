"""DAY 1
USER INPUTS
TYPE CONVERSION

name = str(input("Enter your name: "))
print(f"Dear {name}, Welcome to simple calculator program")
boolean = bool(input("Enter true or false:"))
a = int(input("Enter a number: "))
b = float(input("Enter a second number: "))

add = (a+b)
sub = (a-b)
mul = (a*b)

print(f"the addidtion is {add}, the subtraction is {sub}, the multiplication is {mul}")
print(type(mul))
print(type(boolean))"""

#CW FOR DAY 1: See advanced calcultor file

#DAY 2: CONDITIONAL STATEMENTS? CONTROL FLOW
"""name = str(input("enter your name"))
print(f"{name},welcome to Nigeria's voting registration portal")
age= int(input("Enter your age: "))
if age >= 18:
    print(f"congratulations {name}, you are eligible to vote")
else:
    print(f"sorry {name}, you are not eligible to vote")"""


#are you a student at instinct hub?
"""name = str(input("enter your name:"))
question = str(input("yes or no, are you a student at instict hub?"))
if question == "yes":
    print(f"welcome {name} to instinct hub")
else:
    print(f"sorry {name},please sign up for an account with instinct hub")"""

#PASSWORD?
"""name = str(input("Enter your name:"))
password = str(input("enter your password: "))
if password == "@123":
    print(f"{name}, password correct")
else:
    print(f"sorry {name}, password incorrect. try again")"""

#SCORES
"""90+ A
80 - 89 B 
70 - 79 C
60 - 69 D
50 - 59 E
0 - 49 F 
 elif else if 
 """
score = int(input("Enter your score:"))
if score >= 90 and score <=100: 
    print("Your grade is A")
elif score >= 80 and score <=89:
    print("Your grade B")
elif score >= 70 and score<= 79:
    print("better luck nect time, your grade ia C")
elif score >= 60 and score<= 69 :
    print("you can do better, your grade is D")
elif score >= 50 and score <= 59:
    print("sorry, your grade is E")
elif score >=0 and score<= 49:
    print("you failed, your grade is F")

else: 
    print("Out of range")


