unsorted_integers = [5, 2, 3, 1, 4]

sorted_integers = sorted(unsorted_integers)
print(sorted_integers)

student_tuples = [
    ("john", "A", 15),
    ("jane", "B", 12),
    ("dave", "B", 10),
]
sorted_students = sorted(student_tuples, key=lambda student: student[2])  # sort by age
print(sorted_students)
