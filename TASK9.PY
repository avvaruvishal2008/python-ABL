#9. Largest of Three Numbers

#1. Problem Statement
'''Write a Python program to read three numbers and display the largest number.'''


#2. Objectives
'''	Read three numbers.
	Compare the numbers using conditions.
	Display the largest value.'''


#3. Assumptions
'''	The three inputs are numeric values.
	If values are equal, the program still displays the correct largest value.'''


#4. Algorithm
'''1. Start the program.
   2. Read a, b, and c.
   3. If a is greater than or equal to b and c, largest = a.
   4. Otherwise, if b is greater than or equal to a and c, largest = b.
   5. Otherwise, largest = c.
   6. Display the largest number.
   7. Stop.'''


#5. Mermaid Flowchart Code (Descriptive)
'''flowchart TD
    A([Start]) --> B[/Enter three numbers a, b and c/]
    B --> C{Is a at least b and c?}
    C -- Yes --> D[largest = a]
    C -- No --> E{Is b at least a and c?}
    E -- Yes --> F[largest = b]
    E -- No --> G[largest = c]
    D --> H[/Display largest number/]
    F --> H
    G --> H
    H --> I([Stop])'''


#6. Pseudocode
'''START
INPUT a, b, c
IF a >= b AND a >= c THEN
    largest <- a
ELSE IF b >= a AND b >= c THEN
    largest <- b
ELSE
    largest <- c
END IF
OUTPUT largest
STOP'''


#7. Python Source Code
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number:", largest)


#8. Output 
'''Sample console output:
Enter first number: 10
Enter second number: 25
Enter third number: 15
Largest number: 25.0'''


#9. Conclusion
'''The program uses if-elif-else statements to compare three numbers and display the largest.'''

 