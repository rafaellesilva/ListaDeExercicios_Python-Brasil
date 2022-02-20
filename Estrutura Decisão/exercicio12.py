hours_value = float(input('Enter value hours value: '))
number_hours_worked_month = float(input('Enter value number of hours worked in the month: '))

gross_wage = hours_value * number_hours_worked_month

if gross_wage <= 900:
    discountIR = None
elif gross_wage <= 1500:
    discountIR = gross_wage * 0.05
elif gross_wage <= 2500:
    discountIR = gross_wage * 0.1
else:
    discountIR = gross_wage * 0.2

print(15 * ' ',f'Gross wage                   : R$ {gross_wage:.2f}')
print(15 * ' ',f'IR                           : R$ {discountIR:.2f}')
print(15 * ' ',f'INSS                         : R$ {gross_wage * 0.1:.2f}')
print(15 * ' ',f'FGTS                         : R$ {gross_wage * 0.11:.2f}')
print(15 * ' ',f'Total discounts              : R$ { (discountIR + (gross_wage * 0.1)):.2f}')
print(15 * ' ',f'Net salary                   : R$ {(gross_wage - discountIR - (gross_wage * 0.1)):.2f}')