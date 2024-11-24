month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

month = int(input("Enter the month number (1-12): "))
if 1 <= month <= 12:
    print(f"This month has {month_days[month]} days.")
else:
    print("Wrong month number.")

# leap year
month = int(input("Enter the month number (Choose from 1-12): "))
if month == 2:
    leap_year = input("Is it a leap year? (yes/no): ").lower()
    days = 29 if leap_year == "yes" else 28
    print(f"February has {days} days.")
