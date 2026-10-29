#   2. Electricity Bill Calculator

#1. Problem Statement
'''Write a Python program to calculate a simple electricity bill using units consumed. The first 100 units cost rupees2 per unit and units above 100 cost rupees3 per unit.'''


#2. Objectives
'''	Read electricity units consumed.
	Calculate the bill using two slabs.
	Display the final bill amount.'''


#3. Assumptions
'''	Units are zero or more.
	The first 100 units cost ₹2 per unit.
	Every unit above 100 costs ₹3 per unit.
	No fixed charge or tax is included.'''


#4. Algorithm
'''1. Start the program.
   2. Read units consumed.
   3. If units are at most 100, bill = units × 2.
   4. Otherwise, bill = 100 × 2 + (units − 100) × 3.
   5. Display the bill amount.
   6. Stop.'''


#5. Mermaid Flowchart Code (Descriptive)
'''flowchart TD
    A([Start]) --> B[/Enter units consumed/]
    B --> C{Are units at most 100?}
    C -- Yes --> D[Bill = units × 2]
    C -- No --> E[Bill = 100 × 2 + extra units × 3]
    D --> F[/Display bill/]
    E --> F
    F --> G([Stop])'''

#6. Pseudocode
'''START
INPUT units
IF units ≤ 100 THEN
    bill ← units × 2
ELSE
    bill ← 100 × 2 + (units − 100) × 3
END IF
OUTPUT bill
STOP'''


#7. Python Source Code
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 2
else:
    bill = 100 * 2 + (units - 100) * 3


print("Electricity bill: Rs.", bill)


#8. Output Screenshot
'''Sample console output:
Enter units consumed: 150
Electricity bill: Rs. 350'''


#9. Conclusion
'''The program uses if-else conditions to calculate an electricity bill based on two consumption slabs.'''

 