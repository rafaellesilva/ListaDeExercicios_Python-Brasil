employee_salary = float(input('Enter the value of your salary: '))

if employee_salary <= 280:
    increase = employee_salary * 0.2
    percentage_increase = '20%'
elif employee_salary > 280 and employee_salary <= 700:
    increase = employee_salary * 0.15
    percentage_increase = '15%'
elif employee_salary > 700 and employee_salary <= 1500:
    increase = employee_salary * 0.1
    percentage_increase = '10%'
else:
    increase = employee_salary * 0.05
    percentage_increase = '5%'

print(f'The salary before the adjustment: R$ {employee_salary:.2f}')
print(f'The amount of the increase: R$ {percentage_increase}')
print(f'The new salary after the raise: R$ {employee_salary + increase}')