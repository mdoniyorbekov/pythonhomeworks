import csv

# Step 1: Create grades.csv file
grades_data = [
    ['Name', 'Subject', 'Grade'],
    ['Alice', 'Math', '85'],
    ['Bob', 'Science', '78'],
    ['Carol', 'Math', '92'],
    ['Dave', 'History', '74']
]

with open('grades.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(grades_data)

# Step 2: Read grades.csv and process data
students = []
subject_totals = {}
subject_counts = {}

with open('grades.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Store in list of dictionaries
        students.append(row)
        
        # Convert grade to float for calculations
        grade = float(row['Grade'])
        subject = row['Subject']
        
        # Calculate running totals and counts for averages
        if subject in subject_totals:
            subject_totals[subject] += grade
            subject_counts[subject] += 1
        else:
            subject_totals[subject] = grade
            subject_counts[subject] = 1

# Step 3: Calculate averages
average_grades = []
for subject in subject_totals:
    avg = subject_totals[subject] / subject_counts[subject]
    average_grades.append({'Subject': subject, 'Average Grade': avg})

# Step 4: Write average_grades.csv
with open('average_grades.csv', 'w', newline='') as file:
    fieldnames = ['Subject', 'Average Grade']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(average_grades)

# Optional: Print results to verify
print("Student data:")
for student in students:
    print(student)
    
print("\nAverage grades:")
for avg_grade in average_grades:
    print(f"{avg_grade['Subject']}: {avg_grade['Average Grade']}")