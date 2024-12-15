birth_year = int(input("Enter the birth year: "))
birth_month = int(input("Enter the birth month (1-12): "))
birth_day = int(input("Enter the birth date (1-31): "))

current_year = int(input("Enter the current year: "))
current_month = int(input("Enter the current month (1-12): "))
current_day = int(input("Enter the current date (1-31): "))

age_years = current_year - birth_year
age_months = current_month - birth_month
age_days = current_day - birth_day

if age_days < 0:
    age_months -= 1
    age_days += 30

if age_months < 0:
    age_years -= 1
    age_months += 12

if current_month == birth_month and current_day == birth_day:
    print(f"You are {age_years} years")
else:
    print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")