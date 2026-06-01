"""
TASK: 05 Shopping List

# Skills: Loops, lists
Allow the user to add itemds to a shopping list until they type DONE
When they type DONE, print the list and ask if they want to edit any item.
They should select an item by number and allow them to ammend the item.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

shopping_list = []

while True:
    item = input("Enter an item(or DONE to finish): ")

    if item.upper() == "DONE":
        break
    shopping_list.append(item)

print("\nShopping list:")
for i in range(len(shopping_list)):
    print(i + !, "-", shopping_list[i])

