import datetime

# 1. Get and print the current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

# 2. Calculate and print the number of days between two dates
date1 = datetime.date(2026, 4, 24)   # Example: 24 April 2026
date2 = datetime.date(2026, 12, 31)  # Example: 31 December 2026
difference = date2 - date1
print("Number of days between", date1, "and", date2, "is:", difference.days)

# 3. Format and print the current date in "DD-MM-YYYY"
formatted_date = current_datetime.strftime("%d-%m-%Y")
print("Formatted current date:", formatted_date)
