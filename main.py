import re

def is_strong_password(password):
    # Check if the password meets the following criteria:
    # 1. Minimum length of 8 characters
    # 2. Contains at least one uppercase letter
    # 3. Contains at least one lowercase letter
    # 4. Contains at least one digit
    # 5. Contains at least one special character (e.g., !, @, #, $, %, etc.)
    
    # Minimum length check
    if len(password) < 8:
        return False
    
    # Uppercase letter check
    if not any(char.isupper() for char in password):
        return False
    
    # Lowercase letter check
    if not any(char.islower() for char in password):
        return False
    
    # Digit check
    if not any(char.isdigit() for char in password):
        return False
    
    # Special character check
    special_characters = r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]"
    if not re.search(special_characters, password):
        return False
    
    return True

def main():
    print("Welcome to the Password Strength Checker!")
    password = input("Please enter your password: ")
    
    if is_strong_password(password):
        print("Congratulations! Your password is strong.")
    else:
        print("Your password is weak. Please make it stronger by following the criteria.")
        print("Criteria:")
        print("- Minimum length of 8 characters")
        print("- Contains at least one uppercase letter")
        print("- Contains at least one lowercase letter")
        print("- Contains at least one digit")
        print("- Contains at least one special character (e.g., !, @, #, $, %, etc.)")

if __name__ == "__main__":
    main()
