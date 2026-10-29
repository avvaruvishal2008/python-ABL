#3. Simple Student Attendance Checker

#1. Problem Statement
'''Write a Python program to calculate attendance percentage and check whether a student is eligible when attendance is at least 75%.'''


#2. Objectives
'''	Read total classes and attended classes.
	Calculate attendance percentage.
	Check eligibility using a condition.'''


#3. Assumptions
'''	Total classes must be greater than zero.
	Attended classes cannot exceed total classes.
	Attendance of 75% or more is eligible.'''


#4. Algorithm
'''1. Start the program.
   2. Read total classes and attended classes.
   3. Calculate percentage = attended / total * 100.
   4. If percentage is at least 75, display Eligible; otherwise display Not Eligible.
   5. Display attendance percentage.
   6. Stop.'''


#5. Mermaid Flowchart Code (Descriptive)
'''flowchart TD
    A([Start]) --> B[/Enter total and attended classes/]
    B --> C[Calculate attendance percentage]
    C --> D{Is percentage at least 75?}
    D -- Yes --> E[Display Eligible]
    D -- No --> F[Display Not Eligible]
    E --> G([Stop])
    F --> G'''


#6. Pseudocode
'''START
INPUT total_classes, attended_classes
percentage <- attended_classes / total_classes * 100
IF percentage >= 75 THEN
    OUTPUT "Eligible"
ELSE
    OUTPUT "Not Eligible"
END IF
OUTPUT percentage
STOP'''


#7. Python Source Code
total_classes = int(input("Enter total classes: "))
attended_classes = int(input("Enter classes attended: "))

percentage = attended_classes / total_classes * 100

print("Attendance percentage:", percentage, "%")

if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")


#8. Output Screenshot
'''Sample console output:
Enter total classes: 100
Enter classes attended: 80
Attendance percentage: 80.0 %
Eligible'''


#9. Conclusion
'''The program calculates attendance percentage and checks eligibility against the 75% requirement.'''

 