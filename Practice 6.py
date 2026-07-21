student = ('John')
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

#------------------------------------------------------------

balance = 200
withdrawal = 250

if withdrawal <= balance:
    balance = balance - withdrawal
    print("Withdrawal successful. New balance:", balance)
else:
    print("Insufficient funds.")
    
balance = 250
withdrawal = 200

if withdrawal <= balance:
    balance = balance - withdrawal
    print("Withdrawal successful. New balance:", balance)
else:
    print("Insufficient funds.")

#------------------------------------------------------------

name = "claude" 
capitalized_name = name[0].upper() + name[1]
print(capitalized_name)
capitalized_name = name[0].upper() + name[1:]
capitalized_name = name.upper()
print(capitalized_name)

#------------------------------------------------------------


ids_checked = [18, 20, 21, 23] 
has_id = True
for age in ids_checked:
    if has_id and age >= 21:
        print(f'{age}: you can come in')   
    else:
        print(f"{age}: sorry no entry")

#------------------------------------------------------------

countdown = 100
while countdown >= 0:
    print(countdown)
    countdown = countdown - 5
print("Done!")


  
