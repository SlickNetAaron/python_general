def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    
    return the_mean

def mean_better(value):
    if isinstance(value, dict) :
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    
    return the_mean

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
students_grades ={ "Jesse": 9.3, "Joe": 9.4, "George": 9.9 }
max_value = max(student_grades)
print(max_value)
print(student_grades.count(10.0))
username = "Python3"
print(username.lower() )

print(mean(student_grades))
print(mean(students_grades))

print(mean_better(student_grades))
print(mean_better(students_grades))