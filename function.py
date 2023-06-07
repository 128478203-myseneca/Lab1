from datetime import datetime

def calculate_age():
    current_year = datetime.now().year
    birth_year = int(input("Enter your birth year: "))
    
    age = current_year - birth_year
    return age

age = calculate_age()
print("Your age is:", age)
