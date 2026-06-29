# Student Result Analyzer

# Accept number of students
n = int(input("Enter number of students: "))

marks = []   # List to store marks

# Input marks of each student
for i in range(n):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

# Highest Marks
highest = max(marks)

# Lowest Marks
lowest = min(marks)

# Average Marks
average = sum(marks) / n

# Count students who passed (Marks ≥ 40)
passed = 0
# Count students with distinction (Marks ≥ 75)
distinction = 0

for m in marks:
    if m >= 40:
        passed += 1
    if m >= 75:
        distinction += 1

# Output
print("\n--- Result Analysis ---")
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Number of Students Passed:", passed)
print("Number of Students with Distinction:", distinction)
