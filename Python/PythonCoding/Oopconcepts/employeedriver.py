from Oopconcepts.EmployeeDetails import EmployeeDetails
# driver
eno = int(input('Emp no: '))
name = input('Emp name: ')
bp = float(input('Basic pay: '))
employee = EmployeeDetails(eno, name, bp)

print('Emp no: ', employee.empno)
print('Emp name: ', employee.ename)
print('Basic pay: ', employee.basic_pay)
print('Salary: ', employee.calculate_netsal())