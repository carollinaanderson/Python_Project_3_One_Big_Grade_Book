# Define last semester's gradebook with subjects and grades
last_semester_gradebook = [
    ["politics", 80],
    ["latin", 96],
    ["dance", 97],
    ["architecture", 65]
]

# Create a list of current subjects
subjects = ["physics", "calculus", "poetry", "history"]

# Create a list of current grades
grades = [98, 97, 85, 88]

# Combine subjects and grades into a two-dimensional list called gradebook
gradebook = [
    ["physics", 98],
    ["calculus", 97],
    ["poetry", 85],
    ["history", 88]
]

# Print the current gradebook
print(gradebook)

# Add a new subject and grade for computer science
computer = ["computer science", 100]
gradebook.append(computer)

# Add a new subject and grade for visual arts
viz = ["visual arts", 93]
gradebook.append(viz)

# Update the grade for poetry to 'Pass'
gradebook[2][1] = 'Pass'
