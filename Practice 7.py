#My First Project

student = ['John', 85, 92, 78], ['Jane', 90, 88, 95], ['Joey', 75, 80, 85], ['Jill', 95, 90, 92], ['Jack', 80, 75, 85]

for student in student:
    name = student[0]
    test_scores = student[1:]
    average = sum(test_scores) / len(test_scores)
    print(f'Student name is: {name}')
    print(f'{name} got an average test score of {average:.2f}')
    
    if average >= 90:
        print(f'{name} got an A')
    elif average >= 80:
        print(f'{name} got a B')
    elif average >= 70:
        print(f'{name} got a C')
    else:
        print(f'{name} got a F')
    
    for i in range(len(test_scores)):
        print(f'Score {i + 1}: {test_scores[i]}')
    
    print('-----------------------------')