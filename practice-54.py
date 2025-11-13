import re

def check_password_strength(password):
    length = len(password) >= 8
    upper = bool(re.search(r'[A-Z]', password))
    lower = bool(re.search(r'[a-z]', password))
    digit = bool(re.search(r'\d', password))
    special = bool(re.search(r'[@$!%*?&#]', password))
    score = sum([length, upper, lower, digit, special])

    if score == 5:
        return "Strong 💪"
    elif 3 <= score < 5:
        return "Medium ⚡"
    else:
        return "Weak ❌"

password = input("Enter your password: ")
print("Password Strength:", check_password_strength(password))
