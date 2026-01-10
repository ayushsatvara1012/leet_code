def gradingStudents(grades):
    # Write your code here
    new_grades = []
    for grade in grades:
        if grade < 38:
            new_grades.append(grade)
        elif grade%5 >= 3:
            new_grades.append(grade+(5-(grade%5)))
        else:
            new_grades.append(grade)
    return new_grades