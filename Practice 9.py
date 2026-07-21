
student1 = ['John', 45, 64, 80, 44, 64]
average1 = (student1[1] + student1[2] + student1[3] + student1[4] + student1[5]) / 5
grade1 = average1

if grade1 >= 90:
    grade1 = "A"
elif grade1 >= 80:
    grade1 = "B"
elif grade1 >= 70:
    grade1 = "C"
else:
    grade1 = "F"

print(f'Student: {student1[0]}| Average score: {average1} | Final Grade: {grade1}')

student2 = ['Jenny', 53, 74, 42, 64, 67]
average2 = (student2[1] + student2[2] + student2[3] + student2[4] + student2[5]) / 5
grade2 = average2

if grade2 >= 90:
    grade2 = "A"
elif grade2 >= 80:
    grade2 = "B"
elif grade2 >= 70:
    grade2 = "C"
else:
    grade2 = "F"

print(f'Student: {student2[0]}| Average score: {average2} | Final Grade: {grade2}')

student3 = ['Jacob', 77, 89, 90, 85, 55]
average3 = (student3[1] + student3[2] + student3[3] + student3[4] + student3[5]) / 5
grade3 = average3

if grade3 >= 90:
    grade3 = "A"
elif grade3 >= 80:
    grade3 = "B"
elif grade3 >= 70:
    grade3 = "C"
else:
    grade3 = "F"

print(f'Student: {student3[0]}| Average score: {average3} | Final Grade: {grade3}')


#----------------------

students = [['Marcus', 45, 64, 80, 44, 64], ['Miller', 53, 74, 42, 64, 67], ['Maui', 90, 99, 90, 98, 95]]
highest_score = 0
highest_name = ''
for s in students:
    name = s[0]
    score = s[1:]
    grade = sum(score) / len(score)
    average = grade
    if grade >= 90:
        grade = "A"
    elif grade >= 80:
        grade = "B"
    elif grade >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f'Name: {name} | Average Score: {average} | Grade: {grade}')
    if average > highest_score:
      highest_score = average
      highest_name = name
print(f'Highest Score was {name} {highest_score}')

# TEST PASSED