# Day 4 - testing what I know
import time 
import sys

print("hello user")

age = int(input("How old are you? "))

if age != 23:
    print("You are not the owner of this code.")
    sys.exit()
else:
    print("Okay you're age is right...")

name = str(input("What is your name? "))

if name != ("i am nooone"):
    print('that is correct')
else:
    print('wrong answer')
    sys.exit()
    
print ('You have gotten this right so far. let\'s continue') 

starting_funds = 10000
expenses = 10000
made = 100000

question1 = int(input("You are starting your life, and have $10,000 to begin. What will you have after you split it with everyone?" ))
if question1 >=1:
    print("that is right, you will more since you invested in something you believed in")
elif question1 <= 0:
    print("that is incorrect. Do you have little faith in those around you?")
    sys.exit()
else:
    print("that's not quite right")
    sys.exit()

print(
        f"""start with {starting_funds} and you spend {expenses} with a little patience 
        will give you {made} at the end of the day. 
        You have made it to the end of this test. Congratulations!"""
    )

countdown = 10
while countdown > 0:
    print(countdown)
    time.sleep(1)
    countdown = countdown - 1

list = ['funding', 'work-ethic', 'income', 'enviroment']
for i in range(4):
    print(f'{i + 1}: you need {list[i]}')

print("and this is how fast you will have your money grow")

countup = 1 
while countup < 1000000:
    countup = countup * 2 
    time.sleep(1)
    print(countup)

answer = str(input('you ready for this? '))
if answer == "no":
    print("the door is right there")
else:
    print('then get to work')

yourname = str(input('SAY YOUR NAME '))
capitalized_input = yourname.capitalize()

print(f"Result: {capitalized_input}")
