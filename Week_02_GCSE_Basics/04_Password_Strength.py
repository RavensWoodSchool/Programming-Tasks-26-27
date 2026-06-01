"""
TASK: 04 Password Strength

# Skills: Strings, loops, selection
Ask the user to enter a password, and check that they meet these conditions:
- At least 8 characters
- Contains a number
- Contains a captial and lower cased letter
- Extend for one special character
Print a response of weak, medium or strong for how many they pass.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

passsword = input("Enter a password: ")
score = 0

if len(password) >= 8:
    score += 1

for char in password:
    if char.isdigit():
        score += 1
        break

if password.lower() != password and password.upper() != password:
    score += 1
special = "!@%$#*^"
for char in password:
    if char in special:
        score += 1
        break

if score <= 1:
    print("Weak")
elif score <= 3:
    print("Medium")
else:
    print("Strong")

