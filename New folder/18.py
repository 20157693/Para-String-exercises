# Find the average of all values in 'grades' using a loop.

sum = 0
grades = {
    'Fifi': 6,
    'Riri': 78,
    'Loulou': 56
}

for each in grades:
    sum += grades[each]

mean = sum / len(grades)
print(mean)