#7. Factorial Calculator

#1. Problem Statement
'''Write a Python program to find the factorial of a non-negative integer using a for loop.'''


#2. Objectives
'''	Read a non-negative integer.
	Use a loop to multiply numbers.
	Display the factorial.'''


#3. Assumptions
'''	The input is a whole number greater than or equal to zero.
	The factorial of 0 is 1.'''


#4. Algorithm
'''1. Start the program.
   2. Read n.
   3. Set factorial = 1.
   4. Repeat i from 1 to n and multiply factorial by i.
   5. Display factorial.
   6. Stop.'''


#5. Mermaid Flowchart Code (Descriptive)
'''flowchart TD
    A([Start]) --> B[/Enter non-negative integer n/]
    B --> C[Set factorial = 1]
    C --> D{Are there more values from 1 to n?}
    D -- Yes --> E[Multiply factorial by current value]
    E --> D
    D -- No --> F[/Display factorial/]
    F --> G([Stop])'''


#6. Pseudocode
'''START
INPUT n
factorial <- 1
FOR i <- 1 TO n DO
    factorial <- factorial * i
END FOR
OUTPUT factorial
STOP'''


#7. Python Source Code
n = int(input("Enter a non-negative integer: "))
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print("Factorial:", factorial)


#8. Output 
'''Sample console output:
Enter a non-negative integer: 5
Factorial: 120'''


#9. Conclusion
'''The program uses a for loop to calculate the factorial of a non-negative integer.'''

 