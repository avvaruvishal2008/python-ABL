#8. Multiplication Table

#1. Problem Statement
'''Write a Python program to display the multiplication table of a number from 1 to 10.'''


#2. Objectives
'''	Read a number.
	Use a for loop from 1 to 10.
	Display each multiplication result.'''


#3. Assumptions
'''    The input is an integer.
	The table is displayed from 1 to 10.'''


#4. Algorithm
'''1. Start the program.
   2. Read a number n.
   3. Repeat i from 1 to 10.
   4. Display n * i for each value of i.
   5. Stop.'''


#5. Mermaid Flowchart Code (Descriptive)
'''flowchart TD
    A([Start]) --> B[/Enter a number n/]
    B --> C[Set i = 1]
    C --> D{i is at most 10?}
    D -- Yes --> E[Display n * i]
    E --> F[Increase i by 1]
    F --> D
    D -- No --> G([Stop])'''


#6. Pseudocode
'''START
INPUT n
FOR i ← 1 TO 10 DO
    OUTPUT n, "×", i, "=", n × i
END FOR
STOP'''


#7. Python Source Code
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


#8. Output 
'''Sample console output:
Enter a number: 3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30'''


#9. Conclusion
'''The program demonstrates a for loop by displaying the multiplication table of a given number.''' 