# ? Solve some python problems and learn from that
# Que : Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# TODO learn about nested list

#* Static method

std_names = [['ramesh',34],['suresh',55],['rakesh',94],['mahesh',55]]

second_lowest = []

for val in std_names:
    srtList = sorted(std_names,key=lambda x:x[1])
print(srtList)
second_lowest_grade = srtList[1][1]

for item in range(0,len(srtList)):
    if srtList[item][1] == second_lowest_grade:
        second_lowest.append(srtList[item][0])

for i in second_lowest:
    print(i)

#* Dynamic method

# student = []
# num_student = int(input())
#
#
#     for i in range(0,num_student):
#         std_name = str(input(''))
#         std_grades = float(input())
#         student.append([std_name,std_grades])
#
#     student.sort(key=lambda x:x[1])
#     sorted_grades = sorted(set(grade for name,grade in student))
#
#     second_lowest_grade = sorted_grades[1]
#     print(f'Second lowest grade :{second_lowest_grade}')
#     print(f'Sorted grades :{sorted_grades}')
#
#     names = sorted(name for name,grade in student if grade == second_lowest_grade )
#     for item in names:
#         print(item)