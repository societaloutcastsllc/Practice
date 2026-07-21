#Write a block that gives differnt answers based off the age the user inputs
age: int = int(input('Enter your age: '))
if age < 18:
    print('You are a minor')
elif age >= 18 and age < 65:
    print('You are an adult')
else: 
    print('damn you are old')

#---------------------------------------
#Write a loop that counts from 1 to 10, but only prints the even numbers
for i in range(11):
    if i % 2 == 0:
        print(i)
#test for countdown
countdown = 10
while countdown > -1:
    if countdown % 2 == 0:
        print(countdown)
    countdown = countdown - 1

#---------------------------------------
#find the average of these three test scores; 85, 92, 78
#option 1
test_score1 = 85
test_score2 = 92
test_score3 = 78
average = (test_score1 + test_score2 + test_score3) / 3
print("The average test score is: " + str(average))
#option 2
test_scores = [85, 92, 78]
average = sum(test_scores) / 3
print("The average test score is: " + str(average))
#option 3
print(f'The average test score is: {average}')

#---------------------------------------
#Make a list of 5 of your favorite movies. Loop through 
#the list and print each one with its position number, 

#option 1
anime1 = "Attack on Titan"
anime2 = "One Piece"
anime3 = "Demon Slayer"
anime4 = "My Hero Academia"
anime5 = "Jujutsu Kaisen"
print("My favorite anime are:")
print(f"1. {anime1}")
print(f"2. {anime2}")
print(f"3. {anime3}")
print(f"4. {anime4}")
print(f"5. {anime5}")
#option 2
favorite_movies = ['step up', 'step up 2', 'step up 3D', 'step up revolution', 'step up all in']
print('This is my favorite movie list:')
for i in range(5):
    print(f"{i + 1} is: {favorite_movies[i]}")
