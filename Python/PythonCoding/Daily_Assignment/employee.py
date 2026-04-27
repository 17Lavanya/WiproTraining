class Employee:
    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    # Getters
    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    # Setters
    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative!")

    # Display employee info
    def display_info(self):
        print("----- Employee Information -----")
        print(f"Employee ID: {self.__emp_id}")
        print(f"Name: {self.__name}")
        print(f"Salary: {self.__salary}")
        print("-------------------------------")

    # Salary hike
    def give_hike(self, percentage):
        if percentage > 0:
            hike_amount = self.__salary * (percentage / 100)
            self.__salary += hike_amount
            print(f"Salary increased by {percentage}%. New salary: {self.__salary}")
        else:
            print("Percentage must be positive!")
