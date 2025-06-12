import re
import sys

def print_banner():
    banner = r"""
  _      _  __     __      _        _              
 | |    (_)/ _|    \ \    / /     | |             
 | |     _| |_ ___  \ \  / /__  ___| |_ ___  _ __  
 | |    | |  _/ _ \  \ \/ / _ \/ __| __/ _ \| '__| 
 | |____| | || (_) |  \  /  __/\__ \ || (_) | |    
 |______|_|_| \___/    \/ \___||___/\__\___/|_|    
                                                  
             🔐 Password Strength Checker
             🔧 Developed by: LK
    """
    print(banner)

def check_password_strength(password):
    strength = 0
    feedback = []

    # Criteria
    length = len(password)
    upper = re.search(r'[A-Z]', password)
    lower = re.search(r'[a-z]', password)
    digit = re.search(r'\d', password)
    special = re.search(r'[\W_]', password)

    if length >= 12:
        strength += 2
    elif length >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if upper:
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    if lower:
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    if digit:
        strength += 1
    else:
        feedback.append("Include at least one number (0-9).")

    if special:
        strength += 1
    else:
        feedback.append("Include at least one special character (e.g., !, @, #, etc.).")

    # Strength rating
    if strength >= 6:
        rating = "🟢 Very Strong"
    elif strength == 5:
        rating = "🟡 Strong"
    elif strength == 4:
        rating = "🟠 Moderate"
    else:
        rating = "🔴 Weak"

    return rating, feedback

def main():
    print_banner()
    password = input("🔑 Enter your password: ").strip()
    rating, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {rating}")
    if feedback:
        print("💡 Suggestions to improve your password:")
        for tip in feedback:
            print(f"  - {tip}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
        sys.exit(0)
