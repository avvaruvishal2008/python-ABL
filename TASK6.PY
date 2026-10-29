#6. Temperature Converter

#1. Problem Statement
'''Write a Python program to convert a temperature from Celsius to Fahrenheit.'''


#2. Objectives
'''	Read a temperature in Celsius.
	Apply the conversion formula.
	Display the Fahrenheit temperature.'''


#3. Assumptions
'''	The input is a numeric temperature in Celsius.
	Formula: Fahrenheit = (Celsius * 9/5) + 32.'''


#4. Algorithm
'''1. Start the program.
   2. Read Celsius temperature.
   3. Calculate Fahrenheit = (Celsius * 9 / 5) + 32.
   4. Display Fahrenheit temperature.
   5. Stop.'''


#5. Mermaid Flowchart Code (Descriptive)
'''flowchart TD
    A([Start]) --> B[/Enter Celsius temperature/]
    B --> C[Calculate Fahrenheit = Celsius * 9 % 5 + 32]
    C --> D[/Display Fahrenheit temperature/]
    D --> E([Stop])'''


#6. Pseudocode
'''START
INPUT celsius
fahrenheit <- (celsius * 9 / 5) + 32
OUTPUT fahrenheit
STOP'''


#7. Python Source Code
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Fahrenheit:", fahrenheit)


#8. Output 
'''Sample console output:
Enter temperature in Celsius: 25
Temperature in Fahrenheit: 77.0'''


#9. Conclusion
'''The program uses a mathematical formula to convert Celsius into Fahrenheit.'''

 