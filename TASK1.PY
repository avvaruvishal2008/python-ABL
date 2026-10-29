#1. Student Grade Calculator
'''1. Problem Statement
Write a Python program to enter marks for three subjects, calculate the total and average, and display Pass if every subject mark is at least 35; otherwise display Fail.'''


#2. Objectives
'''Read marks for three subjects.
	Calculate total and average marks.
	Use an if-else statement to display Pass or Fail.'''


#3. Assumptions
'''Each subject is out of 100 marks.
	Marks entered are whole numbers from 0 to 100.
	A student passes when every subject mark is 35 or above.'''


#4. Algorithm
'''1. Start the program.
   2. Read marks in three subjects.
   3. Calculate total = mark1 + mark2 + mark3.
   4. Calculate average = total / 3.
   5. If every mark is at least 35, display Pass; otherwise display Fail.
   6. Display total and average.
   7. Stop.'''


#5. Mermaid Flowchart Code (Descriptive)
'''flowchart TD
    A([Start]) --> B[/Enter marks for 3 subjects/]
    B --> C[Calculate total and average]
    C --> D{Are all marks at least 35?}
    D -- Yes --> E[Set result to Pass]
    D -- No --> F[Set result to Fail]
    E --> G[/Display total, average and result/]
    F --> G
    G --> H([Stop]).'''


#6. Pseudocode
'''START
INPUT mark1, mark2, mark3
total <- mark1 + mark2 + mark3
average <- total / 3
IF mark1 >= 35 AND mark2 >= 35 AND mark3 >= 35 THEN
    result <- "Pass"
ELSE
    result <- "Fail"
END IF
OUTPUT total, average, result
STOP'''


#7. Python Source Code
mark1 = int(input("Enter marks in subject 1: "))
mark2 = int(input("Enter marks in subject 2: "))
mark3 = int(input("Enter marks in subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
    result = "Pass"
else:
    result = "Fail"

print("Total marks:", total)
print("Average marks:", average)
print("Result:", result)


#8. Output 
'''Sample console output:
Enter marks in subject 1: 70
Enter marks in subject 2: 80
Enter marks in subject 3: 90
Total marks: 240
Average marks: 80.0'''

#9Result: 
'''Pass'''

#10. Conclusion
'''The program calculates total and average marks and uses a condition to decide whether the student passes.'''
