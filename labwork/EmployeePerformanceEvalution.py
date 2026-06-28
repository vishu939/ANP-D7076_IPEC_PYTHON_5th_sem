# Employee Performance Evaluation

project_score = int(input("Enter Project Score: "))
attendance = int(input("Enter Attendance Percentage: "))
client_feedback = int(input("Enter Client Feedback Score: "))

# Rating Logic
if project_score > 90 and attendance > 90 and client_feedback > 90:
    rating = "Excellent"
elif project_score > 75 and attendance > 75 and client_feedback > 75:
    rating = "Good"
elif project_score > 60 and attendance > 60 and client_feedback > 60:
    rating = "Average"
else:
    rating = "Poor"

# Additional Rule: Attendance below 70% cannot exceed Average
reason = None
if attendance < 70:
    if rating in ["Excellent", "Good"]:
        rating = "Average"
        reason = "Attendance below 70%"

# Output
print("Performance Rating:", rating)
if reason:
    print("Reason:", reason)
