#constant

TAX_RATE=0.1

#input

name=input("Enter your name:")
salary=float(input("Enter your salary:"))

#calculatins

tax_amount=salary*TAX_RATE
net_salary=salary-tax_amount

#output

print("Name:",name)
print("Gross Salary:",salary)
print("Tax Amount:",tax_amount)
print("Net Salary:",net_salary)
