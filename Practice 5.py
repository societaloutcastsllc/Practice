student = 'John'
test_scores = [85, 92, 78] 
grade = sum(test_scores) / 3

print(f'Student name is: {student}')
print(f'{student} got an average test score of {grade}')
if grade >= 90:
        print(f'{student} got an A')
elif grade >= 80:
        print(f'{student} got a B')
elif grade >= 70:
        print(f'{student} got a C')
else:
        print(f'{student} got a F')
for i in range(len(test_scores)):
    print(f'Score {i + 1}: {test_scores[i]}')

