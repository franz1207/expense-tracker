# Project: Expense Tracker - Installment 2
# Author: Franz Gerald P. Beco
# Description: Landing page plus a two expense logger with total and average.

print("=" * 40)
print("EXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("\t[1] Add an expense\t\t(coming soon)")
print("\t[2] View all expenses\t\t(coming soon)")
print("\t[3] Show total spent\t\t(coming soon)")
print("\t[4] Exit\t\t\t(coming soon)")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print("\n" + "-" * 40)
print("SUMMARY")
print(f"- {item1}: ${amount1}")
print(f"- {item2}: ${amount2}")
print(f"Total spent: ${total}")
print(f"Average: ${average}")
print("-" * 40)
print(f"Made by: {name}  |  Installment 2")