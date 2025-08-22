# Print all names in 'grades' using a loop who scored above 80.

grades = {
    'Fifi': 6,
    'Riri': 88,
    'Loulou': 56
}

for each in grades:
    if grades[each] > 80:
        print(each)