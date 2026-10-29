#10. Count Vowels in a String

#1. Problem Statement
'''Write a Python program to count the vowels in a word or sentence.'''


#2. Objectives
'''	Read a string.
	Check each character against the vowels.
	Display the total number of vowels.'''


#3. Assumptions
'''	The input is a string.
	Both uppercase and lowercase vowels are counted.
	Only a, e, i, o, and u are vowels for this task.'''


#4. Algorithm
'''1. Start the program.
   2. Read a string.
   3. Set count = 0.
   4. For each character, convert it to lowercase and check if it is a vowel.
   5. If it is a vowel, increase count by 1.
   6. Display count.
   7. Stop.'''


#5. Mermaid Flowchart Code (Descriptive)
'''flowchart TD
    A([Start]) --> B[/Enter a word or sentence/]
    B --> C[Set vowel count = 0]
    C --> D{Are there more characters?}
    D -- Yes --> E[Convert character to lowercase]
    E --> F{Is character a, e, i, o or u?}
    F -- Yes --> G[Increase count by 1]
    F -- No --> H[Move to next character]
    G --> H
    H --> D
    D -- No --> I[/Display vowel count/]
    I --> J([Stop])'''


#6. Pseudocode
'''START
INPUT text
count <- 0
FOR each character ch in text DO
    IF lowercase(ch) is in "aeiou" THEN
        count <- count + 1
    END IF
END FOR
OUTPUT count
STOP'''


#7. Python Source Code
text = input("Enter a word or sentence: ")
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count = count + 1

print("Number of vowels:", count)


#8. Output 
'''Sample console output:
Enter a word or sentence: education
Number of vowels: 5'''


#9. Conclusion
'''The program uses a loop and string conditions to count vowels in a word or sentence.'''
