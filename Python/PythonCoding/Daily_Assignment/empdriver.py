from employee import Employee

print("Employee Management System Demo")

# Create employees with predefined values
emp1 = Employee("E101", "ABC", 50000)
emp2 = Employee("E102", "XYZ", 60000)

# Display initial info
emp1.display_info()
emp2.display_info()

# Give salary hikes
print("\n--- Salary Hikes ---")
emp1.give_hike(10)   # 10% hike
emp2.give_hike(15)   # 15% hike

# Display updated info
print("\n--- Updated Employee Information ---")
emp1.display_info()
emp2.display_info()
