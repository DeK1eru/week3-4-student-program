def calculate_average(grades):
    return sum(grades) / len(grades)


name = input("Enter student name: ")

grades_input = input("Enter grades separated by space: ")

grades = list(map(int, grades_input.split()))

average = calculate_average(grades)

print("Student:", name)
print("Grades:", grades)
print("Average:", average)

with open("students.txt", "a") as file:
    file.write(f"{name} {grades} {average}\n")