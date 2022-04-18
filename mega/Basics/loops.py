monday_temperatures = [9.1, 8.8, 7.6]

for temperature in monday_temperatures:
    print(round(temperature))

students_grades ={ "Jesse": 9.3, "Joe": 9.4, "George": 9.9 }

for grades in students_grades.items():
    print(grades)

phone_numbers = {"John Smith": "+3178123", "Mary Simpson": "+3214233"}

for k, v in phone_numbers.items():
    print("{} has phone number {}".format(k, v))

username = ''

while username != 'pypy':
    username = input("Enter username: ")

while True:
    username = input("Enter username: ")
    if username == 'pippy':
        break
    else:
        continue

