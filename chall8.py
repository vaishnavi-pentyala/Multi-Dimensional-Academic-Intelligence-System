import random
import pandas as pd
import numpy as np
import math
def generate_data(n):
    students = []
    for i in range(n):
        student_id = f"S{i+1}"
        marks = random.randint(0,100)
        attendance = random.randint(0,100)
        assignment = random.randint(0,50)

        students.append((student_id, marks, attendance, assignment))

    return students
def classify_students(data):
    categories = {}

    for student in data:
        sid, marks, attendance, assignment = student

        if marks < 40 or attendance < 50:
            category = "At Risk"
        elif 40 <= marks <= 70:
            category = "Average"
        elif 71 <= marks <= 90:
            category = "Good"
        elif marks > 90 and attendance > 80:
            category = "Top Performer"
        else:
            category = "Good"

        categories[sid] = category

    return categories
def analyze_data(df):

    marks = df["Marks"]

    mean_marks = np.mean(marks)
    median_marks = np.median(marks)
    variance = np.mean((marks - mean_marks) ** 2)
    std_dev = math.sqrt(variance)
    max_marks = np.max(marks)
    correlation = np.corrcoef(df["Marks"], df["Attendance"])[0][1]

    normalized = (marks - marks.min()) / (marks.max() - marks.min())
    df["Normalized Marks"] = normalized

    summary_tuple = (mean_marks, std_dev, max_marks)

    return summary_tuple, correlation

roll = input("Enter your roll number: ")

num_students = int(roll[-1])   # last digit

if num_students == 0:
    num_students = 10

student_data = generate_data(num_students)

df = pd.DataFrame(student_data, columns=[
    "Student_ID","Marks","Attendance","Assignment"
])

df["Performance_Index"] = (df["Marks"]*0.6 + df["Assignment"]*0.4) * np.log(df["Attendance"]+1)

categories = classify_students(student_data)

summary, correlation = analyze_data(df)

std_dev = summary[1]
top_count = list(categories.values()).count("Top Performer")
attendance_risk = len(df[df["Attendance"] < 50])

if std_dev < 15:
    insight = "Stable Academic System"
elif attendance_risk > 3:
    insight = "Critical Attention Required"
elif top_count >= 2:
    insight = "High Achievement"
else:
    insight = "Moderate Performance"


print("\n--- Student DataFrame ---")
print(df)

print("\n--- Student Categories ---")
print(categories)

print("\n--- Statistical Summary (mean, std_dev, max_marks) ---")
print(summary)

print("\nCorrelation (Marks vs Attendance):", correlation)

print("\nFinal System Insight:", insight)