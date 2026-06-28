# Online Examination Result Analyzer

# Marks input for 5 subjects
hindi = int(input("Enter Hindi Marks: "))
english = int(input("Enter English Marks: "))
maths = int(input("Enter Mathematics Marks: "))
science = int(input("Enter Science Marks: "))
computer = int(input("Enter Computer Marks: "))

marks = [hindi, english, maths, science, computer]

# Step 1: Check if any subject < 40
if any(m < 40 for m in marks):
    result = "FAIL"
    classification = "None"
else:
    # Step 2: Calculate Average
    average = sum(marks) / 5

    # Step 3: Classification
    if average >= 75:
        classification = "Distinction"
    elif average >= 60:
        classification = "First Division"
    elif average >= 50:
        classification = "Second Division"
    elif average >= 40:
        classification = "Pass"
    else:
        classification = "Fail"

    result = "PASS"

    # Output
    print("Average Marks:", average)
    print("Result:", result)
    print("Classification:", classification)
