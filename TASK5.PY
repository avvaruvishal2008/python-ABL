#5. ATM Balance Simulation

#1. Problem Statement
'''Write a simple Python program to display an account balance and allow one withdrawal if the withdrawal amount does not exceed the balance.'''


#2. Objectives
'''	Store an initial balance.
	Read a withdrawal amount.
	Use a condition to approve or reject a withdrawal.'''


#3. Assumptions
'''The initial balance is ₹5,000.
	The withdrawal amount is positive.
	No transaction fee is charged.'''


#4. Algorithm
'''1. Start the program.
   2. Set balance to 5000.
   3. Read the withdrawal amount.
   4. If amount is positive and no greater than balance, subtract it from balance.
   5. Otherwise, display an invalid amount or insufficient balance message.
   6. Display the remaining balance.
   7. Stop.'''


#5. Mermaid Flowchart Code (Descriptive)
'''flowchart TD
    A([Start]) --> B[Set balance to Rs. 5000]
    B --> C[/Enter withdrawal amount/]
    C --> D{Is amount positive and within balance?}
    D -- Yes --> E[Subtract amount from balance]
    D -- No --> F[Display invalid amount or insufficient balance]
    E --> G[/Display remaining balance/]
    F --> G
    G --> H([Stop])'''

#6. Pseudocode
'''START
balance ← 5000
INPUT amount
IF amount > 0 AND amount ≤ balance THEN
    balance ← balance − amount
    OUTPUT "Withdrawal successful"
ELSE
    OUTPUT "Invalid amount or insufficient balance"
END IF
OUTPUT balance
STOP'''


#7. Python Source Code
balance = 5000
amount = int(input("Enter withdrawal amount: "))

if amount > 0 and amount <= balance:
    balance = balance - amount
    print("Withdrawal successful")
else:
    print("Invalid amount or insufficient balance")

print("Remaining balance: Rs.", balance)


#8. Output 
'''Sample console output:
Enter withdrawal amount: 1500
Withdrawal successful
Remaining balance: Rs. 3500'''


#9. Conclusion
'''The program simulates a basic withdrawal and prevents withdrawing more money than the available balance.'''

 