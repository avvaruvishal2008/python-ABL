#4. Simple Shopping Bill

#1. Problem Statement
'''Write a Python program to read the price and quantity of an item, calculate the total cost, and give a 10% discount when the total is Rupees1,000 or more.'''


#2. Objectives
'''	Read item price and quantity.
	Calculate the total cost.
	Apply a discount when the condition is satisfied.'''


#3. Assumptions
'''	Price and quantity are positive values.
	A 10% discount is given for totals of Rupees1,000 or more.
	No tax or delivery charge is included.'''


#4. Algorithm
'''1. Start the program.
   2. Read price and quantity.
   3. Calculate total = price * quantity.
   4. If total is at least 1000, discount = total * 10 / 100; otherwise discount = 0.
   5. Calculate final amount = total - discount.
   6. Display total, discount, and final amount.
   7. Stop.'''


#5. Mermaid Flowchart Code (Descriptive)
'''flowchart TD
    A([Start]) --> B[/Enter price and quantity/]
    B --> C[Calculate total amount]
    C --> D{Is total at least Rs. 1000?}
    D -- Yes --> E[Calculate 10 percent discount]
    D -- No --> F[Discount = 0]
    E --> G[Calculate final amount]
    F --> G
    G --> H[/Display total, discount and final amount/]
    H --> I([Stop])'''


#6. Pseudocode
'''START
INPUT price, quantity
total <- price * quantity
IF total >= 1000 THEN
    discount <- total * 10 / 100
ELSE
    discount <- 0
END IF
final_amount <- total - discount
OUTPUT total, discount, final_amount
STOP'''


#7. Python Source Code
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if total >= 1000:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

print("Total amount: Rs.", total)
print("Discount: Rs.", discount)
print("Final amount: Rs.", final_amount)


#8. Output Screenshot
'''Sample console output:
Enter item price: 600
Enter quantity: 2
Total amount: Rs. 1200.0
Discount: Rs. 120.0
Final amount: Rs. 1080.0'''


#9. Conclusion
'''he program calculates a shopping total and applies a 10% discount when the total reaches Rupees1,000.'''

 