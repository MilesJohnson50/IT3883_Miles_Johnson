# Program Name: IT3883 Assignment 2.py
# Course: IT3883 W01
# Student Name: Miles Johnson
# Assignment Number: Assignment 2
# Purpose: Read student names and six scores from an input file, calculate
#          each student's final average, and display the students in
#          descending order by final average.

# Store each student's name and calculated average in this list.
student_averages = []

# Open the provided input file and process one student per line.
with open("Assignment2input.txt", "r") as input_file:
    for line in input_file:
        fields = line.split()

        # The first field is the student's name.
        student_name = fields[0]

        # Convert the remaining six score fields from strings to numbers.
        scores = []
        for score in fields[1:]:
            scores.append(float(score))

        # Calculate the student's average score.
        final_average = sum(scores) / len(scores)

        # Save the name and average together for sorting later.
        student_averages.append((student_name, final_average))

# Sort by the average (the second item in each tuple) from highest to lowest.
student_averages.sort(key=lambda student: student[1], reverse=True)

# Print each student's name and average rounded to two decimal places.
for student_name, final_average in student_averages:
    print(f"{student_name} {final_average:.2f}")
