# Vivek's Flowchart

users = int(input("Enter number of users: "))
returning = True if input("Is the user returning? (Y/N): ").upper() == "Y" else False
storage_amount = int(input("Enter storage amount in GB: "))

total = 0

if returning:
    total += 5 * users * 0.95
else:
    total += 5 * users

total += total * 0.2

total += storage_amount * 0.1 * 2

print(f"Total cost: £{total:.2f}")