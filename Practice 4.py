age = int(input('Enter your age: '))
if age < 18:
    print('youre finally getting it')
elif age >= 18 and age < 30:
    print ('you have only till 30')
else:
    print('youre too old') 

print('part1')  

for i in range(5):
    if i %2 == 1:
        print(i)

print('part2)')

countdown = 20
while countdown > -5:
    if countdown % 2 == 1:
        print(countdown)
    countdown = countdown - 1

List_of_numbers = [23, 53, 534, 45, 223]
average = sum(List_of_numbers) / len(List_of_numbers)
print(("the answer to the random numbers is: ") + str(average))
print(f'the average is {average}')

here_are_some_movies = ['boom12', 'boom23', 'boom32']
print('here they are in order')
for i in range(3):
    print(f"{i + 1} is: {here_are_some_movies[i]}")
    

